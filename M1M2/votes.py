C1 = int(input("Quantidade de votos do candidado 1: "))
C2 = int(input("Quantidade de votos do candidado 2: "))
C3 = int(input("Quantidade de votos do candidado 3: "))

VT = C1 + C2 + C3

P1 = C1 / VT * 100
P1 = int(P1)
P2 = C2 / VT * 100
P2 = int(P2)
P3 = C3 / VT * 100
P3 = int(P3)

print(P1, "%")
print(P2, "%")
print(P3, "%")

if P1 > 50 or P2 > 50 or P3 > 50:
    print("Ouve maioria absoluta")
else:
    print("Não ouve maioria absoluta")

if C1 > C2 and C1 > C3:
    print("O candidado 1 Ganhou")

if C2 > C1 and C2 > C3:
    print("O candidado 2 ganhou")

if C3 > C1 and C3 > C2:
    print("O candidado 3 ganhou")