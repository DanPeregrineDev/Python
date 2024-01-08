def nPares(n, m):
    if n < m:
        for i in range(n, m + 1):
            if i % 2 == 0:
                print(i)
    else:
        print("Erro: segundo parametro têm que ser maior que o primeiro. Ex: nPares(1, 2)")

nPares(20, 60)