animais = {('Cao', 'Pitbull'): {'Idade': 5, 'Dono': 'Joaquim'}, ('Tartaruga', 'Ninja'): {'Idade': 10, 'Dono': 'Maria'}, ('Elefante', 'Voador'): {'Idade': 41, 'Dono': 'Pablo'}}

for chave, valor in animais.items():
    if valor['Dono'] == "Joaquim":
        print(chave[0], chave[1])

print("")

for chave, valor in animais.items():
    print(chave[1])

print("")

for i in animais:
    maior = 0
    if animais[i]['Idade'] > maior:
        maior = animais[i]['Idade']
print(f"O animal mais velho tem {maior} anos")