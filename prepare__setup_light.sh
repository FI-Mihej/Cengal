#!/bin/bash

cp -R ./cengal_setup_scripts/setup/setup_light/* .

export PYTHONPATH="${PYTHONPATH}:$(pwd)"
python3 ./readme_update.py
rm ./readme_update.py
