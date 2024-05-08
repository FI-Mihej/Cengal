#!/bin/bash

CENGAL_UNITTESTS_DISCOVER_IS_RUNNING="True"
python -m unittest discover -p "test__*.py" -v
