import time
import sys
import socket
import os

def master():
    s = socket.socket()
    host = socket.gethostname()
    print(host)
    port = 8080
    s.bind((host, port))
    print("")
    print("Waiting for any incoming connection ...")
    print("")
    s.listen(1)
    conn, addr = s.accept()
    print("")
    print(addr, " - Has connected to the server")
    print("")



    command = input(str("Command : "))
    conn.send(command.encode())
    print("")
    print("Command has been sent successfully. Waiting for confirmation")
    print("")
    data = conn.recv(1024)
    if data:
        print("Command has been recieved and executed")
        print("")

master()
"""
if __name__ == '__main__':
    while True:
        master()    """