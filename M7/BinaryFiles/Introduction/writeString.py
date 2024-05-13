import struct

text = input("Texto: ")

with open("string.dat", 'wb') as file:
    data = struct.pack('100s', text.encode('UTF-8'))
    
    file.write(data)