import os

file = 'testFile2.txt'

if os.path.exists(file) == False:
    print("File not found")
else:
    with open(file, 'r', encoding='UTF-8') as file:
        while True:
            text = file.readline()
        
            if not text:
                break
        
            print(text)