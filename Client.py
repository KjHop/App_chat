import socket
import sys
from threading import Thread

s = socket.socket()
host = socket.gethostname()
port = 12345
nick = raw_input('Wpisz nick: ')
s.connect((host, port))
def send(str):
   s.send("{}: {}".format(nick, str).encode('utf-8'))

def recv():
    while True:
         data = s.recv(1024)
         if not data: sys.exit(0)
         data_decoded= s.recv(1024).decode()
         print (data_decoded)
Thread(target=recv).start()
while 2:

   r = raw_input(': ')
   send(r)
   if r == "/close":
      s.close()
      sys.exit()
