#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 PYTHON_VER PLATFORM_TAG"
    exit 1
fi

PYTHON_VER="$1"
PLATFORM_TAG="$2"

# Determine the short Python version string
case "$PYTHON_VER" in
    "3.8")
        PYTHON_SHORT_VER="cp38"
        ;;
    "3.9")
        PYTHON_SHORT_VER="cp39"
        ;;
    "3.10")
        PYTHON_SHORT_VER="cp310"
        ;;
    "3.11")
        PYTHON_SHORT_VER="cp311"
        ;;
    "3.12")
        PYTHON_SHORT_VER="cp312"
        ;;
    "3.13")
        PYTHON_SHORT_VER="cp313"
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

# # # Determine the platform tag string
# # case "$PLATFORM_TAG" in
# #     "macos-13")
# #         PLATFORM_TAG_STR="macosx_13_0_universal2"
# #         ;;
# #     "macos-14")
# #         PLATFORM_TAG_STR="macosx_14_0_universal2"
# #         ;;
# #     *)
# #         echo "Unsupported platform tag"
# #         exit 1
# #         ;;
# # esac

# # Determine the short Python version string
# case "$PYTHON_VER" in
#     "3.8")
#         # Determine the platform tag string
#         case "$PLATFORM_TAG" in
#             "macos-13")
#                 PLATFORM_TAG_STR="macosx_13_0_x86_64"
#                 ;;
#             "macos-14")
#                 PLATFORM_TAG_STR="macosx_14_0_arm64"
#                 ;;
#             *)
#                 echo "Unsupported platform tag"
#                 exit 1
#                 ;;
#         esac
#         ;;
#     "3.9")
#         # Determine the platform tag string
#         case "$PLATFORM_TAG" in
#             "macos-13")
#                 PLATFORM_TAG_STR="macosx_13_0_x86_64"
#                 ;;
#             "macos-14")
#                 PLATFORM_TAG_STR="macosx_14_0_arm64"
#                 ;;
#             *)
#                 echo "Unsupported platform tag"
#                 exit 1
#                 ;;
#         esac
#         ;;
#     "3.10")
#         # Determine the platform tag string
#         case "$PLATFORM_TAG" in
#             "macos-13")
#                 PLATFORM_TAG_STR="macosx_13_0_x86_64"
#                 ;;
#             "macos-14")
#                 PLATFORM_TAG_STR="macosx_14_0_universal2"
#                 ;;
#             *)
#                 echo "Unsupported platform tag"
#                 exit 1
#                 ;;
#         esac
#         ;;
#     "3.11")
#         # Determine the platform tag string
#         case "$PLATFORM_TAG" in
#             "macos-13")
#                 PLATFORM_TAG_STR="macosx_13_0_universal2"
#                 ;;
#             "macos-14")
#                 PLATFORM_TAG_STR="macosx_14_0_universal2"
#                 ;;
#             *)
#                 echo "Unsupported platform tag"
#                 exit 1
#                 ;;
#         esac
#         ;;
#     "3.12")
#         # Determine the platform tag string
#         case "$PLATFORM_TAG" in
#             "macos-13")
#                 PLATFORM_TAG_STR="macosx_13_0_universal2"
#                 ;;
#             "macos-14")
#                 PLATFORM_TAG_STR="macosx_14_0_universal2"
#                 ;;
#             *)
#                 echo "Unsupported platform tag"
#                 exit 1
#                 ;;
#         esac
#         ;;
#     *)
#         echo "Unsupported Python version"
#         exit 1
#         ;;
# esac

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
