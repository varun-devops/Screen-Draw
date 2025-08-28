@echo off
echo Creating Windows shortcut with hotkey CTRL+ALT+W...
powershell -ExecutionPolicy Bypass -File "%~dp0create_shortcut.ps1"
echo.
echo Shortcut created! You can now use CTRL+ALT+W from anywhere to launch the screen drawing tool.
echo.
pause
