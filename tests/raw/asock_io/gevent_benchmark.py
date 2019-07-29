# import gevent
# from gevent import socket as gsock
import socket as sock
from multiprocessing import Pool
from threading import Thread
from datetime import datetime


"""
Module Docstring
Docstrings: http://www.python.org/dev/peps/pep-0257/
"""

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