python3 .\cengal_setup_scripts\remove_pycache\remove_pycache.py
del /Q .coverage

SET CENGAL_UNITTESTS_DISCOVER_IS_RUNNING="True"
python -m coverage run -m unittest discover -p "test__*.py" -v
