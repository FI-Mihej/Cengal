#!/bin/bash

ORIGINAL_DIR=$(pwd)
SCRIPT_DIR=$(dirname "$(realpath "${BASH_SOURCE[0]}")")
source $SCRIPT_DIR/_common.sh

# Use a subshell for the operations in the new directory
(
    # Call the setup function from the sourced script
    setup_environment "$1"

    VIRTUAL_ENVIRONMENT_DIR_PATH=$CURRENT_PROJECT_DIR_PATH/venv

    cd $VIRTUAL_ENVIRONMENT_DIR_PATH/bin
    source activate

    cd $CURRENT_PROJECT_DIR_PATH

    requirements_txt=./requirements.txt
    if [ -f "$requirements_txt" ]; then
        python -m pip install --upgrade -r $requirements_txt
    fi

    requirements_py=./__requirements__.py
    if [ -f "$requirements_py" ]; then
        python $requirements_py
    fi
)
