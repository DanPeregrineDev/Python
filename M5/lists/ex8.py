userInput = input("Escreva uma fraze: ")
userInput += " "

palavras = {}

currentWord = ""

for i in range(len(userInput)):
    if userInput[i] == " ":
        palavras.update({f'{currentWord}': userInput.count(currentWord)})
        currentWord = ""
    elif userInput[i] != " ":
        currentWord += userInput[i]

print(palavras)
