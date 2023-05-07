# echo-client.py

import configparser
import socket
from time import sleep

import GPIO_driver


def main():
    # reads
    config = configparser.ConfigParser()
    config.read(''.join((__file__, "\\..\\..\\..\\config.ini")))
    # sets variables to their values in the config file
    TESTMODE = config['rover'].getboolean('testmode')
    HOST = config['rover']['laptop_ip']
    PORT = int(config['rover']['port'])
    MAXATTEMPTS = int(config['rover']['max_connection_attempts'])

    # makes the server run on localhost if in testmode so it can be tested with a single machine
    if TESTMODE:
        print(
            "\x1b[91m" + "WARNING: TESTMODE is curently active. This can be disabled in the config file" + "\x1b[0m")
        HOST = '127.0.0.1'

    # opens a socket which is used to communicate over the ethernet cable
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as clientSocket:
        connected = False
        numAttempts = 0

        # trys to connect to the server using its ip and port number.
        print(f"Attempting to connect to {HOST}: {PORT}...")
        while not connected:
            numAttempts += 1
            try:
                clientSocket.connect((HOST, PORT))
                connected = True

            except socket.error:
                if numAttempts == MAXATTEMPTS:
                    print(f"Can't connect to {HOST}: {PORT}")
                    exit()

                print(f"Failed to connect. Retrying...")
                sleep(5)

        print(f"Connected to {HOST} on port {PORT}")
        # repeatedly checks for incoming data
        while True:
            # 1024 refers to the buffersize of the incoming data
            data = clientSocket.recv(1024)

            # if empty data packet is recieved then break while loop (end connection)
            if not data:
                break

            GPIO_driver.handleInput(data.decode('UTF-8'))
            print(f"Received message: '{data.decode('UTF-8')}'")

            # decodes binary data into string using UTF-8 encoding


if __name__ == '__main__':
    main()
