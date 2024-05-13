import struct

with open("int2.dat", 'rb') as file:
    while True:
        temp = file.read(4)

        if not temp:
            break

        number = struct.unpack('i', temp)[0]

        print(number)