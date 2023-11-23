#!/bin/bash

cp -R ./cengal_setup_scripts/setup/setup_shell_main/* .

mkdir -p ./setup_shell_main_sdist
cp -R ./cengal_setup_scripts/setup/setup_shell_main/* ./setup_shell_main_sdist
cp -fr ./LICENSE.md ./setup_shell_main_sdist/LICENSE.md
cp -fr ./NOTICE ./setup_shell_main_sdist/NOTICE
cp -fr ./README.md ./setup_shell_main_sdist/README.md
cp -fr ./THIRD_PARTY_LICENSES.md ./setup_shell_main_sdist/THIRD_PARTY_LICENSES.md
cp -fr ./upload_to_pypi.sh ./setup_shell_main_sdist/upload_to_pypi.sh
cp -fr ./upload_to_testpypi.sh ./setup_shell_main_sdist/upload_to_testpypi.sh
mkdir -p ./setup_shell_main_sdist/cengal_shell
cp -R ./cengal_shell/* ./setup_shell_main_sdist/cengal_shell
