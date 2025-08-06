#!/usr/bin/env python3
"""
RDP Tunnel Client - Perfect ngrok Alternative
Run this on your Windows PC to create RDP tunnel
"""

import os
import sys
import subprocess
import platform
import urllib.request
import zipfile
import time

class RDPTunnel:
    def __init__(self):
        self.system = platform.system().lower()
        self.tunnel_methods = {
            '1': self.setup_bore,
            '2': self.setup_playit,
            '3': self.setup_localtunnel,
            '4': self.setup_serveo
        }
    
    def print_banner(self):
        print("=" * 50)
        print("🚀 RDP TUNNEL CLIENT - ngrok Alternative")
        print("=" * 50)
        print("Choose your tunnel method:")
        print("1. Bore.pub (Recommended - Fastest)")
        print("2. PlayIt.gg (Most reliable)")
        print("3. LocalTunnel (Simple)")
        print("4. Serveo.net (SSH-based)")
        print("=" * 50)
    
    def setup_bore(self):
        print("🔧 Setting up Bore tunnel...")
        
        if self.system == 'windows':
            # Download bore for Windows
            url = "https://github.com/ekzhang/bore/releases/latest/download/bore-v0.5.0-x86_64-pc-windows-msvc.zip"
            print("📥 Downloading Bore...")
            urllib.request.urlretrieve(url, "bore.zip")
            
            with zipfile.ZipFile("bore.zip", 'r') as zip_ref:
                zip_ref.extractall(".")
            
            print("✅ Bore installed!")
            print("🚀 Starting tunnel...")
            
            # Start bore tunnel
            cmd = "bore.exe local 3389 --to bore.pub"
            print(f"Running: {cmd}")
            subprocess.run(cmd, shell=True)
        
        else:
            # Linux/Mac
            os.system("curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh -s -- -y")
            os.system("source ~/.cargo/env && cargo install bore-cli")
            os.system("~/.cargo/bin/bore local 3389 --to bore.pub")
    
    def setup_playit(self):
        print("🔧 Setting up PlayIt tunnel...")
        
        if self.system == 'windows':
            url = "https://github.com/playit-cloud/playit-agent/releases/latest/download/playit-windows_64.exe"
            print("📥 Downloading PlayIt...")
            urllib.request.urlretrieve(url, "playit.exe")
            
            print("✅ PlayIt installed!")
            print("🚀 Starting tunnel...")
            
            cmd = "playit.exe --proto tcp --local-port 3389"
            print(f"Running: {cmd}")
            subprocess.run(cmd, shell=True)
        
        else:
            os.system("wget https://github.com/playit-cloud/playit-agent/releases/latest/download/playit-linux_64")
            os.system("chmod +x playit-linux_64")
            os.system("./playit-linux_64 --proto tcp --local-port 3389")
    
    def setup_localtunnel(self):
        print("🔧 Setting up LocalTunnel...")
        
        # Check if Node.js is installed
        try:
            subprocess.check_output(['node', '--version'])
        except:
            print("❌ Node.js not found! Please install Node.js first.")
            print("Download from: https://nodejs.org/")
            return
        
        # Install localtunnel
        print("📦 Installing LocalTunnel...")
        os.system("npm install -g localtunnel")
        
        # Create unique subdomain
        subdomain = f"myrdp{int(time.time())}"
        cmd = f"lt --port 3389 --subdomain {subdomain}"
        
        print("🚀 Starting tunnel...")
        print(f"Running: {cmd}")
        os.system(cmd)
    
    def setup_serveo(self):
        print("🔧 Setting up Serveo SSH tunnel...")
        
        cmd = "ssh -R 80:localhost:3389 serveo.net"
        print("🚀 Starting SSH tunnel...")
        print(f"Running: {cmd}")
        os.system(cmd)
    
    def check_rdp_status(self):
        print("🔍 Checking RDP status...")
        
        if self.system == 'windows':
            # Check if RDP is enabled
            try:
                result = subprocess.check_output('reg query "HKLM\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" /v fDenyTSConnections', shell=True)
                if b'0x0' in result:
                    print("✅ RDP is enabled")
                else:
                    print("❌ RDP is disabled")
                    print("💡 Enable RDP: Control Panel > System > Remote Settings")
            except:
                print("❓ Could not check RDP status")
    
    def run(self):
        self.print_banner()
        self.check_rdp_status()
        
        choice = input("\n🎯 Select method (1-4): ").strip()
        
        if choice in self.tunnel_methods:
            print(f"\n🚀 Starting method {choice}...")
            self.tunnel_methods[choice]()
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    tunnel = RDPTunnel()
    tunnel.run()
