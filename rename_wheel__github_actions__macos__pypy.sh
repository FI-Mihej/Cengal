#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 PYTHON_VER PLATFORM_TAG"
    exit 1
fi

PYTHON_VER="$1"
PLATFORM_TAG="$2"

# Determine the short Python version string
case "$PYTHON_VER" in
    "pypy-3.8")
        PYTHON_SHORT_VER="pp38"
        ;;
    "pypy-3.9")
        PYTHON_SHORT_VER="pp39"
        ;;
    "pypy-3.10")
        PYTHON_SHORT_VER="pp310"
        ;;
    *)
        echo "Unsupported Python version"
        exit 1
        ;;
esac

# Determine the platform tag string
case "$PLATFORM_TAG" in
    "macos-13")
        PLATFORM_TAG_STR="macosx_13_0_x86_64"
        ;;
    "macos-14")
        PLATFORM_TAG_STR="macosx_14_0_arm64"
        ;;
    *)
        echo "Unsupported platform tag"
        exit 1
        ;;
esac

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
