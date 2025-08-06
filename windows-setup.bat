@echo off
echo ========================================
echo 🚀 RDP TUNNEL SETUP - Windows
echo ========================================

echo 🔧 Enabling Remote Desktop...
reg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f

echo 🔥 Configuring Windows Firewall...
netsh advfirewall firewall set rule group="Remote Desktop" new enable=yes

echo 👤 Creating RDP User...
net user rdpuser MyStrong123! /add
net localgroup "Remote Desktop Users" rdpuser /add
net localgroup "Users" rdpuser /add

echo 🌐 Downloading tunnel client...
powershell -Command "Invoke-WebRequest -Uri 'https://github.com/ekzhang/bore/releases/latest/download/bore-v0.5.0-x86_64-pc-windows-msvc.zip' -OutFile 'bore.zip'"

echo 📦 Extracting tunnel client...
powershell -Command "Expand-Archive -Path 'bore.zip' -DestinationPath '.'"

echo ✅ Setup completed!
echo ========================================
echo 🎯 READY TO CREATE TUNNEL!
echo ========================================
echo.
echo To start tunnel, run:
echo bore.exe local 3389 --to bore.pub
echo.
echo RDP Credentials:
echo Username: rdpuser
echo Password: MyStrong123!
echo.
echo Press any key to start tunnel now...
pause > nul

echo 🚀 Starting tunnel...
bore.exe local 3389 --to bore.pub
