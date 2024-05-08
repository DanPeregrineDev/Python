"""
Programa para guardar dados de uma lista com vários alunos em um ficheiro de texto
Neste projeto os dados estão todos na lista durante a execução do programa
"""
import os
import utils

#Lista dos alunos
alunos = []

#nome do ficheiro
nomeFicheiro = "alunos.txt"

def criar_aluno():
    """Função para ler os seguintes dados:
    Nome, morada, email e idade de um aluno
    Devolve um dicionário com os dados"""
    
    aluno = {
        "nome": utils.le_texto("Nome do aluno: "),
        "morada": utils.le_texto("Morada do aluno: "),
        "email": utils.le_email("Email do aluno: "),
        "idade": utils.le_numero("Idade do aluno: ")
    }

    return aluno

def listar():
    """Função para listar os alunos da lista"""
    if len(alunos) == 0:
        print("=" * 40)
        print("Vazio")
    
    for aluno in alunos:
        print(f"Nome: {aluno['nome']} | Morada: {aluno['morada']} | Email: {aluno['email']} | Idade: {aluno['idade']}")

def adicionar():
    """Função para adicionar um aluno à lista"""
    
    alunos.append(criar_aluno())

    print(f"Aluno inserido com sucesso! Tem {len(alunos)} alunos")

def pesquisar():
    pesquisa = input("Nome do aluno: ")

    for aluno in alunos:
        if pesquisa in aluno:
            print(aluno)

def apagar():
    """Função para apagar um aluno da lista"""
    
    nome = input("Nome do aluno: ")

    for aluno in alunos:
        if aluno['nome'] == nome:
            alunos.remove(aluno)

            print(f"O aluno {nome} foi removido com sucesso")

            break


def guardar():
    """Função para guardar todos os alunos num ficheiro de texto.
    Cada aluno deve ficar numa só linha com os seus dados separados por ,
    A primeira linha do ficheiro deve indicar quantos alunos existem no ficheiro"""
    
    with open(nomeFicheiro, 'w', encoding='UTF-8') as file:
        file.write(f"{len(alunos)}\n")

        for aluno in alunos:
            file.write(f"{aluno['nome']};{aluno['morada']};{aluno['email']};{aluno['idade']}\n")

def ler():
    """Função para ler os alunos do ficheiro para a lista. Primeira linha tem a quantidade de alunos"""
    if os.path.exists(nomeFicheiro) == False:
        return
    
    with open(nomeFicheiro, 'r', encoding='UTF-8') as file:
        nAlunos = int(file.readline())

        for i in range(nAlunos):
            dadosAluno = file.readline()

            if dadosAluno == "":
                continue

            dadosAluno = dadosAluno.split(';')

            if len(dadosAluno) > 4 or len(dadosAluno) < 4:
                print(f"Dados do aluno {dadosAluno[0]} corrompidos")
                continue

            aluno = {
                "nome": dadosAluno[0],
                "morada": dadosAluno[1],
                "email": dadosAluno[2],
                "idade": int(dadosAluno[3])
            }

            alunos.append(aluno)

        print(f"{nAlunos} alunos carregados do ficheiro")



def main():

    ler()

    while True:
        op=utils.menu("Ficheiros Texto",["Adicionar","Listar","Pesquisar","Apagar","Terminar"])
        if op==1:
            adicionar()
        if op==2:
            listar()
        if op==3:
            pesquisar()
        if op==4:
            apagar()
        if op==5:
            break
    
    guardar()

if __name__=="__main__":
    main()