#!/bin/sh

sudo pip3 install paver  # needed for python-lzf module installation process
sudo pip3 install urllib3
sudo pip3 install thrift
sudo pip3 install thriftpy
sudo pip3 install tornado
sudo pip3 install requests
sudo pip3 install simplejson
sudo pip3 install pyOpenSSL
sudo pip3 install pycurl
sudo pip3 install pycrypto
sudo pip3 install pyasn1
sudo pip3 install lzmaffi  # for pypy3 and Python2 only: it is backport from python34 which is default in Ubuntu 14.04
sudo pip3 install Jinja2
sudo pip3 install http-parser
sudo pip3 install html5lib
sudo pip3 install greenlet
sudo pip3 install enum34  # for pypy3 and Python2 only: it is backport from python34 which is default in Ubuntu 14.04
sudo pip3 install Cython
sudo pip3 install cryptography

sudo pip3 install audioread
sudo pip3 install beautifulsoup4
sudo pip3 install cchardet
sudo pip3 install cookies
sudo pip3 install decorator
sudo pip3 install httpagentparser
sudo pip3 install line-profiler  # for CPython only! (as far as I know)
sudo pip3 install pyaudio
sudo pip3 install pygeoip
sudo pip3 install pylast
sudo pip3 install python-mimeparse


cd ./InstallSourcess/Python3/common-mimetypes
sudo pip3 install ./common-mimetypes-0.1rc1-Python3.zip
cd ../../..

cd ./InstallSourcess/Python3/progress
sudo pip3 install ./progress-crossplatform.zip
cd ../../..

cd ./InstallSourcess/Python3/python-lzf
sudo pip3 install ./python-lzf-master-python3.zip
cd ../../..