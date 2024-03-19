#!/bin/bash

python3 -m cython remote_objects.py -o remote_objects_compiled.c
gcc -shared -fPIC -Os -I /usr/include/python3.8 -o remote_objects_compiled.so remote_objects_compiled.c -lpython3.8 -lpthread -lm -lutil -ldl
