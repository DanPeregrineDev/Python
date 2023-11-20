N = int(input("Quantos valores pretende inserir: "))

soma = 0

for i in range(N):
    x = int(input("Intruduza o valor: "))
    if i == 0:
        Nmaior = x
    if Nmaior < x:
        Nmaior = x
    soma = soma + x

print("A soma é: %d"% soma)
print("Média é %.2f"% (soma/N))
print("O maior numero que inseriu foi o: %d"% Nmaior)