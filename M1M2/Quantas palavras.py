Texto = input("")

Palavras = 1

for letra in Texto:
    print(letra)
    if letra == " ":
        Palavras = Palavras + 1

print(" ")
print("Existem: ", Palavras, "palavras")