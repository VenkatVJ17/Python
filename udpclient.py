import socket
MAX_SIZE_BYTES = 65535 # Mazimum size of a UDP datagram

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('The os assigned the address {} to me'.format(s.getsockname()))
message = input('Input lower case sentence: ')
data = message.encode('ascii')
s.sendto(data,('127.0.0.1',3000))
print('The os assigned the address {} to me'.format(s.getsockname()))
data, address = s.recvfrom(MAX_SIZE_BYTES)
text = data.decode('ascii')
print('The server {} replied with {!r}'.format(address, text))