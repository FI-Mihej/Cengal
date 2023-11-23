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


from cengal.parallel_execution.coroutines.coro_scheduler import Interface, current_interface, CoroID
from nicegui.elements.mixins.text_element import TextElement
from nicegui.elements.select import Select
from nicegui.elements.tabs import Tab
from cengal.text_processing.text_translator import TranslationLanguageId, TextEntityId, TextTranslator, TranslationLanguageChooser, \
    TranslationLanguageMapper, TranslatableText, tt, TranslateMe, TMe, tme, TranslatableTextElement, TTE
from cengal.introspection.inspect import is_callable
from cengal.file_system.path_manager import path_relative_to_src
from typing import Optional, Tuple, Dict, Any, List, Union, Callable, Hashable, Set
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro, put_coro
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoroRequest, CoroutineNotFoundError
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest
from cengal.text_processing.text_translator.versions.v_1.text_translator import TranslationLanguageChooser


class NiceguiTranslatableTextElement(TranslatableTextElement[TextElement]):
    def __init__(self, text_translation_language_chooser: TranslationLanguageChooser) -> None:
        super().__init__(text_translation_language_chooser)
    
    def __call__(self, text_element: TextElement) -> TextElement:
        if text_element is None:
            return None
        
        if isinstance(text_element, TextElement):
            if isinstance(text_element.text, TranslateMe):
                if text_element.text:
                    self.elements_and_their_translatable_text[text_element] = text_element.text
                
                text_element.text = text_element.text.to_str(self.text_translator, self.text_translation_language_chooser.end_lang)
        elif isinstance(text_element, Select):
            if 'label' in text_element._props:
                text: TranslateMe = text_element._props['label']
                if isinstance(text, TranslateMe):
                    if text:
                        self.elements_and_their_translatable_text[text_element] = text
                    
                    text_element._props['label'] = text.to_str(self.text_translator, self.text_translation_language_chooser.end_lang)
        elif isinstance(text_element, Tab):
            text: TranslateMe = text_element._props['label']
            if isinstance(text, TranslateMe):
                if text:
                    self.elements_and_their_translatable_text[text_element] = text
                
                text_element._props['label'] = text.to_str(self.text_translator, self.text_translation_language_chooser.end_lang)
        
        return text_element

    def set_text(self, text_element: TextElement, text: Union[TranslateMe, str]) -> TextElement:
        if text_element is None:
            return None
        
        need_to_remove = False
        if isinstance(text, TranslateMe):
            if text:
                self.elements_and_their_translatable_text[text_element] = text
                text_element.text = text.to_str(self.text_translator, self.text_translation_language_chooser.end_lang)
            else:
                need_to_remove = True
        else:
            need_to_remove = True
        
        if need_to_remove:
            del self.elements_and_their_translatable_text[text_element]
            text_element.text = text
        
        return text_element


NTTE = NiceguiTranslatableTextElement


def setup_translation(text_dictionary_path: str):
    # with open(path_relative_to_src('./text_dictionary.json'), 'rb') as f:
    with open(text_dictionary_path, 'rb') as f:
        text_dictionary_data = f.read()

    text_translator: TextTranslator = TextTranslator.from_json(text_dictionary_data)
    translation_language_mapper: TranslationLanguageMapper = TranslationLanguageMapper(text_translator.decoded_data['translation_language_map'],
                                                                                    text_translator.decoded_data['default_language'])
    return text_translator, translation_language_mapper


def create_translatable_text_element(text_translator, translation_language_mapper):
    translation_language_chooser: TranslationLanguageChooser = TranslationLanguageChooser(text_translator, translation_language_mapper)
    # translation_language_chooser.lang = text_translator.decoded_data['original_text_language']
    return NiceguiTranslatableTextElement(translation_language_chooser)


async def acreate_translatable_text_element(text_translator, translation_language_mapper):
    translation_language_chooser: TranslationLanguageChooser = TranslationLanguageChooser(text_translator, translation_language_mapper)
    # translation_language_chooser.lang = text_translator.decoded_data['original_text_language']

    translatable_text_element = NiceguiTranslatableTextElement(translation_language_chooser)
    await translatable_text_element.aregister_on_lang_changed_handler()
    return translatable_text_element
