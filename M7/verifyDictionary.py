import os

dictionary = []

phrase = input("").lower().replace(',', '')

while len(phrase) == 0:
    print("Frase inválida. Escreva outravez:")
    phrase = input("")

phraseWords = phrase.split()



if os.path.exists('dwords.txt') == False:
    print("File not found")
else:
    with open('words.txt', 'r') as file:
        while True:
            word = file.readline()

            if not word:
                break

            dictionary.append(word.strip("\n").lower())

for i in phraseWords:
    if i not in dictionary:
        print(f"The word {i} is not in the dictionary")
print("done")