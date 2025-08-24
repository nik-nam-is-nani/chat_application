#!/usr/bin/env python3
"""
Test script to verify the chat server works
"""

import sys
import subprocess
import time
import threading

def run_server():
    """Run the Flask server"""
    try:
        print("Starting Flask server...")
        # Use subprocess to capture output
        process = subprocess.Popen(
            [sys.executable, "app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        
        # Wait a bit for server to start
        time.sleep(3)
        
        # Check if process is still running
        if process.poll() is None:
            print("Server is running successfully!")
            return True
        else:
            stdout, stderr = process.communicate()
            print(f"Server failed to start. Error: {stderr}")
            return False
            
    except Exception as e:
        print(f"Error starting server: {e}")
        return False

def check_dependencies():
    """Check if all required packages are installed"""
    required_packages = ['Flask', 'flask_socketio', 'eventlet']
    missing = []
    
    for package in required_packages:
        try:
            __import__(package.lower().replace('-', '_'))
            print(f"✓ {package} is installed")
        except ImportError:
            print(f"✗ {package} is missing")
            missing.append(package)
    
    return missing

if __name__ == "__main__":
    print("Checking dependencies...")
    missing = check_dependencies()
    
    if missing:
        print(f"\nMissing packages: {missing}")
        print("Please install them using: pip install " + " ".join(missing))
    else:
        print("\nAll dependencies are installed!")
        print("Testing server startup...")
        success = run_server()
        
        if success:
            print("Server test passed! You can now run: python app.py")
        else:
            print("Server test failed. Please check the error messages above.")
