import os

filePath = 'ex1.txt'

if os.path.exists(filePath) == False:
    print("File not found")

with open(filePath, 'r') as file:
    while True:
        line = file.readline()

        if not line:
            break

        print(line, end="")