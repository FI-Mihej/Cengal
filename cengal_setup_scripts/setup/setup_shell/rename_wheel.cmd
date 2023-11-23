@echo off
setlocal EnableDelayedExpansion

rem Define the directory where the wheels are located
set "WHEELHOUSE_DIR=.\dist"

rem Check for Python version argument
if "%~1"=="" (
    echo Usage: %0 WHEEL_TAG
    exit /b 1
)
set "WHEEL_TAG=%~1"

pushd %WHEELHOUSE_DIR%
for %%f in (cengal-*-py3-none-any.whl) do (
    if exist "%%f" (
        for /f "tokens=2 delims=-" %%v in ("%%f") do (
            set "version=%%v"
        )
        set "new_filename=cengal-!version!-%WHEEL_TAG%-none-win_amd64.whl"
        echo Renaming %%f to !new_filename!
        ren "%%f" "!new_filename!"
    )
)
popd

endlocal
