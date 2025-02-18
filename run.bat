@echo off
setlocal

rem Get all command line arguments after the file name
set args=%*

rem Activate the virtual environment
call %~dp0\venv\Scripts\activate

rem Run src\main.py with command line arguments
python %~dp0\src\main.py %args%

endlocal