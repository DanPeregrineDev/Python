def media(tuplo):
    soma = 0
    nPares = 0
    for i in tuplo:
        if i % 2 == 0:
            soma += i
            nPares += 1
    media = soma / nPares
    return media