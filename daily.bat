::::::::::::::::::::::::::::::::::::::::::::::::
::
:: daily.bat
:: Authors: Kyle Sunderland, Aidan Dusseault
:: Last Modified: Oct 30, 2014
::
:: This script automatically runs the system using the specified files.
::
:: Output summaries are written in the specified folder.
::
::::::::::::::::::::::::::::::::::::::::::::::::

@echo off
SETLOCAL ENABLEDELAYEDEXPANSION

if not exist %2 mkdir "%2" >NUL
if not exist %2/summary mkdir "%2/summary" >NUL

if not exist %2/master_accounts.log type NUL >%2/master_accounts.log
if not exist %2/valid_accounts.log  type NUL >%2/valid_accounts.log 

:: Loop through the tests in the current category.
for %%f in (%1/*) do (

	python ./frontend/scripts/main.py %2/valid_accounts.log %2/summary/%%~nf.log < %1/%%f

)

python fileMerge.py %2/summary %2/merged_summary.log

python ./backend/scripts/main.py %2/master_accounts.log %2/merged_summary.log %2/master_accounts.log %2/valid_accounts.log 