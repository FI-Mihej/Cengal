#!/bin/bash

CENGAL_UNITTESTS_DISCOVER_IS_RUNNING="True"
python3 -m unittest discover -p "test__*.py" -v
