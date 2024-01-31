"""
    Um programa para ler do utilizador as temperaturas mensais de 3 cidades durante 1 ano
    O programa deve mostrar a temperatura mais elevada
    Hacker:
        Calcular a media das temperaturas por cidade
        Calcular a media das temperaturas por mes
        Mostrar a cidade com a temperatura media mais elevada
        Mostrar o mes com a temperatura media mais elevada
"""

import numpy

temperaturas = numpy.zeros((3, 12), 'f')

for l in range(temperaturas.shape[0]):
    for c in range(temperaturas.shape[1]):
        temp = float(input(f"Escreva a temperatura para a cidade de {l + 1} correspondente ao mes {c + 1}: "))

        temperaturas[l, c] = temp

maiorTemp = temperaturas[0, 0]

for l in range(temperaturas.shape[0]):
    for c in range(temperaturas.shape[1]):
        if temperaturas[l, c] > maiorTemp:
            maiorTemp = temperaturas[l, c]

print(f"A maior temperatura foi {maiorTemp}")

maiorMedia = 0
for l in range(temperaturas.shape[0]):
    soma = 0
    for c in range(temperaturas.shape[1]):
        soma += temperaturas[l, c]
    media = soma / 12
    if l == 0 or media > maiorMedia:
        maiorMedia = media
        cidade = l
    print(f"Aa media da temperatura da cidade {l} foi {media}")
print(f"A cidade com temperatura media mais elevada foi a cidade {cidade}")

for c in range(temperaturas.shape[1]):
    soma = 0
    for l in range(temperaturas.shape[0]):
        soma += temperaturas[l, c]
    media = soma / 3
    if c == 0 or media > maiorMedia:
        maiorMedia = media
        mes = c
    print(f"A media da temperatura do mes {c} foi {media:.1f}")
print(f"O mes com temperatura media mais elevada foi a cidade {cidade}")