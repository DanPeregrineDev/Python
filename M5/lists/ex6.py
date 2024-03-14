clube1 = []
clube2 = []

userInput = ""

while True:
    socio = input("Nome do socio para o clube1 (deixe vazio para continuar): ")
    if socio == "":
        break
    clube1.append(socio)

print("")

while True:
    socio = input("Nome do socio para o clube2 (deixe vazio para continuar): ")
    if socio == "":
        break
    clube2.append(socio)

print("")
print(clube1)
print(clube2)

t = []

for i in range(len(clube1)):
    for a in range(len(clube2)):
        if clube1[i] == clube2[a]:
            t.append(clube1[i])

print("")
print(t)

if len(t) > 0:
    for i in t:
        choise = int(input(f"Em qual clube deve ficar o {i} (1 ou 2): "))
        if choise == 1:
            clube2.remove(i)
            t.remove(i)
        elif choise == 2:
            clube1.remove(i)
            t.remove(i)

clube1.sort()
clube2.sort()
t.sort()

print("")
print(clube1)
print(clube2)
print(t)