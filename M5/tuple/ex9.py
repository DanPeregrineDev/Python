"""
    Conte quantas vezes a letra 'a' aparece na tupla de palavras
"""

cores_primarias = ("Vermelho", "Verde", "Azul")
cores_secundarias = ("Laranja", "Violeta", "Amarelo")

cores = cores_primarias + cores_secundarias

contar = 0
for i in range(len(cores)):
    for f in range(len(cores[i])):
        if "a" == cores[i][f]:
            contar += 1
print (contar)