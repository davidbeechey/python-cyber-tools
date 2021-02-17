import threading
import time
import os
from icmplib import ping
from termcolor import colored

def check_ping(hostname, x):
    global up, responses
    try:
        data = threading.local()
        data.response = ping(hostname, count=1, timeout=2)

        if data.response.is_alive:
            responses[x-1] = colored(f"{hostname} is up","green")
            up += 1

        else:
            responses[x-1] = colored(f"{hostname} is down","red")
    

    except KeyboardInterrupt:
        quit("Stopping...")

global up, responses
responses = [None for x in range(0,255)]
up = 0

for x in range(1,256):
    try:
        hostname = f"192.168.1.{str(x)}"
        t = threading.Thread(target = check_ping, args = (hostname,x))
        t.start()
        time.sleep(0.1)
        
    except KeyboardInterrupt:
        quit("Stopping...")

while threading.active_count() != 1:
    time.sleep(1)

for x in range(0,255):
    print(responses[x])

print(f"\nHosts scanned: 255\nHosts alive: {up}\n")