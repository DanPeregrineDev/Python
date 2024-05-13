import struct

howMany = int(input("Quantos inteiros pretende gravar?: "))

with open("int2.dat", 'wb') as file:
    for i in range(howMany):
        number = int(input("Numero: "))
        file.write(struct.pack('i', number))