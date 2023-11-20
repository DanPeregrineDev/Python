#Exercicio N5

QuantosAlunos = int(input("Quantos alunos?: "))

Positivas = 0
Negativas = 0

for i in range (0, QuantosAlunos):
    QualANota = int(input("Escreva a nota do aluno: "))
    # Validation
    while QualANota > 20 or QualANota < 0:
        print(QualANota, "é uma nota invalida")
        QualANota = int(input("Escreva a nota do aluno novamente: "))
    # Operation
    if QualANota >= 10:
        Positivas = Positivas + 1
    elif QualANota < 10:
        Negativas = Negativas + 1

Media = (Positivas + Negativas) / 2

print("Ouve", Positivas, "Positivas e ouve", Negativas, "Negativas")
print(Media)