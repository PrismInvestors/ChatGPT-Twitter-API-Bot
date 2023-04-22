:: This is a batch file to run a Python script at random time intervals.
:: To change the random time interval, modify the values of 'min_minutes' and 'max_minutes' accordingly.
:: The 'timeout' command will wait for a random number of minutes between 'min_minutes' and 'max_minutes'.

@echo off
setlocal enabledelayedexpansion
cd main

:: Set the minimum and maximum number of minutes for the random time interval
echo This script will use a random interval of a min and max minutes to tweet out reply tweets to top tweets on your home page. The script will run indefinitely until stopped.
echo.
echo Please, follow the instructions below to set up the time intervals and run the script.
echo.
echo 1. Enter the minimum and maximum number of minutes for the random time interval.
echo 2. The script will start running and use the specified interval to execute the Python script.
echo 3. To stop the script, press CTRL+C in the command prompt window.
echo.
echo ^<WARNING^> The script will run indefinitely until stopped. Make sure to stop the script when you are done using it.
echo _________________________________________
set /p min_minutes=Enter the minimum number of minutes: 
set /p max_minutes=Enter the maximum number of minutes: 

:loop
:: Convert minutes to seconds
set /a min_seconds=min_minutes*60
set /a max_seconds=max_minutes*60

:: Generate a random number between 'min_seconds' and 'max_seconds'
set /a rand_seconds=%min_seconds% + !random! %% (%max_seconds% - %min_seconds% + 1)

:: Run the Python script
python main.py

:: Wait for the random number of seconds
timeout /t !rand_seconds!

goto loop
