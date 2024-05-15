import os

files = os.listdir('.')

print(files)

for file in files:
    if os.path.isfile(file):
        print(file)

def tree(path):
    files = os.listdir(path)

    print(files)

    for file in files:
        if not os.path.isfile(os.path.join(path, file)):
            tree(os.path.join(path, file))

tree(".")