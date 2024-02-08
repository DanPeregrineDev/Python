def soma(tuplo):
    soma = 0
    for i in tuplo:
        soma += i
    return soma

tuplo = (1, 6, 2) # 9
print(soma(tuplo))