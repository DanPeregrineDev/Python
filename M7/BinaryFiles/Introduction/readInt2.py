import struct

with open("int2.dat", 'rb') as file:
    while True:
        temp = file.read(4)

        if not temp:
            break

        number = struct.unpack('i', temp)[0]

        print(number)

    pos = int(input("Qual o numero a ler: "))

    pos = (pos - 1) * 4

    file.seek(pos)

    temp = file.read(4)

    print(struct.unpack('i', temp)[0])