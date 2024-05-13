import os

filePath = 'ex1.txt'
names = []

if os.path.exists(filePath) == False:
    print("File not found")

with open(filePath, 'r+', encoding='UTF-8') as file:
    while True:
        line = file.readline()

        if not line:
            break

        if line.strip("\n") in names:
            continue
        else:
            names.append(line.strip("\n"))

with open(filePath, 'w', encoding='UTF-8') as file2:
    for i in range(len(names)):

        file2.write(f"{names[i]}\n")