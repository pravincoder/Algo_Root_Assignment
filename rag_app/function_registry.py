# function_registry.py
import os
import webbrowser
import psutil
import subprocess

def open_chrome():
    """Opens Google Chrome and navigates to Google.com."""
    webbrowser.open("https://www.google.com")

def open_calculator():
    """Opens the system calculator."""
    os.startfile("calc.exe")  # Windows-specific; adjust for other OS

def get_cpu_usage():
    """Returns the current CPU usage percentage."""
    return psutil.cpu_percent()

def run_shell_command(command):
    """Executes a shell command and returns the output."""
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return result.stdout