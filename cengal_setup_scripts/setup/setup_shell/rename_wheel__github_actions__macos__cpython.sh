#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 PYTHON_VER PLATFORM_TAG"
    exit 1
fi

declare -A PYTHON_SHORT_VERSIONS
PYTHON_SHORT_VERSIONS["3.10"]="cp310"
PYTHON_SHORT_VERSIONS["3.11"]="cp311"
PYTHON_SHORT_VERSIONS["3.12"]="cp312"
PYTHON_SHORT_VERSIONS["3.8"]="cp38"
PYTHON_SHORT_VERSIONS["3.9"]="cp39"

declare -A PLATFORM_TAG_VERSIONS
PLATFORM_TAG_VERSIONS["macos-13"]="macosx_13_0_universal2"
PLATFORM_TAG_VERSIONS["macos-14"]="macosx_14_0_universal2"

PYTHON_VER="$1"
PYTHON_SHORT_VER=${PYTHON_SHORT_VERSIONS[$PYTHON_VER]}
PLATFORM_TAG="$2"
PLATFORM_TAG_STR=${PLATFORM_TAG_VERSIONS[$PLATFORM_TAG]}

WHEELHOUSE_DIR="wheelhouse_temp"

shopt -s nullglob
for file in "$WHEELHOUSE_DIR"/cengal-*-py3-none-any.whl; do
    if [ -f "$file" ]; then
        version=$(echo "$file" | sed 's|.*/cengal-\(.*\)-py3-none-any.whl|\1|')
        new_filename="$WHEELHOUSE_DIR/cengal-${version}-${PYTHON_SHORT_VER}-none-${PLATFORM_TAG_STR}.whl"

        echo "Renaming $file to $new_filename"
        mv "$file" "$new_filename"
    fi
done
shopt -u nullglob
