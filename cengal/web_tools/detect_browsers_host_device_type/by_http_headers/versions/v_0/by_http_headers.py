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


__all__ = ['UAProf', 'is_wap_browser', 'BrowserViewState', 'browser_view_state', 'ClientDevicePlatform', 
           'client_device_platform', 'client_device_platform_version', 'client_device_model', 'client_device_arch', 
           'MobileDeviceType', 'mobile_device_type_by_user_agent', 'ClientDeviceType', 'client_device_type', 
           'ClientViewType', 'client_view_type']


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


from enum import Enum, IntEnum
from typing import Mapping, Optional
from cengal.web_tools.detect_browsers_host_device_type.by_http_user_agent import is_mobile_or_tablet_browser


UAProf = {
    'x-wap-profile'.casefold(),
    '19-Profile'.casefold(),
    'WAP-Profile'.casefold(),
}


def is_wap_browser(headers: Mapping) -> bool:
    return bool(UAProf.intersection(headers.keys()))


class BrowserViewState(str, Enum):
    desktop = '?0'
    mobile = '?1'
    unknown = 'unknown'


def browser_view_state(headers: Mapping) -> BrowserViewState:
    return BrowserViewState(headers.get('Sec-CH-UA-Mobile'.casefold(), 'unknown'))


class ClientDevicePlatform(str, Enum):
    unknown = 'unknown'
    windows = 'Windows'
    macos = 'macOS'
    linux = 'Linux'
    ios = 'iOS'
    chromiumos = 'Chromium OS'
    chromeos = 'Chrome OS'
    android = 'Android'


def client_device_platform(headers: Mapping) -> ClientDevicePlatform:
    return ClientDevicePlatform(headers.get('Sec-CH-UA-Platform'.casefold(), 'unknown'))


def client_device_platform_version(headers: Mapping) -> Optional[str]:
    return headers.get('Sec-CH-UA-Platform-Version'.casefold(), None)


def client_device_model(headers: Mapping) -> Optional[str]:
    return headers.get('Sec-CH-UA-Model'.casefold(), None)


def client_device_arch(headers: Mapping) -> Optional[str]:
    return headers.get('Sec-CH-UA-Arch'.casefold(), None)


class MobileDeviceType(str, Enum):
    unknown = 'unknown'
    mobile = 'mobile'
    tablet = 'tablet'


def mobile_device_type_by_user_agent(headers: Mapping) -> MobileDeviceType:
    mobile, tablet = is_mobile_or_tablet_browser(headers.get('User-Agent'.casefold(), ''))
    if tablet:
        return MobileDeviceType.tablet
    elif mobile:
        return MobileDeviceType.mobile
    else:
        return MobileDeviceType.unknown


class ClientDeviceType(str, Enum):
    desktop = 'desktop'
    laptop = 'laptop'
    tablet = 'tablet'
    mobile = 'mobile'


def client_device_type(headers: Mapping) -> ClientDeviceType:
    if is_wap_browser(headers):
        return ClientDeviceType.mobile
    else:
        cdp: ClientDevicePlatform = client_device_platform(headers)
        if ClientDevicePlatform.unknown == cdp:
            mdt: MobileDeviceType = mobile_device_type_by_user_agent(headers)
            if MobileDeviceType.tablet == mdt:
                return ClientDeviceType.tablet
            elif MobileDeviceType.mobile == mdt:
                return ClientDeviceType.mobile
            else:
                return ClientDeviceType.desktop
        elif cdp in {ClientDevicePlatform.ios, ClientDevicePlatform.android}:
            mdt: MobileDeviceType = mobile_device_type_by_user_agent(headers)
            if MobileDeviceType.tablet == mdt:
                return ClientDeviceType.tablet
            else:
                return ClientDeviceType.mobile
        else:
            return ClientDeviceType.desktop


class ClientViewType(str, Enum):
    desktop = 'desktop'
    laptop = 'laptop'
    tablet = 'tablet'
    mobile = 'mobile'


def client_view_type(headers: Mapping) -> ClientViewType:
    bvs: BrowserViewState = browser_view_state(headers)
    if BrowserViewState.desktop == bvs:
        return ClientViewType.desktop
    elif BrowserViewState.mobile == bvs:
        mdt: MobileDeviceType = mobile_device_type_by_user_agent(headers)
        if MobileDeviceType.tablet == mdt:
            return ClientViewType.tablet
        else:
            return ClientViewType.mobile
    elif BrowserViewState.unknown == bvs:
        if is_wap_browser(headers):
            return ClientDeviceType.mobile
        else:
            mdt: MobileDeviceType = mobile_device_type_by_user_agent(headers)
            if MobileDeviceType.tablet == mdt:
                return ClientViewType.tablet
            elif MobileDeviceType.mobile == mdt:
                return ClientViewType.mobile
            else:
                return ClientViewType.desktop
    else:
        raise ValueError(f'Unknown BrowserViewState: {bvs}')
