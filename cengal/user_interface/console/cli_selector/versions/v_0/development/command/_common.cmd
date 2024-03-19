@echo off
SETLOCAL

:setup_environment
    SET "SCRIPT_PATH=%~f0"
    SET "SCRIPT_DIR_PATH=%~dp0"

    REM Removing the trailing backslash for consistency in path
    SET "SCRIPT_DIR_PATH=%SCRIPT_DIR_PATH:~0,-1%"
    SET "COMMAND_DIR_PATH=%SCRIPT_DIR_PATH%"

    REM Normalizing the path to the current project directory
    FOR /f "tokens=*" %%i IN ('cd /D "%COMMAND_DIR_PATH%\.." ^&^& cd') DO SET "CURRENT_PROJECT_DIR_PATH=%%i"

    REM Normalizing the path to the internal Python library root directory
    FOR /f "tokens=*" %%i IN ('cd /D "%CURRENT_PROJECT_DIR_PATH%\..\..\..\..\..\..\.." ^&^& cd') DO SET "CENGAL_ROOT_DIR_PATH=%%i"
    
    SET "PYTHON_INTERPRETER=python3"
    IF NOT "%~1"=="" SET "PYTHON_INTERPRETER=%~1"

    REM Make the variables available outside of the script
    ENDLOCAL & SET "SCRIPT_PATH=%SCRIPT_PATH%" & SET "SCRIPT_DIR_PATH=%SCRIPT_DIR_PATH%" & SET "COMMAND_DIR_PATH=%COMMAND_DIR_PATH%" & SET "CURRENT_PROJECT_DIR_PATH=%CURRENT_PROJECT_DIR_PATH%" & SET "CENGAL_ROOT_DIR_PATH=%CENGAL_ROOT_DIR_PATH%" & SET "PYTHON_INTERPRETER=%PYTHON_INTERPRETER%"

    GOTO :EOF
