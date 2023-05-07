# echo-server.py

import configparser
import socket
from time import sleep

import pygame
import XBcontroller


def main():

    # read config file
    config = configparser.ConfigParser()
    config.read(''.join((__file__, "\\..\\..\\..\\config.ini")))

    TESTMODE = config['DEFAULT'].getboolean('testmode')
    HOST = "192.168.1.25"
    # pick any number between 1024 and 65535 as long as it matches rover
    PORT = 65433

    if TESTMODE:
        print(
            "\x1b[91m" + "WARNING: TESTMODE is curently active. This can be disabled in the config file" + "\x1b[0m")
        HOST = '127.0.0.1'  # Standard loopback interface address (localhost)

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
                for event in events:  # allows multiple events to be handled at once
                    # inp = input("Enter msg:")
                    inp = cont.getInput(event)
                    if inp:
                        conn.sendall(inp.encode('UTF-8'))
                    sleep(0.01)


if __name__ == '__main__':
    main()
