@echo off
%cd%\venv\Scripts\python.exe %cd%\main.py >> %cd%\Data\ExecutionLogs\Log%random%.txt

shutdown /s /t 300 /c "Shutdown will be executed in 300 seconds!"

:BreakUp
cls
echo Shutdown will be executed in less than 300 seconds!
echo.

set /P break_up=Do you want to break up shutdown[Y/N]?:
if /I %break_up%==Y goto Yes
if /I %break_up%==N goto Exit
goto BreakUp

:Yes
shutdown /a

:Exit
exit