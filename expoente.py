B = float(input("Escreva a base: "))
E = int(input("Escreva o expoente: "))

M = 1

for i in range(E):
    M = M * B

print(M)