signos = ["Rato", "Búfalo", "Tigre", "Coelho", "Dragão", "Serpente", "Cavalo", "Cabra", "Macaco", "Galo", "Cão", "Porco"]

data_nascimento = input("Data de nascimento (dd/mm/yyyy): ")
ano = int(data_nascimento[6:])

posicao = (ano - 1900) % 12

print(signos[posicao])