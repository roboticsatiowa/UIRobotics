# echo-server.py

import os
import socket
from time import sleep
from pyautogui import run

import pygame

import XBcontroller

# read config file
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
with open(os.path.join(__location__, 'config')) as config:
    L = config.read().split('\n')
    params = {i.split(':')[0].strip(): i.split(':')[1].strip() for i in L if ':' in i}

TESTMODE = params['testmode'] == 'True'
HOST = params['laptop_ip']
PORT = int(params['port'])  # pick any number between 1024 and 65535 as long as it matches rover

if TESTMODE:
    print("\x1b[91m" + "WARNING: TESTMODE is curently active. This can be disabled in the config file" + "\x1b[0m")
    HOST = '127.0.0.1' # Standard loopback interface address (localhost)
    
def quit(message:str):
    print(message)
    exit()

def endConn(message:str, conn:socket.socket):
    print(message)
    conn.close()

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
            running = True
            while running:
                events = pygame.event.get()
                for event in events: # allows multiple events to be handled at once
                    inp = input("Enter msg:")
                    # inp = cont.getInput(event)
                    if inp == 'PRESSED BCK':
                        print("Back button pressed: Terminating connection")
                        conn.close()
                        running = False
                        break
                    conn.sendall(inp.encode('UTF-8'))
                    sleep(0.01)
                
if __name__ == '__main__':
    while 1:
        main()
