nomes1 = {"Joaquim", "Ana", "Maria"}
nomes2 = {"Antonio", "Carla", "Joaquim", "Maria"}

uniao = nomes1.union(nomes2)
diferenca = nomes1.difference(nomes2)
comuns = nomes1.intersection(nomes2)

print(uniao, diferenca, comuns)

nomes1.add("pai natal")

if "pai natal" in nomes1:
    print("Existe")
else:
    print("n existe")