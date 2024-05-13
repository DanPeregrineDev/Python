import struct

number = 1234

with open('int.dat', 'wb') as file:
    file.write(struct.pack('i', number))