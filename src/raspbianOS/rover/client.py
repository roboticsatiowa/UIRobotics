# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(f"Connected to {HOST} on port {PORT}...")
    while True:
        data = s.recv(1024)
        if not data:
            break
        print(f"Received message: '{data.decode('UTF-8')}'")

print("Connection closed by server")      