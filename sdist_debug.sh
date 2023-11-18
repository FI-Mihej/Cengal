#!/bin/bash

sudo chown -R $(id -u):$(id -g) .
python3 -m debugpy --wait-for-client --listen 0.0.0.0:5678 setup.py sdist
