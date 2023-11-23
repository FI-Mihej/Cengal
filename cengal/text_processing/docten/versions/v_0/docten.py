#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#     http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import platform, sys
import codecs

"""
Determination Of the Correct Text Encoding
Obsolete. Use: `cengal/text_processing/encoding_detection` instead
"""

__author__ = "ButenkoMS <gtalk@butenkoms.space>"
__copyright__ = "Copyright © 2012-2024 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "4.0.3"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


class BomInfo:
    def __init__(self, encodingName, strWithBOM):
        self.encodingName = encodingName
        self.strWithBOM = strWithBOM


class TextData:
    def __init__(self, bomInfo, text):
        self.bomInfo = bomInfo
        self.text = text


def parse_unicode_text(fData, isNeedToDecodeText=True):
    # utf8_BOM = bytes([0xef, 0xbb, 0xbf])
    # utf16LE_BOM = bytes([0xff, 0xfe])
    # utf16BE_BOM = bytes([0xfe, 0xff])
    utf8_BOM = codecs.BOM_UTF8
    utf16LE_BOM = codecs.BOM_UTF16_LE
    utf16BE_BOM = codecs.BOM_UTF16_BE
    spaceInUtf16LE = bytes([0x20, 0x00])
    spaceInUtf16BE = bytes([0x00, 0x20])
    isUTF = False
    isUTF16LE = False
    isUTF16BE = False
    isWithBOM = False

    #------------------
    #Preparing
    #------------------

    #preparing data: removing BOM if it exist
    #preparing triggers
    if fData.startswith(utf8_BOM):
        isUTF = True
        isWithBOM = True
        fData = fData[len(utf8_BOM):]
    elif fData.startswith(utf16LE_BOM):
        isUTF16LE = True
        isWithBOM = True
        fData = fData[len(utf16LE_BOM):]
    elif fData.startswith(utf16BE_BOM):
        isUTF16BE = True
        fData = fData[len(utf16BE_BOM):]
    elif (fData.count(spaceInUtf16BE) > 1) or (1 < fData.count(spaceInUtf16LE)):
        isWithBOM = False
        if (platform.system() == 'Windows') and (sys.byteorder == 'little'):
            isUTF16LE = True
        else:
            isUTF16BE = True

    #preparing file for editing: converting from UTF-16 if needed
    encodingName = 'utf-8'
    if isUTF:
        encodingName = 'utf-8'
    elif isUTF16LE:
        encodingName = 'utf-16le'
    elif isUTF16BE:
        encodingName = 'utf-16be'

    if isNeedToDecodeText:
        fData = str(fData, encodingName)

    #preparing BOM-trigger
    strWithBOM = b''
    if isWithBOM:
        if isUTF :
            strWithBOM = utf8_BOM
        elif isUTF16LE:
            strWithBOM = utf16LE_BOM
        elif isUTF16BE:
            strWithBOM = utf16BE_BOM

    bomInfo = BomInfo(encodingName, strWithBOM)
    textData = TextData(bomInfo, fData)
    return textData


def compile_unicode_text(textData):
    #preparing edited file for writing to disk: converting to UTF-16 if needed
    fData = bytes(textData.text, textData.bomInfo.encodingName)
    fData = textData.bomInfo.strWithBOM + fData
    return fData


def read_text_from_file(inputFile):
    textData = None
    with open(inputFile, "rb") as file:
        fData = file.read()
        textData = parse_unicode_text(fData)
    return textData


def write_text_to_file(outputFile, textData):
    #Writing edited file to disk
    with open(outputFile, "wb") as file:
        file.write(compile_unicode_text(textData))

# def remove_all_nonUtf8_symbols_from_utf8_text(binData, bytesFiller=b''):
#     data = parse_unicode_text(binData, False)
#     counter = 0
#     while counter < len(data.text):
#         if data.text[counter] > 0x7f:
#             # data.text[counter] = bytesFiller  # this is doesn't work
#             data.text = data.text[:counter] + bytesFiller + data.text[counter+1:]
#         else:
#             counter += 1
#     result = data.bomInfo.strWithBOM + data.text
#     return result


def remove_all_nonUtf8_symbols_from_utf8_text(binData):
    data = parse_unicode_text(binData, False)
    inputBinData = binData
    encodingName = 'utf-8'
    if data.bomInfo.encodingName.startswith('utf'):
        inputBinData = data.text
        encodingName = data.bomInfo.encodingName
    bufStr = inputBinData.decode(encodingName, 'replace')
    inputBinData = bufStr.encode(encodingName)

    result = data.bomInfo.strWithBOM + inputBinData
    return result


def get_BOM_from_text(binText):
    bomsList = (
        codecs.BOM
        , codecs.BOM_BE
        , codecs.BOM_LE
        , codecs.BOM32_BE
        , codecs.BOM32_LE
        , codecs.BOM64_BE
        , codecs.BOM64_LE
        , codecs.BOM_UTF8
        , codecs.BOM_UTF16
        , codecs.BOM_UTF16_BE
        , codecs.BOM_UTF16_LE
        , codecs.BOM_UTF32
        , codecs.BOM_UTF32_BE
        , codecs.BOM_UTF32_LE
    )

    result = (binText, None)

    for bom in bomsList:
        if binText.startswith(bom):
            result = (binText[len(bom):], bom)

    return result
