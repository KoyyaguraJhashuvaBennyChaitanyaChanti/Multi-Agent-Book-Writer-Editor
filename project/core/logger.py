import datetime
import os

os.makedirs("project/memory", exist_ok=True)

def log(msg):
    ts = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{ts}] {msg}")
    with open("project/memory/logs.txt", "a") as f:
        f.write(f"[{ts}] {msg}\n")
