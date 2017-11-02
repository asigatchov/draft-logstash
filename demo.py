import socket
import json
import sys

HOST = '127.0.0.1'
PORT = 5228


try:
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  #sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except socket.error, msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(1)

try:
  sock.connect((HOST, PORT))
except socket.error, msg:
  sys.stderr.write("[ERROR] %s\n" % msg[1])
  sys.exit(2)

msg = {'@message': 'python test message', '@tags': ['python', 'test']}
sock.send(json.dumps(msg))
sock.close()
sys.exit(0)


 
# sock = socket.socket( socket.AF_INET, # Internet
#                       socket.SOCK_DGRAM ) # UDP
# sock.sendto( MESSAGE, (UDP_IP, UDP_PORT) )
