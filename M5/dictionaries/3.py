phrase = input("Escreva uma fraze: ")
phrase = phrase.lower()
phrase = phrase.strip()
phrase = phrase + " "

dictionary = {}

currentWord = ""

for letra in phrase:
    if letra != " ":
        currentWord = currentWord + letra
    else:
        if currentWord in dictionary:
            dictionary[currentWord] += 1
        else:
            dictionary[currentWord] = 1
        currentWord = ""


print(dictionary)