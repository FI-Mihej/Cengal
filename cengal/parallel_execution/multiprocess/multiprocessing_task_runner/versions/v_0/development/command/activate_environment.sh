#!/bin/bash

ORIGINAL_DIR=$(pwd)
SCRIPT_DIR=$(dirname "$(realpath "${BASH_SOURCE[0]}")")
source $SCRIPT_DIR/_common.sh

# Call the setup function from the sourced script
setup_environment "$1"

VIRTUAL_ENVIRONMENT_DIR_PATH=$CURRENT_PROJECT_DIR_PATH/venv

cd $VIRTUAL_ENVIRONMENT_DIR_PATH/bin
source activate

cd $CURRENT_PROJECT_DIR_PATH
