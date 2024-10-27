@echo off
SETLOCAL

SET "ORIGINAL_DIR=%CD%"
SET "SCRIPT_DIR=%~dp0"
SET "SCRIPT_DIR=%SCRIPT_DIR:~0,-1%"
CALL "%SCRIPT_DIR%\_common.cmd" :setup_environment %*

CALL :executeCommands

cd /D "%ORIGINAL_DIR%"
ENDLOCAL
GOTO :EOF

:executeCommands
    SET "VIRTUAL_ENVIRONMENT_DIR_PATH=%CURRENT_PROJECT_DIR_PATH%\venv"

    cd "%VIRTUAL_ENVIRONMENT_DIR_PATH%\Scripts"
    IF NOT ERRORLEVEL 0 GOTO :errorHandler

    CALL .\activate.bat
    IF NOT ERRORLEVEL 0 GOTO :errorHandler

    cd %CURRENT_PROJECT_DIR_PATH%

    set "requirements_txt=requirements.txt"
    if exist "%requirements_txt%" (
        python -m pip install --upgrade -r %requirements_txt%
        IF NOT ERRORLEVEL 0 GOTO :errorHandler
    )

    set "requirements_py=__requirements__.py"
    if exist "%requirements_py%" (
        python %requirements_py%
        IF NOT ERRORLEVEL 0 GOTO :errorHandler
    )

    GOTO :EOF

:errorHandler
    echo An error occurred during execution
    cd /D "%ORIGINAL_DIR%"
    EXIT /B 1
