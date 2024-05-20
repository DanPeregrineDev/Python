import csv

dados = [
    {'nome': 'Joaquim',
     'idade': 30,
     'cidade': 'Viseu'},
     {'nome': 'Maria',
     'idade': 25,
     'cidade': 'Lisboa'},
     {'nome': 'António',
     'idade': 35,
     'cidade': 'Tondela'}
]

with open('dados.csv', 'w', encoding='UTF-8', newline='') as file:
    campos = dados[0].keys()
    gravador = csv.DictWriter(file, fieldnames=campos)
    gravador.writeheader()

    for dado in dados:
        gravador.writerow(dado)