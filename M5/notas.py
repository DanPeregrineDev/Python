turma = {
    123: {'M01': 10, 'M02': 15, 'M03': 8},
    124: {'M01': 10, 'M02': 15, 'M03': 18},
    125: {'M01': 12, 'M02': 12, 'M03': 10}
}

# Mostrar a notas dos alunos, primeiro deve mostrar o nprocesso e depois a nota de cada modulo

for i in turma:
    print(f"{i} - {turma[i]}")

print("")# Calcular e mostrar a media das notas por aluno

for i in turma:

    soma = 0

    for modulos, nota in turma[i].items():
        soma += nota

    print(f"O nProcesso {i} teve uma media de: {soma / len(turma[i].values())}")

print("")# Calcular e mostrar o n de positivas e negativas por aluno

for i in turma:

    positivas = 0
    negativas = 0

    for modulos, nota in turma[i].items():
        if nota >= 10:
            positivas += 1
        elif nota < 10:
            negativas += 1
        else:
            print("ERRO")
    
    print(f"O nProcesso {i} teve {positivas} positivas e {negativas} negativas.")

print("")# Calcular e mostrar qual o aluno com melhor media

for i in turma:

    somas = []

    for notas in turma[i].values():
        somas.append(notas)

    print(soma)