@echo off

for /f "tokens=2 delims==" %%a in ('wmic OS Get localdatetime /value') do set "dt=%%a"
set "YY=%dt:~2,2%" & set "YYYY=%dt:~0,4%" & set "MM=%dt:~4,2%" & set "DD=%dt:~6,2%"
set "HH=%dt:~8,2%" & set "Min=%dt:~10,2%" & set "Sec=%dt:~12,2%"

set "out_dir=./results/d%YYYY%-%MM%-%DD%_t%HH%-%Min%-%Sec%"

mkdir "%out_dir%" >NUL

echo Running Tests...
echo Test ID: d%YYYY%-%MM%-%DD%_t%HH%-%Min%-%Sec%
echo ________________

echo ________________ >>%out_dir%/test_log.log
echo Test Log >>%out_dir%/test_log.log
echo Test ID: d%YYYY%-%MM%-%DD%_t%HH%-%Min%-%Sec% >>%out_dir%/test_log.log
echo ________________ >>%out_dir%/test_log.log
echo Failed Tests: >>%out_dir%/test_log.log
echo ________________ >>%out_dir%/test_log.log

for %%t in (create delete deposit general login logout transfer withdraw) do (

	mkdir "%out_dir%/%%t" >NUL
	mkdir "%out_dir%/%%t/summary" >NUL
	mkdir "%out_dir%/%%t/output" >NUL
	mkdir "%out_dir%/%%t/logs" >NUL

	for %%f in (.\tests\%%t\input\*) do (
		echo Running: %%~nf
		python frontend/scripts/main.py .\tests\%%t\accounts\accounts_%%~nf.txt %out_dir%/%%t/summary/summary_%%~nf.log < %%f >> %out_dir%/%%t/output/output_%%~nf.log
		python fileCompare.py %%~nf %out_dir%
		
	)
)

echo ________________
echo Tests Complete