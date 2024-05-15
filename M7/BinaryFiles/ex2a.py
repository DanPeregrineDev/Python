import pickle

with open('ex2.dat', 'rb') as file:
    while True:
        try:
            obj = pickle.load(file)
            print(obj)
        except EOFError:
            break