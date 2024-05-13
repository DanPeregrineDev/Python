import struct

with open('string.dat', 'rb') as file:
    data = file.read(100)

    text = struct.unpack('100s', data)[0]

    cleanText = text.decode('UTF-8').rstrip('\x00')

print(cleanText)