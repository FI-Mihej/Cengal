#!/bin/bash

python3 ./cengal_setup_scripts/remove_pycache/remove_pycache.py
rm -f ./.coverage

CENGAL_UNITTESTS_DISCOVER_IS_RUNNING="True"
python3 -m coverage run -m unittest discover -p "test__*.py" -v
