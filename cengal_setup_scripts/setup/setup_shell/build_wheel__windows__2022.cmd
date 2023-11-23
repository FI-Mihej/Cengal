@echo off
setlocal enabledelayedexpansion

set PACKAGE_NAME=cengal

set VS2022_PYTHONS=Python311 Python312

rem Define Python version to wheel tag mapping
set "tag_Python311=cp311"
set "tag_Python312=cp312"

if exist "C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat" (
    set "VS2022_PATH=C:\Program Files\Microsoft Visual Studio\2022\Community\VC\Auxiliary\Build\vcvars64.bat"
) else (
    echo Visual Studio 2022 not found.
    exit /b 1
)

rmdir /s /q  .\build
rmdir /s /q  .\dist
rmdir /s /q  .\sdist
rmdir /s /q  .\wheel
rmdir /s /q  .\wheelhouse

for %%P in (%VS2022_PYTHONS%) do call :build_wheels %%P "%VS2022_PATH%"

echo Wheels built successfully.

echo Uploading wheels to PyPI...
"%DevCompilers%\Python311\python.exe" -m pip install --upgrade pip
"%DevCompilers%\Python311\python.exe" -m pip install --upgrade setuptools
"%DevCompilers%\Python311\python.exe" -m pip install twine
"%DevCompilers%\Python311\python.exe" -m twine upload --repository pypi dist\%PACKAGE_NAME%-*.whl

echo Upload complete.
endlocal

EXIT /B %ERRORLEVEL%

:: Functions

rem Function to build wheels
:build_wheels
set "PYTHON_DIR=%DevCompilers%\%~1"
set "VSVARS_PATH=%~2"

set "WHEEL_TAG=!tag_%~1!"

"%PYTHON_DIR%\python.exe" -m pip install --upgrade pip
"%PYTHON_DIR%\python.exe" -m pip install --upgrade setuptools
"%PYTHON_DIR%\python.exe" -m pip install -r .\requirements.txt
"%PYTHON_DIR%\python.exe" -m pip wheel . -w dist

call rename_wheel.cmd !WHEEL_TAG!

goto :eof
