a = int(input("Escreva o numero que quer comessar a somar: "))
b = int(input("Escreva o numero que quer terminar a somar: "))

# Validation
if a > b:
    print("O primeiro valor não pode ser maior que o ultimo valor")
    v_q = input("Quer trocar a ordem? y/n ")
    if v_q == "n":
        exit()
    elif v_q == "y":
        T = a
        a = b
        b = T

# Operation
Soma = 0
for i in range(a, (b + 1)): # b + 1 para incluir o ultimo numero
    Soma = i + Soma
    print(Soma)