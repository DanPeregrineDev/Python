lista = ["Alegria", "Descoberta", "Estrela", "Viagem", "Harmonia", "Mistério", "Oceano", "Poema", "Luz", "Sonho"]

consoantes = 0

for i in lista:
    for letra in i:
        if letra in "aeiouAEIOU":
            consoantes += 1

print(consoantes, "consoantes")

maior = 0
maiorPalavra = ""

for i in lista:
    if len(i) > maior:
        maior = len(i)
        maiorPalavra = i

print(maiorPalavra)

comessamComA = 0

for i in lista:
    if i[0] in "aA":
        comessamComA += 1

print(comessamComA)