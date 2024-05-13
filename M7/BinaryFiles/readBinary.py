import struct

with open('int.dat', 'rb') as file:
    temp = file.read(4)
    number = struct.unpack('i', temp)[0]

print(number)