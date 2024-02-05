import numpy

data = numpy.array([[0.01, 0], [0.05, 0], [0.1, 0], [0.2, 0], [0.5, 0], [1, 0], [2, 0]])

# Stock

for l in range(data.shape[0]):
    stockCoins = int(input(f"Quantas moedas de {data[l, 0]} tem?: "))
    data[l, 1] = stockCoins

toPay = float(input("Qual o valor a pagar?: "))
recievedCash = float(input("Insira o dinheiro: "))

change = recievedCash - toPay

if change > 0:
    print(f"Vao receber {change:.2f}€ de troco")

while change > 0:
    oldChange = change
    for i in range(data.shape[0], -1, -1):
        if data[i, 0] <= change and data[i, 1] > 0:
            data[i, 1] -= 1
            print(f'Recebeu uma moeda de {data[i, 0]}')
            change -= data[i, 1]
            break
    if oldChange == change:
        print("Não tenho mais moedas")
        break