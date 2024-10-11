import socket

size = 8192

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('', 9876))
i=0

try:
  while True:
    data, address = sock.recvfrom(size)
    data = data.decode()+' ' + str(i)
    sock.sendto(data.encode('utf-8'), address)
    i+=1

finally:
  sock.close()