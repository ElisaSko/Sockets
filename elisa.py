##modules

import socket
import argparse
import sys
import logging

##Arguments
parser = argparse.ArgumentParser(description='Some description.')

parser.add_argument('-c',help='A flag. When True, is a client', action='store_true')
parser.add_argument('-host', default='localhost', help='The host to connect to')

args = parser.parse_args()

##logging
logger=logging.getLogger(__name__)
handler=logging.StreamHandler(sys.stderr)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

##variables
HANDSHAKE_MSG = b'hello'
HANDSHAKE_REPLY = b'hi'

# create an INET, STREAMing socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def connect_client(host):
    s.connect((host, 34000))  #a utiliser quand on est le client
    logger.debug('connected')
    s.send(HANDSHAKE_MSG)
    logger.debug('sent handshake')
    s.recv(len(HANDSHAKE_REPLY))
    logger.debug('received handshake reply')

def connect_server():
    s.bind(('',34000))      #a utiliser quand on est le serveur
    s.listen()
    (client_socket, adrr) = s.accept()
    logger.debug('accepted connection')
    client_socket.recv(len(HANDSHAKE_MSG))
    logger.debug('received handshake')
    client_socket.send(HANDSHAKE_REPLY)
    logger.debug('sent handshake reply')

## on se connecte selon que c'est un client ou un serveur
if args.c == True:
    connect_client(args.host)
else:
    connect_server()
