#!/usr/bin/env python
# coding=utf-8

# Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>
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
__copyright__ = "Copyright © 2012-2023 ButenkoMS. All rights reserved. Contacts: <gtalk@butenkoms.space>"
__credits__ = ["ButenkoMS <gtalk@butenkoms.space>", ]
__license__ = "Apache License, Version 2.0"
__version__ = "3.1.12"
__maintainer__ = "ButenkoMS <gtalk@butenkoms.space>"
__email__ = "gtalk@butenkoms.space"
# __status__ = "Prototype"
__status__ = "Development"
# __status__ = "Production"


# import gevent
# from gevent import socket as gsock
import socket as sock
from multiprocessing import Pool
from threading import Thread
from datetime import datetime




__author__ = 'ButenkoMS <gtalk@butenkoms.space>'


class IpGetter(Thread):
    def __init__(self, domain):
        Thread.__init__(self)
        self.domain = domain

    def run(self):
        self.ip = sock.gethostbyname(self.domain)


if __name__ == "__main__":
    URLS = ['www.google.com', 'www.example.com', 'www.python.org', 'www.yahoo.com', 'www.ubc.ca', 'www.wikipedia.org']
    # t1 = datetime.now()
    # jobs = [gevent.spawn(gsock.gethostbyname, url) for url in URLS]
    # gevent.joinall(jobs, timeout=2)
    # t2 = datetime.now()
    # print("Using gevent it took: %s" % (t2-t1).total_seconds())
    print("-----------")
    t1 = datetime.now()
    pool = Pool(len(URLS))
    results = pool.map(sock.gethostbyname, URLS)
    t2 = datetime.now()
    pool.close()
    print("Using multiprocessing it took: %s" % (t2-t1).total_seconds())
    print("-----------")
    t1 = datetime.now()
    threads = []
    for url in URLS:
        t = IpGetter(url)
        t.start()
        threads.append(t)
    for t in threads:
        t.join()
    t2 = datetime.now()
    print("Using multi-threading it took: %s" % (t2-t1).total_seconds())