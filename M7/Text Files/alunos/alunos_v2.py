"""
Programa para guardar dados de vários alunos em um ficheiro de texto
Neste projeto os dados estão todos só no ficheiro e são lidos/escritos quando é necessário
"""
import os
import utils


#nome do ficheiro
nome_ficheiro = "alunos2.txt"

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
    """Função para listar os alunos do ficheiro"""

    if verificarExistenciaDeFicheiro() == False:
        return
    
    with open(nome_ficheiro, 'r', encoding='UTF-8') as file:
        while True:
            aluno = file.readline()

            if not aluno:
                break
            
            aluno = aluno.split(';')

            print(f"Nome: {aluno[0]} | Morada: {aluno[1]} | Email: {aluno[2]} | Idade: {aluno[3]}")

def pesquisar():
    if verificarExistenciaDeFicheiro() == False:
        return
    
    pesquisa = input("Nome do aluno: ")

    with open(nome_ficheiro, "r", encoding='UTF-8') as file:
        while True:
            linha = file.readline()

            if pesquisa in linha:
                print(linha)

def adicionar():
    """Função para adicionar um aluno ao ficheiro"""
    
    aluno = criar_aluno()

    with open(nome_ficheiro, 'a', encoding='UTF-8') as file:
        file.write(f"{aluno['nome']};{aluno['morada']};{aluno['email']};{aluno['idade']}\n")
    
    print(f"Aluno {aluno['nome']} adicionado com sucesso")

def apagar():
    """Função para remover um aluno do ficheiro"""
    
    if verificarExistenciaDeFicheiro() == False:
        return
    
    nome = utils.le_texto("Nome do aluno: ")

    with open(nome_ficheiro, 'r', encoding='UTF-8') as readFile:
        with open("temp.txt", 'w', encoding='UTF-8') as tempFile:
            while True:
                linha = readFile.readline()

                if not linha:
                    break

                aluno = linha.split(';')
                
                apaguei = False

                if aluno[0] != nome or apaguei == True:
                    tempFile.write(linha)
                else:
                    apaguei = True

    os.remove(nome_ficheiro)
    os.rename("temp.txt", nome_ficheiro)

def verificarExistenciaDeFicheiro():
    if os.path.exists(nome_ficheiro) == False:
        print("Ainda não tem dados")
        return False
    return True

def main():
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

if __name__=="__main__":
    main()