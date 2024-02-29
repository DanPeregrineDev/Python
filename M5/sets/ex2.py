PSI = {
    'Modulos': ('Algoritmia', 'Estruturas de Controlo', 'Funções', 'Estruturas de Dados Estáticas'),
    'WebGrafia': {'3wschool.com', 'github.com/alunosnet', 'udacity.com'} ,
    'Aulas': ['M1', 'M1', 'M1', 'M2', 'M2', 'M3', 'M3', 'M4', 'M4', 'M4', 'M4'],
    'Avaliação': ['Teste Escrito', 'Teste prático', 'Teste prático', 'Teste prático']
}

# Mostrar os sites recomendados para a disciplina (webgrafia)

print(PSI['WebGrafia'])
print("")

# Mostrar o nome de um módulo pela posição (pedir ao utilizador)

nModulo = int(input("Escreva o numero do modulo: "))
print("")

while nModulo > 4 or nModulo < 1:
    print("Numero do modulo invalido!")
    nModulo = int(input("Escreva o numero do modulo: "))
    print("")

print(PSI['Modulos'][nModulo - 1])
print("")

# Mostrar as aulas que são dadas num módulo (pedir ao utilizador o nº do módulo)

numero = int(input("Digite o número do módulo que deseja consultar (1 a 4): "))

if numero >= 1 and numero <= 4:

    contador = 0

    for aula in PSI['Aulas']:

        if aula == f"M{numero}":
            contador += 1

    print(f"O módulo {PSI['Modulos'][numero-1]} tem {contador} aulas.")
    print("")

else:

    print("Número inválido. Tente novamente.")
    print("")

# Mostrar os módulos que tenham determinado conteudo (pedir ao utilizador)

print(PSI['Modulos'])
conteudo = input("Escreva o conteúdo que deseja procurar nos módulos: ").capitalize()

if conteudo in PSI['Modulos']:

    resultado = []

    for i, modulo in enumerate(PSI['Modulos']):

        if conteudo in modulo:
            resultado.append(f"M{i+1}")

    print(f"Os módulos que têm o conteúdo {conteudo} são: {', '.join(resultado)}.")
    print("")

else:

    print("Conteúdo inválido. Tente novamente.")
    print("")

# Mostrar os módulo cuja avaliação não é 'Teste Escrito'

resultado2 = []

for i, avaliacao in enumerate(PSI['Avaliação']):

    if avaliacao != 'Teste Escrito':
        resultado2.append(f"M{i+1}")

print(f"Os módulos que têm uma avaliação diferente de 'Teste Escrito' são: {', '.join(resultado2)}.")
print("")

# Mostrar o nº de módulos da disciplina

print(f"A disciplina tem {len(PSI['Modulos'])} módulos.")
print("")

# Adicionar mais 5 aulas do módulo M2

for i in range(5):
  PSI['Aulas'].append('M2')

print("Adicionado 5 aulas com sucesso")
print(f"Aulas: {PSI['Aulas']}")
print("")

# Adicionar uma chave nova para classificacoes que deve corresponder a uma lista de 4 notas indicadas pelo utilizador

classificacoes = []

for i in range(4):
    notas = input("Digite a nota que deseja atribuir ao módulo da disciplina: ")
    classificacoes.append(notas)

PSI['Classificacoes'] = classificacoes

print(PSI)