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

    rmdir /s /q "%VIRTUAL_ENVIRONMENT_DIR_PATH%"
    IF NOT ERRORLEVEL 0 GOTO :errorHandler

    mkdir -p %VIRTUAL_ENVIRONMENT_DIR_PATH%
    IF NOT ERRORLEVEL 0 GOTO :errorHandler

    %PYTHON_INTERPRETER% -m venv %VIRTUAL_ENVIRONMENT_DIR_PATH%
    IF NOT ERRORLEVEL 0 GOTO :errorHandler

    echo SET PYTHONPATH=%CENGAL_ROOT_DIR_PATH%;%%PYTHONPATH%% >> %VIRTUAL_ENVIRONMENT_DIR_PATH%\Scripts\activate.bat

    cd "%VIRTUAL_ENVIRONMENT_DIR_PATH%\Scripts"
    IF NOT ERRORLEVEL 0 GOTO :errorHandler

    CALL .\activate.bat
    IF NOT ERRORLEVEL 0 GOTO :errorHandler

    cd %CURRENT_PROJECT_DIR_PATH%

    SET "requirements_txt=requirements.txt"
    if exist "%requirements_txt%" (
        python -m pip install --upgrade -r %requirements_txt%
        IF NOT ERRORLEVEL 0 GOTO :errorHandler
    )

    SET "requirements_py=__requirements__.py"
    if exist "%requirements_py%" (
        python %requirements_py%
        IF NOT ERRORLEVEL 0 GOTO :errorHandler
    )

    GOTO :EOF

:errorHandler
    echo An error occurred during execution
    cd /D "%ORIGINAL_DIR%"
    EXIT /B 1
