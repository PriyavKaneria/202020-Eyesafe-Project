@echo off

echo cheking for python.

python --version >nul 2>&1

if %errorlevel% neq 0 (
    echo Installing Python...
    
    curl -o python_installer.exe https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe
    python_installer.exe /quiet InstallAllUsers=1 PrependPath=1

    echo deleting unnecessary files.
    del python_installer.exe
) 

echo Python is good to go.

echo installing pywin32.

pip install pywin32

echo installing pyinstaller 
pip install pyinstaller




echo Running PyInstaller on 20-20-20-Eyesafe-project.py...
pyinstaller --onefile 20-20-20-Eyesafe-project.py

cd dist

start 20-20-20-Eyesafe-project.exe
