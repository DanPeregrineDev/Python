import pickle

dictionary = {
    'name': 'Joaquim',
    'age': 22,
    'email': 'email@email.com',
    'phone': '932422554'
}

FILE_NAME = 'ex2.dat'

with open(FILE_NAME, 'ab') as file:
    pickle.dump(dictionary, file)