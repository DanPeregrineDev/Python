import os

dictionary = []
toRemove = ";,.:?!="

phrase = input("").lower()

while len(phrase) == 0:
    print("Frase inválida. Escreva outravez:")
    phrase = input("")

for c in phrase:
    if c in toRemove:
        phrase = phrase.replace(c, '')

phraseWords = phrase.split()



if os.path.exists('words.txt') == False:
    print("File not found")
else:
    with open('words.txt', 'r') as file:
        while True:
            word = file.readline()

            if not word:
                break

            dictionary.append(word.strip("\n").lower())

hasErrors = False

for i in phraseWords:
    if i not in dictionary:
        print(f"The word {i} is not in the dictionary")
        hasErrors = True

if hasErrors == False:
    print("No errors found")