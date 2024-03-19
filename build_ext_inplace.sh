#!/bin/bash

# sudo chown -R $(id -u):$(id -g) .
python3 setup.py build_ext --inplace
