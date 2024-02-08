def largest(tuplo):
    largest = tuplo[0]
    for i in range (len(tuplo)):
        if len(tuplo[i]) > len(largest):
            largest = tuplo[i]
    return largest

cores_primarias = ("Vermelho", "Verde", "Azul")
cores_secundarias = ("Laranja", "Violeta", "Amarelo")

cores = cores_primarias + cores_secundarias
print(largest(cores))