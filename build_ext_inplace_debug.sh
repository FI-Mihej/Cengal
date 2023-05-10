#!/bin/bash

python3 -m debugpy --wait-for-client --listen 0.0.0.0:5678 setup.py build_ext --inplace
