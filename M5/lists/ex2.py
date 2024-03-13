lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

t = []

for i in range(len(lista) - 1, -1, -1):
    t.append(lista[i])

print(t)

positivos = 0
negativos = 0

for i in lista:
    if i >= 0:
        positivos += 1
    elif i < 0:
        negativos += 1

percentagemPositivos = positivos / len(lista) * 100
percentagemNegativos = negativos / len(lista) * 100

print(f"Positivos {percentagemPositivos}%")
print(f"Negativos {percentagemNegativos}%")