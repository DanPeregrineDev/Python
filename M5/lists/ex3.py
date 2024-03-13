notas = [17, 10, 4, 9]

positivas = 0
negativas = 0

for i in notas:
    if i >= 10:
        positivas += 1
    elif i < 10:
        negativas += 1

percentagemPositivas = positivas / len(notas) * 100
percentagemNegativas = negativas / len(notas) * 100

print(f"Positivos {percentagemPositivas}%")
print(f"Negativos {percentagemNegativas}%")

maior = 0

for i in notas:
    if i > maior:
        maior = i

print(maior)