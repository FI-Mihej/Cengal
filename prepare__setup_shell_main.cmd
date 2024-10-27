@echo off
xcopy /E /Y ".\cengal_setup_scripts\setup\setup_shell_main\*" ".\"

set PYTHONPATH=%PYTHONPATH%;%CD%
python .\readme_update.py
del .\readme_update.py
