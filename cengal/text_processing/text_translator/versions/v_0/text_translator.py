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


__all__ = ['TextTranslationDictionary', 'TextEntityId', 'TranslatableText', 'TranslationLanguageId', 'TextTranslatorError', 'TextTranslator', 'TranslationLanguageMapper', 'TranslationLanguageChooser', 'TextTranslationReapplier', 'CoroPriority', 'tt', 'TranslationWorker']


from collections.abc import Mapping
from typing import Hashable, Dict, Union, Optional, Callable
from cengal.data_manipulation.serialization import *
from cengal.code_flow_control.call_history_reapplier import *
from cengal.parallel_execution.coroutines.coro_scheduler import *
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import *
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import *
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import *
from uuid import uuid4
import sys


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


TranslationLanguageId = Hashable
TextEntityId = Hashable
TranslatableText = str
TextTranslationDictionary = Dict
'''
In Python:
text_translation_dictionary = {
    '{TranslatableText}': {
        'default': {  // Can be empty. "Variants" field must not be empty in this case.
            '{TranslationLanguageId}': '{TranslatableText}',
            '{TranslationLanguageId}': '{TranslatableText}',
            ...
        },
        'variants': {  // Can be empty. "Default" field must not be empty in this case.
            '{TextEntityId}': {
                '{TranslationLanguageId}': '{TranslatableText}',
                '{TranslationLanguageId}': '{TranslatableText}',
                ...
            },
            '{TextEntityId}': {
                '{TranslationLanguageId}': '{TranslatableText}',
                '{TranslationLanguageId}': '{TranslatableText}',
                ...
            },
            ...
        }
    }
}

In JSON:
{
    'type': 'Cengal.TextTranslationDictionary',
    'version': '1.0.0'
    'text_translation_list': [
        {
            'text': '{TranslatableText}',
            'translations': {
                'default': {  // Can be empty. "Variants" field must not be empty in this case.
                    '{TranslationLanguageId}': '{TranslatableText}',
                    '{TranslationLanguageId}': '{TranslatableText}',
                    ...
                },
                'variants': {  // Can be empty. "Default" field must not be empty in this case.
                    '{TextEntityId}': {
                        '{TranslationLanguageId}': '{TranslatableText}',
                        '{TranslationLanguageId}': '{TranslatableText}',
                        ...
                    },
                    '{TextEntityId}': {
                        '{TranslationLanguageId}': '{TranslatableText}',
                        '{TranslationLanguageId}': '{TranslatableText}',
                        ...
                    },
                    ...
                }
            }
        }
    ]
}
'''
TranslationLangToLangMap = Dict[TranslationLanguageId, TranslationLanguageId]
TranslationWorker = Callable[['TranslatableText'], None]


class TextTranslatorError(Exception):
    pass

class TextTranslator:
    @classmethod
    def from_json(cls, json_data: Union[bytes, str], encoding: Optional[str]=None):
        serializer = best_serializer({DataFormats.json,
                                 Tags.decode_str_as_str,
                                 Tags.decode_list_as_list,
                                 Tags.superficial,
                                 Tags.current_platform},
                                test_data_factory(TestDataType.deep_large),
                                0.1)
        encoding = encoding or 'utf-8'
        if isinstance(json_data, bytes):
            json_data = json_data.decode(encoding=encoding)
        decoded_data: Dict = serializer.loads(json_data)
        if not isinstance(decoded_data, Mapping):
            raise TextTranslatorError('Wrong json data: root must be a dict')
        if 'Cengal.TextTranslationDictionary' != decoded_data.get('type'):
            raise TextTranslatorError('Wrong json data: lack of "type" field or a "type" field value mismatch')
        try:
            text_translation_dictionary: TextTranslationDictionary = dict()
            text_translation_list = decoded_data['text_translation_list']
            for item in text_translation_list:
                text_translation_dictionary[item['text']] = item['translations']
            return cls(text_translation_dictionary, decoded_data)
        except (KeyError, TypeError):
            raise TextTranslatorError('Wrong json data or other parsing error')
    
    def __init__(self, dictionary: TextTranslationDictionary, decoded_data: Optional[Dict]=None):
        self.dictionary = dictionary
        self.decoded_data = decoded_data
    
    def __call__(self, language: TranslationLanguageId, text: TranslatableText, entity_id: Optional[TextEntityId]=None) -> TranslatableText:
        try:
            translations = self.dictionary[text]
            if entity_id is None:
                variant = translations['default']
            else:
                variant = translations['variants'][entity_id]
            return variant[language]
        except KeyError:
            return text


class TranslationLanguageMapper:
    def __init__(self, lang_2_lang: TranslationLangToLangMap, default_lang: TranslationLanguageId):
        self.lang_2_lang: TranslationLangToLangMap = lang_2_lang
        self.default_lang: TranslationLanguageId = default_lang
    
    def __call__(self, lang: TranslationLanguageId):
        return self.lang_2_lang.get(lang, None) or self.default_lang


class TranslationLanguageChooser:
    def __init__(self, text_translator: TextTranslator, 
                 translation_language_mapper: TranslationLanguageMapper,
                 coro_scheduler: Optional[CoroScheduler]=None):
        self._end_lang: Optional[TranslationLanguageId] = None
        self._lang: Optional[TranslationLanguageId] = None
        self.text_translator: TextTranslator = text_translator
        self.translation_language_mapper: TranslationLanguageMapper = translation_language_mapper
        self.coro_scheduler: CoroScheduler = coro_scheduler or CoroScheduler.current_loop()
        self.translation_language_changed_event: str = str(uuid4())
    
    @property
    def lang(self) -> TranslationLanguageId:
        return self._lang
    
    @lang.setter
    def lang(self, language: TranslationLanguageId):
        self._lang = language
        self._end_lang = self.translation_language_mapper(self._lang)
        
        # def raise_translation_language_changed_event(
        #     interface: Interface,
        #     translation_language_changed_event: str,
        #     lang: TranslationLanguageId,
        #     end_lang: TranslationLanguageId
        #     ):
        #     with log_uncatched_exception():
        #         print('raise_translation_language_changed_event - raising event...')
        #         print(interface, translation_language_changed_event, lang, end_lang)
        #         interface(Sleep, 1.0)
        #         interface(AsyncEventBus, AsyncEventBusRequest().send_event(translation_language_changed_event, (lang, end_lang), CoroPriority.low))
        #         interface(Sleep, 1.0)
        #         print('raise_translation_language_changed_event - done')
        
        # try_put_coro_to(get_interface_and_loop_with_explicit_loop(self.coro_scheduler), raise_translation_language_changed_event, 
        #         self.translation_language_changed_event, self._lang, self._end_lang)
        try_send_async_event(self.coro_scheduler, self.translation_language_changed_event, (self._lang, self._end_lang), CoroPriority.high)
    
    # @staticmethod
    # def raise_translation_language_changed_event(
    #     interface: Interface,
    #     translation_language_changed_event: str,
    #     lang: TranslationLanguageId,
    #     end_lang: TranslationLanguageId
    #     ):
    #     print('raise_translation_language_changed_event - raising event...')
    #     print(interface, translation_language_changed_event, lang, end_lang)
    #     interface(AsyncEventBus, AsyncEventBusRequest().send_event(translation_language_changed_event, (lang, end_lang), CoroPriority.low))
    #     print('raise_translation_language_changed_event - done')
    
    def set_lang(self, language: TranslationLanguageId) -> 'TranslationLanguageChooser':
        '''
        For usage with ArgsManager like
                am = ArgsManager(
                    EArgs(text_translator=TranslationLanguageChooser(
                        TextTranslator.from_json(TEXT_DICTIONARY), 
                        TranslationLanguageMapper(TRANSLATION_LANGUAGE_MAP, 'en')).set_lang('ru'))
                )

        '''
        self.lang = language
        return self
    
    @property
    def end_lang(self) -> TranslationLanguageId:
        return self._end_lang
    
    @end_lang.setter
    def end_lang(self, language: TranslationLanguageId):
        pass
    
    def __call__(self, text: TranslatableText, entity_id: Optional[TextEntityId]=None) -> TranslatableText:
        return self.text_translator(self._end_lang, text, entity_id)


class TextTranslationReapplier(CallHistoryReapplier):
    class ToBeTranslated:
        def __init__(self):
            self.text: TranslatableText = None
        
        def __call__(self, text: TranslatableText) -> 'TextTranslationReapplier.ToBeTranslated':
            self.text = text
            return self
        
    def __init__(self, text_translator: TranslationLanguageChooser, priority: CoroPriority=CoroPriority.low):
        self.text_translator = text_translator
        super().__init__(priority)
    
    def _translate_needed(self, value: Any, entity_id: Optional[TextEntityId]) -> Any:
        if isinstance(value, TextTranslationReapplier.ToBeTranslated):
            return self.text_translator(value.text, entity_id)
        else:
            return value
    
    def call_impl(self, entity_id: Optional[TextEntityId], obj: Any, field: Hashable, translation_worker: TranslationWorker, text_template: Optional[str], *args, **kwargs):
        new_args = list()
        for arg in args:
            new_args.append(self._translate_needed(arg, entity_id))
        
        new_kwargs = dict()
        for key, value in kwargs.items():
            new_kwargs[key] = self._translate_needed(value, entity_id)
        
        if text_template is None:
            if new_kwargs:
                raise RuntimeError('There are tt items in kwargs, however text_template is None')

            translated_text = ' '.join(new_args)
        else:
            translated_text = text_template.format(*new_args, **new_kwargs)
        
        translation_worker(translated_text)
    
    def args_to_key_value(self, entity_id: Optional[TextEntityId], obj: Any, field: Hashable, translation_worker: Callable, text_template: Optional[str], *args, **kwargs) -> Tuple[Hashable, Any]:
        return ((entity_id, id(obj), field), (translation_worker, text_template, args, kwargs))
    
    def key_value_to_args(self, key: Hashable, value: Any) -> Tuple[Tuple, Dict]:
        entity_id, obj, field = key
        translation_worker, text_template, args, kwargs = value
        new_args = tuple([entity_id, obj, field, translation_worker, text_template] + list(args))
        return new_args, kwargs


def tt(text: TranslatableText) -> 'TextTranslationReapplier.ToBeTranslated':
    return TextTranslationReapplier.ToBeTranslated()(text)
