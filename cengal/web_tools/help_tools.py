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


import platform
if 'PyPy' != platform.python_implementation():
    import requests
import binascii
import os, os.path
import pickle
import datetime
# try to import C parser then fallback in pure python parser.
try:
    from http_parser.parser import HttpParser
except ImportError:
    from http_parser.pyparser import HttpParser

from cengal.modules_management import alt_import

with alt_import('lzma') as lzma:
    if lzma is None:
        import lzmaffi.compat
        lzmaffi.compat.register()
        import lzma


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
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


def remove_percent_encoding_from_the_URI(string, plus=True):
    try:
        string = str(string)
        if plus:
            string = string.replace('+', ' ')
        string = string.encode(encoding='utf-8')
        percentTypes = ((b'%u', 6, (False, None)), (b'%', 3, (True, tuple(range(32)) + (34, 42, 58, 60, 62, 63, 124, 127))))
        # (prefix, full size, (allowed type or not at all, list of disallowed characters like backspace etc.))
        for percType in percentTypes:
            isDone = False
            while not isDone:
                index = string.find(percType[0])
                if index > -1:
                    ind2 = index+percType[1]
                    if ind2 > len(string):
                        ind2 = len(string)
                    hexString = string[index:ind2]
                    hexString = hexString[len(percType[0]):]
                    decodedString = b''
                    if percType[2][0]:
                        try:
                            decodedStringBuff = binascii.unhexlify(hexString)
                            if int.from_bytes(decodedStringBuff, byteorder='little') not in percType[2][1]:
                                decodedString = decodedStringBuff
                        except binascii.Error:
                            pass
                    string = string[:index] + decodedString + string[ind2:]
                else:
                    isDone = True
            if percType[2][0]:
                if (len(string) > 0) and (len(set(string).intersection(set(percType[2][1]))) > 0):
                    index = 0
                    isDone = False
                    while not isDone:
                        if string[index] in percType[2][1]:
                            string = string[:index] + string[index+1:]
                        else:
                            index += 1
                        if index >= len(string):
                            isDone = True
        string = string.decode(encoding='utf-8')
    except UnicodeDecodeError:
        string = None
    except UnicodeEncodeError:
        string = None
    return string


def get_standard_folder_separator():
    return '/'


def unify_folder_separators(string):
    string = str(string)
    string = string.replace('\\', get_standard_folder_separator())
    return string


def remove_forbidden_file_names_from_the_URI(string):
    # replace forbidden file names with slash ('/'). Also will unify folder separators (replace '\' with '/')
    forbiddenFileNames = {'con', 'prn', 'aux', 'nul', 'com1', 'com2', 'com3', 'com4', 'com5', 'com6', 'com7', 'com8'
        , 'com9', 'lpt1', 'lpt2', 'lpt3', 'lpt4', 'lpt5', 'lpt6', 'lpt7', 'lpt8', 'lpt9'}
    string = unify_folder_separators(str(string))
    strBuffer = string
    string = string.lower()
    for forbFile in forbiddenFileNames:
        string = string.replace(get_standard_folder_separator() + forbFile + get_standard_folder_separator(), '/')
        string = string.replace(get_standard_folder_separator() + forbFile + '.', '/')
    isStrWasChanged = False
    if strBuffer.lower() != string:
        isStrWasChanged = True
    else:
        string = strBuffer
    result = (string, isStrWasChanged)
    return result


def remove_path_to_the_parent_of_the_current_directory(string):
    string = unify_folder_separators(str(string))
    string = string.replace('../', '/')
    string = string.replace('/..', '/')
    return string


def is_path_is_trying_to_leave_site_sandbox(string):
    itemsList = string.split(get_standard_folder_separator())
    while '' in itemsList:
        itemsList.remove('')
    counter = 0
    for item in itemsList:
        if item == '..':
            counter -= 1
        elif item == '.':
            pass
        else:
            counter += 1
        if counter < 0:
            return True
    return False


def is_path_is_not_safe(string):
    # return tuple (decoded string, is_path_is_not_safe)
    result = tuple()
    string = remove_percent_encoding_from_the_URI(string)
    if string is None:
        result = (string, True)
        return result
    string = remove_forbidden_file_names_from_the_URI(string)
    if string[1]:
        result = (string[0], True)
        return result
    is_not_safe = is_path_is_trying_to_leave_site_sandbox(string[0])
    result = (string[0], is_not_safe)
    return result


def web_server__is_redirection_to_the_main_domain_needed(httpParser: HttpParser, prefix=None):
    functionResult = False

    host = httpParser.get_headers()['Host']
    domain = host
    if ':' in host:
        host = host.split(':')
        while '' in host:
            host.remove('')
        domain = host[0]
    if '.' in domain:
        domain = domain.split('.')
        if domain[0] == '':
            del domain[0]
            functionResult = True
        if prefix is not None:
            if domain[0] != prefix:
                domain.insert(0, prefix)
                functionResult = True
        lastDLen = len(domain) - 1
        if domain[lastDLen] == '':
            del domain[lastDLen]
            functionResult = True
        domain = '.'.join(domain)
    if host.__class__ is list:
        if len(host) > 1:
            host[0] = domain
            domain = ':'.join(host)

    functionResult = (functionResult, domain)
    return functionResult


def load_cache_from_file(fileName, originalCache):
    fileName = unify_folder_separators(fileName)
    cache = originalCache
    if os.path.exists(fileName):
        if os.path.isfile(fileName):
            cacheDataFile = None
            dataBuff = originalCache
            try:
                # cacheDataFile = open(fileName, 'rb')
                cacheDataFile = lzma.open(fileName, 'rb')
                cache = pickle.load(cacheDataFile)
                dataBuff.update(cache)
                cache = dataBuff
            except(EnvironmentError, pickle.PicklingError) as err:
                cache = dataBuff
            finally:
                if cacheDataFile is not None:
                    cacheDataFile.close()
    return cache


def save_cache_to_file(fileName, cache):
    fileName = unify_folder_separators(fileName)
    if cache.isWasChanged:
        isRenamedToBak = False
        if os.path.exists(fileName):
            try:
                if os.path.exists(fileName+'.bak'):
                    try:
                        os.remove(fileName+'.bak')
                    except IOError:
                        pass
                os.rename(fileName, fileName+'.bak')
                isRenamedToBak = True
            except IOError:
                pass

        isDumped = False
        cacheDataFile = None
        try:
            # cacheDataFile = open(fileName, 'wb')
            cacheDataFile = lzma.open(fileName, 'wb', format=lzma.FORMAT_XZ, check=lzma.CHECK_CRC64, preset=1)
            pickle.dump(cache, cacheDataFile)
            cache.isWasChanged = False
            isDumped = True
        except(EnvironmentError, pickle.PicklingError) as err:
            pass
        finally:
            if cacheDataFile is not None:
                cacheDataFile.close()

        if isRenamedToBak and isDumped:
            try:
                os.remove(fileName+'.bak')
            except IOError:
                pass


class CachedRequestError(Exception): pass


def make_cached_request__get(cache, request, useOnlyCachedResults=False):
    result = cache.try_to_get_data_for_request(request)
    if (result is None) or (not result.ok):
        if useOnlyCachedResults:
            raise CachedRequestError()
        result = requests.get(unify_folder_separators(request))
        result = SerializableHttpResponseFromRequests(result)
        cache.put_new_request(request, result)

    return result


def make_cached_request__universal(cache, request, workerFunction, useOnlyCachedResults=False, **workerFunctionParams):
    result = cache.try_to_get_data_for_request(request)
    if result is None:
        if useOnlyCachedResults:
            raise CachedRequestError()
        result = workerFunction(**workerFunctionParams)
        cache.put_new_request(request, result)

    return result


def make_a_copy_of_cached_request_with_another_keyname(cache, current_name, new_name, make_first_copy_only=False):
    is_copy_avaliable = True
    if make_first_copy_only:
        test = cache.try_to_get_data_for_request(current_name)
        if test is not None:
            is_copy_avaliable = False
    if is_copy_avaliable:
        result = cache.try_to_get_data_for_request(current_name)
        if result is not None:
            cache.put_new_request(new_name, result)


class SerializableHttpResponseFromRequests:
    def __init__(self, request, isBinaryFile=False):
        super(SerializableHttpResponseFromRequests, self).__init__()
        self.isBinaryFile = isBinaryFile
        self.url = request.url
        self.ok = request.ok
        self.reason = request.reason
        self.status_code = request.status_code
        self.headers = request.headers
        self.encoding = request.encoding

        if 'content' in dir(request):
            self.content = request.content
        else:
            self.content = None

        # if not isBinaryFile:
        #     if 'apparent_encoding' in dir(request):
        #         self.apparent_encoding = request.apparent_encoding
        #     else:
        #         self.apparent_encoding = None
        # else:
        #     self.apparent_encoding = None
        self.apparent_encoding = None

        # if (self.encoding is not None) or (self.apparent_encoding is not None):
        #     self.text = request.text
        # else:
        #     self.text = None
        self.text = None

    def getResultEncoding(self):
        if self.encoding is not None:
            return self.encoding
        elif self.apparent_encoding is not None:
            return self.apparent_encoding
        else:
            return 'utf-8'

    def getBytesContent(self):
        if self.content is not None:
            return self.content
        elif self.text is not None:
            bData = bytes(self.text, self.getResultEncoding())
            return bData
        else:
            print("Can't get data from the request object on url ", self.url)
            raise Exception


def saveRequestedFileToFS(folderName, requestResult):
    fileName = folderName + os.path.basename(requestResult.url)
    fileName = unify_folder_separators(fileName)
    with open(fileName, 'wb') as file:
        if requestResult.content is not None:
            file.write(requestResult.content)
        elif requestResult.text is not None:
            bData = bytes(requestResult.text, requestResult.getResultEncoding())
            file.write(bData)
        else:
            ex_text = "Can't save object from {} to the fie. Can't get data to save".format(requestResult.url)
            print(ex_text)
            raise Exception(ex_text)


def getFileModificationDate(fileName):
    fileName = unify_folder_separators(fileName)
    t = os.path.getmtime(fileName)
    return datetime.datetime.fromtimestamp(t)


