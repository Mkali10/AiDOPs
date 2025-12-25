# AiDOPs - AI Development Operations Platform

**AiDOPs** is a GUI-based DevOps AI platform for developers:

- Role-based login: Admin / Supervisor / Guest
- OTP-based forgot password
- Mobile login support
- Dashboard with machine-style dev flow graph
- Reports export
- Settings management
- Modular backend for logs, DB, network, AI explanations

## Installation

1. Install Python 3.11+
2. Install Flask:
pip install -r requirements.txt
3. Run backend:
   python main.py

4. Open `src/gui/index.html` in browser (or integrate with Tauri for desktop)

## Project Structure

See the folder hierarchy in the source for GUI, core modules, and data storage.

Python Backend Integration (Flask) Desktop app launch


> npm run start-backend
&
> npm run tauri



Windows: double-click start_app.bat

and For Linux "give the permission first" chmod +x start_app.sh

Mac/Linux: terminal me ./start_app.sh

