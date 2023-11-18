#!/bin/bash

# https://stackoverflow.com/questions/30306099/pip-install-editable-vs-python-setup-py-develop
# https://www.reddit.com/r/learnpython/comments/ayx7za/how_does_pip_install_e_work_is_there_a_specific/
# https://stackoverflow.com/questions/42609943/what-is-the-use-case-for-pip-install-e
# https://stackoverflow.com/questions/20339183/difference-between-setup-py-install-and-setup-py-develop

# https://packaging.python.org/specifications/recording-installed-packages/

python3 -m pip uninstall cengal
rm -rf ./cengal.egg-info
# https://setuptools.pypa.io/en/latest/userguide/development_mode.html#limitations
# python3 -m pip install -e .
python3 -m pip install --upgrade pip
python3 -m pip install --upgrade setuptools

export CENGAL_BUILD_IS_IN_DEBUG_MODE=True
# python3 -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m pip install -e . --config-settings editable_mode=compat
python3 -m debugpy --wait-for-client --listen 0.0.0.0:5678 -m pip install -e .[hardware__info__cpu__versions__v_1] --config-settings editable_mode=compat
# python3 -m pip install -e .[hardware__info__cpu__versions__v_1] --config-settings editable_mode=compat
