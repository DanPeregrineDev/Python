benfica = []
sporting = []
def adicionarNome(a, b):
    nome = ""
    while nome != "Proximo":
        nome = input(f"Escreva o nome do socio no clube do {b} (escreva proximo para continuar): ").capitalize()
        if nome != "Proximo":
            a.append(nome)
adicionarNome(benfica, "Benfica")
adicionarNome(sporting, "Sporting")
for i in benfica:
    if i in sporting:
        benfica.remove(i)
        sporting.remove(i)
print(benfica, sporting)