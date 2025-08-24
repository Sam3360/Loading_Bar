import time
import sys
import random


GREEN = "\033[92m"
RESET = "\033[0m"

bar_length = 30
percent = 0

while percent <= 100:
    filled = int(bar_length * percent / 100)
    bar = "█" * filled + "░" * (bar_length - filled)

    sys.stdout.write(f"\r{GREEN}[{bar}] {percent}%{RESET}")
    sys.stdout.flush()

    
    if percent < 20:
        delay = random.uniform(0.3, 0.6)
    elif percent < 60:
        delay = random.uniform(0.1, 0.3)
    elif percent < 85:
        delay = random.uniform(0.2, 0.5)
    else:
        delay = random.uniform(0.4, 0.8)

    time.sleep(delay)
    percent += random.choice([1, 1, 1, 2])  

print("\nDone!")
