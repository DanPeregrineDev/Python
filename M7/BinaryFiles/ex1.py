# Save a selected ammount of strings

import struct


def save():
    nStrings = int(input("How many strings: "))
    
    with open('ex1.dat', 'wb') as file:
        for i in range(nStrings):
            text = input("Text: ")
            data = struct.pack('100s', text.encode('UTF-8'))

            file.write(data)

        print("Saved Successfully")


def read():
    with open('ex1.dat', 'rb') as file:
        while True:
            data = file.read(100)

            if not data:
                break

            text = struct.unpack('100s', data)[0]

            print(text.decode('UTF-8').rstrip('\x00'))


def readSpecificLine():
    with open('ex1.dat', 'rb') as file:
        position = int(input("Line number: "))
        position = (position - 1) * 100

        file.seek(position)

        data = file.read(100)

        text = struct.unpack('100s', data)[0]
        print(text.decode('UTF-8').rstrip('\x00'))

print("1 - Write")
print("2 - Read")
print("3 - Read specific line")
option = int(input(""))

if option == 1:
    save()
if option == 2:
    read()
if option == 3:
    readSpecificLine()