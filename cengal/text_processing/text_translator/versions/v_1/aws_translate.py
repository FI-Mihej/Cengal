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


import sys, os, boto3, json, pickle, logging
from enum import Enum
from typing import Dict, Optional, Any, Tuple
from cengal.file_system.path_manager import path_relative_to_cwd
from .aws_translate__supported_languages import codes, names, name_by_code
_boto3_client = None

def aws_client():
    global _boto3_client
    if _boto3_client is None:
        aws_init()
    return _boto3_client


def aws_init(region_name: Optional[str]=None):
    global _boto3_client
    region_name = region_name or 'us-east-1'
    _boto3_client = boto3.client(service_name='translate', region_name=region_name, use_ssl=True)


_logger = None

def init_logger():
    global _logger
    _logger = logging.getLogger('text_dictionary_translator')


def log() -> logging.Logger:
    if _logger is None:
        init_logger()
    return _logger


class AwsClientForTranslateText:

    def __init__(self, cache_file_path: Optional[str]=None) -> None:
        self._cache_file_path = cache_file_path
        self._cache = None

    def _prepare(self):
        if self._cache is None:
            if self._cache_file_path is None:
                return False
            if os.path.exists(self._cache_file_path) and os.path.isfile(self._cache_file_path):
                with open(self._cache_file_path, 'rb') as file:
                    self._cache = pickle.load(file)
                    return True
            else:
                self._cache = dict()
                return True
        else:
            return True

    def save(self):
        if self._cache_file_path is not None:
            if self._cache is None:
                text_dictionary = dict()
            else:
                text_dictionary = self._cache
            with open(self._cache_file_path, 'wb') as file:
                pickle.dump(text_dictionary, file)

    def _cache_get(self, key, default: Optional[Any]=None) -> Any:
        if self._cache is not None:
            return self._cache.get(key, default)
        return default

    def _cache_set(self, key, value: Any) -> Any:
        if self._cache is not None:
            self._cache[key] = value

    def __call__(self, text, source_language_code, target_language_code):
        result = None
        if self._prepare():
            key = (
             text, source_language_code, target_language_code)
            result = self._cache_get(key)
        if result is None:
            result = aws_client().translate_text(Text=text, SourceLanguageCode=source_language_code,
              TargetLanguageCode=target_language_code)
            result = result.get('TranslatedText')
            if self._prepare():
                self._cache_set(key, result)
        return result


aws_translate: AwsClientForTranslateText = None

class TextCaseTypes(Enum):
    mixed = 0
    lower = 1
    capitalized = 2
    title = 3
    upper = 4


def detect_text_case(text: str) -> TextCaseTypes:
    if text.islower():
        return TextCaseTypes.lower
    if text.istitle():
        return TextCaseTypes.title
    if text.isupper():
        return TextCaseTypes.upper
    if text:
        if text[0].istitle():
            second_part = text[1:]
            if second_part:
                if text[1:].islower():
                    return TextCaseTypes.capitalized
            else:
                return TextCaseTypes.capitalized
    return TextCaseTypes.mixed


def apply_text_case(text: str, case: TextCaseTypes) -> str:
    if TextCaseTypes.mixed == case:
        return text
    if TextCaseTypes.lower == case:
        return text.lower()
    if TextCaseTypes.capitalized == case:
        return text.capitalize()
    if TextCaseTypes.title == case:
        return text.title()
    if TextCaseTypes.upper == case:
        return text.upper()
    raise RuntimeError(f"Unknown text case type: {case}")


def translate(text, source_language_code, target_language_code):
    case = detect_text_case(text)
    translation = aws_translate(text, source_language_code, target_language_code)
    return apply_text_case(translation, case)


def read_text_dictionary(file_path: str) -> Dict:
    with open(file_path, 'rb') as file:
        return json.load(file)


def save_text_dictionary(file_path: str, text_dictionary: Dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        return json.dump(text_dictionary, file, ensure_ascii=False, indent=4)


def translate_text_dictionary(text_dictionary: Dict) -> Dict:
    translated_items = 0
    translated_variants = 0
    translation_requests = 0
    successfull_translation_requests = 0
    sent_characters = 0
    received_characters = 0
    language_in_code = text_dictionary['original_text_language']
    default_language = text_dictionary['default_language']
    translation_language_map = text_dictionary['translation_language_map']
    if default_language in translation_language_map:
        default_language = translation_language_map[default_language]
    manually_translated_to = set(text_dictionary.get('manually_translated_to', list()))
    all_translated_codes = set(codes())
    translated_codes = set()
    for code in codes():
        code = code.lower()
        if code in translation_language_map:
            code = translation_language_map[code]
        else:
            translation_language_map[code] = code
        translated_codes.add(code)

    translated_codes = list(translated_codes)
    translated_codes.sort()
    translated_to = all_translated_codes | manually_translated_to
    auto_translated_to = all_translated_codes - manually_translated_to
    auto_translated_to = list(auto_translated_to)
    auto_translated_to.sort()
    text_dictionary['auto_translated_to'] = auto_translated_to
    translated_to = list(translated_to)
    translated_to.sort()
    text_dictionary['translated_to'] = translated_to
    manually_translated_to = list(manually_translated_to)
    manually_translated_to.sort()
    text_dictionary['manually_translated_to'] = manually_translated_to
    rtl_languages = [
     'ar', 'he', 'fa', 'ur']
    rtl_languages.sort()
    text_dictionary['rtl_languages'] = rtl_languages
    present_laguages_names = text_dictionary.get('laguages_names', dict())
    laguages_english_names = dict()
    laguages_names = dict()
    log().info('Translating language names ->')
    for code in codes():
        original_name = name_by_code(code)
        laguages_english_names[code] = original_name
        if code in present_laguages_names:
            continue
        try:
            translation_requests += 1
            sent_characters += len(original_name)
            translation_result = translate(original_name, 'en', code)
            successfull_translation_requests += 1
            received_characters += len(translation_result)
            log().info(f"\t[{code}]: {translation_result}")
            laguages_names[code] = translation_result
        except:
            log().exception('\t -> [{code}] Translation Failed.')

    text_dictionary['laguages_english_names'] = laguages_english_names
    present_laguages_names.update(laguages_names)
    text_dictionary['laguages_names'] = present_laguages_names
    text_translation_list = text_dictionary['text_translation_list']
    for item in text_translation_list:
        translated_items += 1
        text_in_code = item['text']
        if 'translations' not in item:
            item['translations'] = {'default': dict()}
        else:
            translations = item['translations']
            copy_settings = item.get('copy_settings', dict())
            for tr_variant_name, tr_variant_data in translations.items():
                if tr_variant_name in copy_settings:
                    variant_copy_settings = copy_settings[tr_variant_name]
                    variant_copy_default_language = variant_copy_settings['default_language']
                    variant_copy_translation_language_map = variant_copy_settings['translation_language_map']
                    log().info('Copy translation:')
                    for code in translated_codes:
                        if code in tr_variant_data:
                            continue
                        else:
                            copy_source_language_code = variant_copy_translation_language_map.get(code, variant_copy_default_language)
                            copy_source_text = tr_variant_data[copy_source_language_code]
                            log().info(f"\t[{copy_source_language_code}] -> [{code}]: {copy_source_text}")
                            tr_variant_data[code] = copy_source_text

                    continue
                else:
                    if default_language in tr_variant_data:
                        source_language_code = default_language
                        source_text = tr_variant_data[default_language]
                    else:
                        source_language_code = language_in_code
                        source_text = text_in_code
                    log().info(f'Translating [{source_language_code}] "{source_text}" ->')
                    translated_variants += 1
                    for code in translated_codes:
                        if code == source_language_code:
                            continue
                        if code in tr_variant_data:
                            continue
                        try:
                            translation_requests += 1
                            sent_characters += len(source_text)
                            translation_result = translate(source_text, source_language_code, code)
                            successfull_translation_requests += 1
                            received_characters += len(translation_result)
                            log().info(f"\t[{code}]: {translation_result}")
                            tr_variant_data[code] = translation_result
                        except:
                            log().exception('\t -> [{code}] Translation Failed.')

    log().info('Translation Results:')
    log().info(f"\ttranslated_items: {translated_items}")
    log().info(f"\ttranslated_variants: {translated_variants}")
    log().info(f"\ttranslation_requests: {translation_requests}")
    log().info(f"\tsuccessfull_translation_requests: {successfull_translation_requests}")
    log().info(f"\tsent_characters: {sent_characters}")
    log().info(f"\treceived_characters: {received_characters}")
    return text_dictionary


def is_str_equal(text1: str, text2: str):
    return text1.casefold() == text2.casefold()


if __name__ == '__main__':
    aws_init('eu-central-1')
    logging.basicConfig()
    log().setLevel(logging.INFO)
    if 3 <= len(sys.argv):
        text_dictionary_source_file_path = sys.argv[1]
        text_dictionary_result_file_path = sys.argv[2]
        aws_translate_cache_file_path = None
        if 4 <= len(sys.argv):
            aws_translate_cache_file_path = sys.argv[3]
    else:
        text_dictionary_source_file_path = 'text_stylizer/text_dictionaly_src.json'
        text_dictionary_result_file_path = 'text_stylizer/text_dictionaly.json'
        aws_translate_cache_file_path = 'text_stylizer/text_dictionaly_cache.pickle'
    if not os.path.exists(text_dictionary_source_file_path):
        text_dictionary_source_file_path = path_relative_to_cwd(text_dictionary_source_file_path)
        if not os.path.exists(text_dictionary_source_file_path) or os.path.exists(text_dictionary_result_file_path):
            text_dictionary_result_file_path = path_relative_to_cwd(text_dictionary_result_file_path)
            if os.path.exists(text_dictionary_result_file_path):
                pass
            else:
                print(f"ERROR: Result text dictionary file not found: {text_dictionary_result_file_path}")
                text_dictionary_result_file_path = None
        else:
            print(f"ERROR: Source text dictionary file not found: {text_dictionary_source_file_path}")
            text_dictionary_source_file_path = None
    if text_dictionary_source_file_path is not None:
        if text_dictionary_result_file_path is not None:
            print('Loading text dictionary...')
            text_dictionary = read_text_dictionary(text_dictionary_source_file_path)
            print('Translating text dictionary...')
            aws_translate = AwsClientForTranslateText(aws_translate_cache_file_path)
            text_dictionary = translate_text_dictionary(text_dictionary)
            aws_translate.save()
            save_text_dictionary(text_dictionary_result_file_path, text_dictionary)
            print('Done')