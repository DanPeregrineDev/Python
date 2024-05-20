import csv

with open('dados.csv', 'r', encoding='UTF-8') as file:
    leitor = csv.DictReader(file)

    for dados in leitor:
        print(dados)