#client ou serveur
#liste de mot à lire
#numéro de serveur ? 34000

##modules

import socket
import argparse

##Arguments
parser = argparse.ArgumentParser(description='Some description.')

parser.add_argument('-c',help='A flag. When True, is a client', action='store_true')

args = parser.parse_args()




# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## on se connecte selon que c'est un client ou un serveur
if args.c == True:
    s.connect(('localhost', 34000))  #à utiliser quand on est le client
else:
    s.bind(('127001',34000))      #à utiliser quand on est le serveur
    s.listen()
    (client_socket, adrr) = s.accept()


class MySocket:

    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(
                            socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def connect(self, host, port):
        self.sock.connect((host, port))

    def mysend(self, msg):
        totalsent = 0
        while totalsent < MSGLEN:
            sent = self.sock.send(msg[totalsent:])
            if sent == 0:
                raise RuntimeError("socket connection broken")
            totalsent = totalsent + sent

    def myreceive(self):
        chunks = []
        bytes_recd = 0
        while bytes_recd < MSGLEN:
            chunk = self.sock.recv(min(MSGLEN - bytes_recd, 2048))
            if chunk == b'':
                raise RuntimeError("socket connection broken")
            chunks.append(chunk)
            bytes_recd = bytes_recd + len(chunk)
        return b''.join(chunks)