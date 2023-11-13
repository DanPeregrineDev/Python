QuantosNumeros = int(input("Quantos numeros são?: "))

b = 0

print("Escreva os numeros:")
for i in range(1, (QuantosNumeros + 1)):
    a = int(input())
    b = a + b

print((b) / QuantosNumeros)