#!/bin/bash

setup_environment() {
    SCRIPT_PATH=$(realpath "${BASH_SOURCE[0]}")
    SCRIPT_DIR_PATH=$(dirname "$SCRIPT_PATH")
    COMMAND_DIR_PATH=$SCRIPT_DIR_PATH
    CURRENT_PROJECT_DIR_PATH=$(realpath "$COMMAND_DIR_PATH/..")
    CENGAL_ROOT_DIR_PATH=$(realpath "$CURRENT_PROJECT_DIR_PATH/../../../../../../../..")

    cd "$CENGAL_LIB_DIR_PATH"

    PYTHON_INTERPRETER="python3"

    if [ ! -z "$1" ]; then
        PYTHON_INTERPRETER="$1"
    fi

    export SCRIPT_PATH SCRIPT_DIR_PATH COMMAND_DIR_PATH CENGAL_LIB_DIR_PATH PYTHON_INTERPRETER
}

setup_environment "$@"
