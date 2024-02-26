benfica = []
sporting = []
nome = ""
while nome != "Proximo":
    nome = input(f"Escreva o nome do socio no clube do benfica (escreva proximo para continuar): ").capitalize()
    if nome != "Proximo":
        benfica.append(nome)
nome = ""
while nome != "Proximo":
    nome = input(f"Escreva o nome do socio no clube do sporting (escreva proximo para continuar): ").capitalize()
    if nome != "Proximo":
        sporting.append(nome)
for i in benfica:
    if i in sporting:
        benfica.remove(i)
        sporting.remove(i)

print(benfica, sporting)