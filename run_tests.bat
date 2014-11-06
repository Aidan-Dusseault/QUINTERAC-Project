::::::::::::::::::::::::::::::::::::::::::::::::
::
:: run_tests.bat
:: Authors: Kyle Sunderland, Aidan Dusseault
:: Last Modified: Oct 30, 2014
::
:: This script automatically runs and tests the frontend system
:: using files contained in the ./tests/ folder.
::
:: Tests summaries are written in ./results/d"date"t"time" folder
:: organized by tests subject.
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
set "out_dir=./results/d%year%-%month%-%day%_t%hour%-%minute%-%second%"
mkdir "%out_dir%" >NUL

echo Running Tests...
echo Test ID: d%year%-%month%-%day%_t%hour%-%minute%-%second%

:: Write to the summary file.
echo ________________
echo Test Log >>%out_dir%/test_log.log
echo Test ID: d%year%-%month%-%day%_t%hour%-%minute%-%second% >>%out_dir%/test_log.log
echo ______________________ >>%out_dir%/test_log.log
echo Failed Tests: >>%out_dir%/test_log.log
echo ------------- >>%out_dir%/test_log.log

set /a numberTests=0
set /a failures=0
:: Loop into each of the test categories.
for %%t in (create delete deposit general login logout transfer withdraw) do (

	:: Create the current categories file structure.
	mkdir "%out_dir%/%%t" >NUL
	mkdir "%out_dir%/%%t/summary" >NUL
	mkdir "%out_dir%/%%t/output" >NUL
	mkdir "%out_dir%/%%t/logs" >NUL

	:: Loop through the tests in the current category.
	for %%f in (.\tests\%%t\input\*) do (
	
		:: Run the tests and compare the files.
		echo Running: %%~nf
		python frontend/scripts/main.py .\tests\%%t\accounts\accounts_%%~nf.txt %out_dir%/%%t/summary/summary_%%~nf.log < %%f >> %out_dir%/%%t/output/output_%%~nf.log
		python fileCompare.py %%~nf %out_dir%
		if errorlevel 1 set /a failures=!failures!+1
		set /a numberTests=!numberTests!+1

	)
)
if !failures! == 0 echo None >>%out_dir%/test_log.log

echo ______________________ >>%out_dir%/test_log.log
echo Number of tests run: !numberTests!>>%out_dir%/test_log.log
echo Number of tests failed: !failures!>>%out_dir%/test_log.log

echo ________________
echo Tests Complete
