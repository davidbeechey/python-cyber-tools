import socket
import _thread
import sys
import time

def scanner(target, port, protocol):
    try:
        service = socket.getservbyport(port, protocol)
        print(f"{protocol} port: {str(port)} open. Service: {service}")

        global open_ports
        open_ports += 1
    except:
        pass

try:
    target = sys.argv[1]
except:
    quit("\nERROR: Please provide the target (IP address)\n")

try:
    protocol = sys.argv[2]
except:
    quit("\nERROR: Please provide the protocol (tcp or udp)\n")

print(f"\nScanning: {target}\n")

open_ports = 0
max_port = 1024
start_time = time.time()

for port in range(1, max_port):
    try:
        _thread.start_new_thread(scanner, (target, port, protocol))
        time.sleep(0.000001)
    except KeyboardInterrupt:
        quit("\nStopping...\n")

print(f"\nTotal ports scanned: {max_port}\nOpen ports: {open_ports}\nTime taken: {round(time.time() - start_time,2)}s")

if input():
    quit("Exiting...")