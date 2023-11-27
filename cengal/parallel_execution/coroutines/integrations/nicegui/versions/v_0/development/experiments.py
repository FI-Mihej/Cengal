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
__version__ = "4.1.1"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


from cengal.parallel_execution.coroutines.coro_scheduler import Interface, cs_acoro, cs_coro, current_interface, CoroWrapperBase, CoroWrapperGreenlet, CoroID
from cengal.parallel_execution.coroutines.coro_standard_services.loop_yield import (
    CoroPriority, agly, gly)
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.instance import InstanceRequest
from nicegui import app, ui, Client
from cengal.parallel_execution.coroutines.integrations.nicegui import run, apage, apage_class, sl_page, tme, tt, TTE, NTTE, PageContextBase

from nicegui.elements.mixins.text_element import TextElement
from cengal.text_processing.text_translator import TranslationLanguageId, TextEntityId, TextTranslator, TranslationLanguageChooser, TranslationLanguageMapper
from cengal.introspection.inspect import is_callable, is_async
from inspect import isawaitable
from cengal.file_system.path_manager import path_relative_to_src
from typing import Optional, Tuple, Dict, Any, List, Union, Literal, Callable, Hashable, Set
from cengal.parallel_execution.coroutines.coro_standard_services.sleep import Sleep
from cengal.parallel_execution.coroutines.coro_standard_services.put_coro import PutCoro, put_coro
from cengal.parallel_execution.coroutines.coro_standard_services.wait_coro import WaitCoroRequest, CoroutineNotFoundError
from cengal.parallel_execution.coroutines.coro_standard_services.async_event_bus import AsyncEventBusRequest
from random import randint
from nicegui.storage import Storage, request_contextvar
from functools import partial


async def main_coro(i: Interface, app_args_kwargs: Tuple[Tuple, Dict]):
    pass


class HomePage(PageContextBase):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.label: ui.label = None
        self.button: ui.button = None
        self.result: ui.label = None

    def on_clicked(self):
        _t = self._t
        if 'en' == _t.text_translation_language_chooser.lang:
            _t.text_translation_language_chooser.lang = 'uk'
        elif 'uk' == _t.text_translation_language_chooser.lang:
            _t.text_translation_language_chooser.lang = 'ru'
        elif 'ru' == _t.text_translation_language_chooser.lang:
            _t.text_translation_language_chooser.lang = 'en'
        else:
            _t.text_translation_language_chooser.lang = 'en'
        
        ui.notify(tme(f'You clicked me! ', tt('Button clicked'), '. Oh, yes!').tte(_t))
        if self.label is not None:
            _t.set_text(self.label, tme(f'client_id: {self.client.id}; session_id: {self.client.session_id}. ', tt('Tree rendered')))


@ui.page('/', response_timeout=30)
@apage_class(HomePage)
async def home(i: Interface, self: HomePage, _t: NTTE):
    self.label = _t(ui.label(tme(f'{self.client_id=}, {self.session_id=}, {self.user_id=}. ', tt('Tree removed'))))
    ui.link('NiceGUI on GitHub', 'https://github.com/zauberzeug/nicegui')
    self.button = _t(ui.button(tme('Click me! ', tt('Reloading Components Tree'), '. Please!'), on_click=self.on_clicked))

    ui.input(label='Text', placeholder='start typing',
            on_change=lambda e: self.result.set_text('you typed: ' + e.value),
            validation={'Input too long': lambda value: len(value) < 20})
    self.result = ui.label()
    _t(ui.label(tme(tt('Browser view type'), ': ', tt(self.client_view_type.value, formatter=lambda x: x.capitalize()))))
    _t(ui.label(tme(tt('Best lang'), ': ', self.better_lang)))
    _t(ui.label(tme(tt('Featured langs'), ': ', str(self.featured_langs))))
    _t(ui.label(tme(tt('Langs'), ': ', str(self.langs))))


if '__main__' == __name__:
    run(port_or_range=(18000, 18050), app_name_for_fs='nicegui_experiments', reload=False, main_coro=main_coro, storage_secret='THIS_NEEDS_TO_BE_CHANGED')
