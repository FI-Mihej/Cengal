#!/bin/bash

sudo chown -R $(id -u):$(id -g) .
python3 setup.py sdist --verbose
