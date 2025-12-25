@echo off
REM Activate Python virtual environment
call venv\Scripts\activate

REM Start Python backend in new window
start python main.py

REM Give backend a few seconds to start
timeout /t 3

REM Start Tauri desktop app
npm run tauri

pause
