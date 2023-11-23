#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 PYTHON_VER PLATFORM_TAG"
    exit 1
fi

PYTHON_VER="$1"
PLATFORM_TAG="$2"

WHEELHOUSE_DIR="wheelhouse"

shopt -s nullglob
for file in "$WHEELHOUSE_DIR"/cengal-*-py3-none-any.whl; do
    if [ -f "$file" ]; then
        version=$(echo "$file" | sed 's|.*/cengal-\(.*\)-py3-none-any.whl|\1|')
        new_filename="$WHEELHOUSE_DIR/cengal-${version}-${PYTHON_VER}-none-${PLATFORM_TAG}.whl"

        echo "Renaming $file to $new_filename"
        mv "$file" "$new_filename"
    fi
done
shopt -u nullglob
