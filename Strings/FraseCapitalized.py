Frase = input("Escreva uma frase: ")

Frase2 = Frase[0].capitalize()

for i in range((len(Frase) - 1)):
    if Frase[i] == " ":
        Frase2 = Frase2 + Frase[i + 1].capitalize()
    else:
        Frase2 = Frase2 + Frase[i+1].lower()

print(Frase2)