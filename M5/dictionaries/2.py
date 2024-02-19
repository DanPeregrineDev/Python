capital = {"Portugal": "Lisboa", "Espanha": "Madrid", "Franca": "Paris", "Alemanha": "Berlin"}

novoPais = input("Escreve um novo pais: ")
novaCapital = input("Escreve uma nova capital: ")

capital.update({novoPais: novaCapital})

for pais in capital:
    print(f"A capital de {pais} é {capital[pais]}")

# Search contry

pesquiza = input("Pais a pesquizar: ")

resultado = capital.get(pesquiza)

if capital:
    print(f"A capital de {pesquiza} é {resultado}")
else:
    print(f"{pesquiza} não encontrado")

# Search capital

capitalAPesquizar = input("Capital a pesquizar: ")

if capitalAPesquizar not in capital.values():
    print("Essa capital não existe")

for pais, cap in capital.items():
    if cap == capitalAPesquizar:
        print(pais)