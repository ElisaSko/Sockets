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

HANDSHAKE_MSG = b'hello'
HANDSHAKE_REPLY = b'hi'

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## on se connecte selon que c'est un client ou un serveur
if args.c == True:
    s.connect(('localhost', 34000))  #a utiliser quand on est le client
    print('connected')
    s.send(HANDSHAKE_MSG)
    print('sent')
else:
    s.bind(('',34000))      #a utiliser quand on est le serveur
    s.listen()
    (client_socket, adrr) = s.accept()
    print('accepted')
    client_socket.recv(len(HANDSHAKE_MSG))
    client_socket.send(HANDSHAKE_REPLY)