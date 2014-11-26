::::::::::::::::::::::::::::::::::::::::::::::::
::
:: daily.bat
:: Authors: Kyle Sunderland, Aidan Dusseault
:: Last Modified: Oct 30, 2014
::
:: This script automatically runs the system using the test files.
::
:: Output summaries are written in ./output/d"date"t"time" folder.
::
::::::::::::::::::::::::::::::::::::::::::::::::


@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

:: Get the date and time in order to create a unique test directory.
for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "date=%%a"
set "year=%date:~0,4%"
set "month=%date:~4,2%"
set "day=%date:~6,2%"
set "hour=%date:~8,2%"
set "minute=%date:~10,2%"
set "second=%date:~12,2%"

:: Create a unique test directory based on the current date/time.
set "out_dir=./output/d%year%-%month%-%day%_t%hour%-%minute%-%second%"
mkdir "%out_dir%" >NUL

:: Loop into each of the test categories.
for %%t in (create delete deposit general login logout transfer withdraw) do (

	:: Loop through the tests in the current category.
	for %%f in (.\tests\%%t\input\*) do (
	
		:: Run the tests and compare the files.
		python frontend/scripts/main.py .\tests\%%t\accounts\accounts_%%~nf.txt %out_dir%/%%~nf.log < %%f >> nul

	)
)
python frontend/scripts/main.py .\tests\%%t\accounts\accounts_%%~nf.txt %out_dir%/%%~nf.log

