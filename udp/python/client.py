import socket
 
size = 8192
 
try:
  for i in range(51):
    msg = f'{i}'
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.sendto(msg.encode('utf-8'), ('localhost', 9876))
    print(sock.recv(size).decode())
    sock.close()
 
except:
  print("cannot reach the server")