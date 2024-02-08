"""
    Encontre o indice da primeira ocurrencia de 'Verde' na tupla de cores
"""

cores_primarias = ("Vermelho", "Verde", "Azul")
cores_secundarias = ("Laranja", "Violeta", "Amarelo")

cores = cores_primarias + cores_secundarias

a = cores.index("Verde")

print(a)