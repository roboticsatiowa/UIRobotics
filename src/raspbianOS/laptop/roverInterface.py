# echo-server.py

import socket
import warnings
import XBcontroller
import pygame
from time import sleep

TESTMODE = True

HOST = "192.168.1.25"  
PORT = 65432  # pick any number between 1024 and 65535 as long as it matches rover

if TESTMODE:
    warnings.warn("TESTMODE is curently active. change TESTMODE variable to false to disable")
    HOST = '127.0.0.1' # Standard loopback interface address (localhost)

def main():
    pygame.init()
    cont = XBcontroller.XBcontroller()
    
    # AF_INET specifies IPv4        SOCK_STREAM specifies TCP Protocol
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print(f"Starting server on: {HOST} Port: {PORT}...")
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print(f"Connected to client {addr[0]} on port {addr[1]}")
            while True:
                events = pygame.event.get()
                for event in events: # allows multiple events to be handled at once
                    input = cont.getInput(event)
                    if input == 'PRESSED BCK':
                        print("Back button pressed: Terminating connection")
                        exit()
                    conn.sendall(input.encode('UTF-8'))
                sleep(0.02)
                
if __name__ == '__main__':
    main()