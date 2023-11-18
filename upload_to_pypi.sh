#!/bin/bash

sudo chown -R $(id -u):$(id -g) .
python3 setup.py sdist
python3 -m twine upload dist/*
