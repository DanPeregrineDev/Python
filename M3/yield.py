def gerar_pares(limite):
    n = 0
    while n < limite:
        yield n
        n += 2

for n_par in gerar_pares(10):
    print(n_par)