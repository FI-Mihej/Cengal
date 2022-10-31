python -m pip uninstall cengal
rmdir /s /q  .\cengal.egg-info
@REM python -m pip install -e .
@REM https://setuptools.pypa.io/en/latest/userguide/development_mode.html#limitations
python -m pip install --upgrade pip
python -m pip install --upgrade setuptools
python -m pip install -e . --config-settings editable_mode=compat
