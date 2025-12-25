#!/bin/bash

# Activate Python virtual environment
source venv/bin/activate

# Start Python backend in background
python main.py &

# Give backend a few seconds to start
sleep 3

# Start Tauri desktop app
npm run tauri
