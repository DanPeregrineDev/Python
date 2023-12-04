import sys

def howManyVogals(word):
    vogals = 0
    for letter in word:
        if letter in "aeiouAEIOU":
            vogals += 1
    return vogals

if sys.argv != 3:
    UserInput = input("Escreva uma palavra: ")
    print(howManyVogals(UserInput))
else:
    Word = sys.argv[1]
    print(howManyVogals(Word))

# ta tudo mal :\