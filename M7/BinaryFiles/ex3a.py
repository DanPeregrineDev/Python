import pickle

with open('ex3.pkl', 'rb') as file:
    while True:
        try:
            print(pickle.load(file))
        except EOFError:
            break