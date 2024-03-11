animais = {("cão","pitbull"):{"idade":5,"dono":"joaquim"},
           ("gato","persa"):{"idade":6,"dono":"joaquim"},
           ("tartaruga","ninja"):{"idade":9,"dono":"ana"},
           ("priquito","preto"):{"idade":18,"dono":"joaquim"},
           ("priquito","pitbull"):{"idade":1,"dono":""},
           ("cão","ninja"):{"idade":10,"dono":"ana"},
           ("gato","preto"):{"idade":5,"dono":"joaquim"},
}

for chave, valor in animais.items():
    if valor['dono'] == "Joaquim":
        print(chave[0], chave[1])

print("")

contagem = {}

for chave in animais.keys():
    especie = chave[0]
    if especie in contagem:
        contagem[especie] += 1
    else:
        contagem[especie] = 1
print(contagem)

print("")


for i in animais:
    maior = 0
    if animais[i]['idade'] > maior:
        maior = animais[i]['idade']
print(f"O animal mais velho tem {maior} anos")