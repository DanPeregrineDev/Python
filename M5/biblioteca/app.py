import numpy as np
from termcolor import colored, cprint

# Função que permite ao utilizador adicionar um livro
# O livro novo estará sempre disponivel
# Verifique se ainda existe espaço no array antes de adicionar
# Tenha atenção para não repetir o id do livro
def adicionar_livro(biblioteca, nLivros):
    titulo = input("Escreva o titulo do livro: ")

    biblioteca[nLivros] = {"id_livro": nLivros + 1, "titulo": titulo, "disponivel": True, "nome_leitor":""}

    cprint("Sucesso", "green")
    return biblioteca


# Função para mostrar os livros
# deve permitir escolher se lista todos ou só os disponíveis ou só os indisponíveis
def listar_livros(biblioteca, nLivros):

    selection = 0

    while selection < 1 or selection > 3:
        print(f"Livros: {nLivros}")
        print("1 - Mostrar todos")
        print("2 - Mostrar disponíveis")
        print("3 - Mostrar indesponíveis")
        print("")

        selection = int(input(""))
        print("")

        if selection < 1 or selection > 3:
            cprint("Seleção inválida!", "red")
            print("")

    if selection == 1:
        for livro in biblioteca:
            if livro != None:

                if livro['nome_leitor'] == "":
                    livro['nome_leitor'] = "Nenhum"

                if livro['disponivel'] == True:
                    print(f"ID: {livro['id_livro']} | Titulo: '{livro['titulo']}' | Disponível: {colored(livro['disponivel'], "green")} | Leitor: {livro['nome_leitor']}")
                elif livro['disponivel'] == False:
                    print(f"ID: {livro['id_livro']} | Titulo: '{livro['titulo']}' | Disponível: {colored(livro['disponivel'], "red")} | Leitor: {livro['nome_leitor']}")
                print("")

    if selection == 2:
        for livro in biblioteca:
            if livro != None:
                if livro['disponivel'] == True:

                    if livro['nome_leitor'] == "":
                        livro['nome_leitor'] = "Nenhum"

                    print(f"ID: {livro['id_livro']} | Titulo: '{livro['titulo']}' | Disponível?: {colored(livro['disponivel'], "green")} | Leitor: {livro['nome_leitor']}")
                    print("")

    if selection == 3:
        for livro in biblioteca:
            if livro != None:
                if livro['disponivel'] == False:

                    if livro['nome_leitor'] == "":
                        livro['nome_leitor'] = "Nenhum"

                    print(f"ID: {livro['id_livro']} | Titulo: '{livro['titulo']}' | Disponível?: {colored(livro['disponivel'], "red")} | Leitor: {livro['nome_leitor']}")
                    print("")



# Função que muda o estado do livro e regista o nome do leitor
def emprestar_livro(biblioteca):
    idLivro = int(input("Escreva o id do livro: "))
    nome = input("Escreva o nome do leitor: ")

    for livro in biblioteca:
        if livro != None:
            if livro['id_livro'] == idLivro:
                livro['disponivel'] = False
                livro['nome_leitor'] = nome
                cprint("Sucesso", "green")
                return
    print("")
    cprint(f"Não existe um livro com o id {idLivro}", "red")


#Função que torna o livro disponível e apaga o nome do leitor
def devolver_livro(biblioteca):
    idLivro = int(input("Qual o id do livro?: "))

    for livro in biblioteca:
        if livro != None:
            if livro['id_livro'] == idLivro:
                livro['disponivel'] = True
                livro['nome_leitor'] = ""
                cprint("Sucesso", "green")
                return
    print("")
    cprint(f"Não existe um livro com o id {idLivro}", "red")


#Função que apresenta as opções ao utilizador e devolve a sua escolha
def menu():

    selecao = 0

    while selecao > 4 or selecao < 1:
        print("")
        print("1 - Adicionar livro")
        print("2 - Listar livros")
        print("3 - Tornar estado do livro como Emprestado")
        print("4 - Tornar estado do livro como Devolvido")
        print("")
    
        selecao = int(input(""))
        print("")

        if selecao > 4 or selecao < 1:
            cprint("Seleção inválida!", "red")

    return selecao


#função para gerar (seed) dados iniciais
def inicializar(livros):
    livros[0]={"id_livro":1,"titulo": "Dom Quixote", "disponivel": True,"nome_leitor":""}
    livros[1]={"id_livro":2,"titulo": "A Arte da Guerra", "disponivel": True,"nome_leitor":""}
    livros[2]={"id_livro":3,"titulo": "1984", "disponivel": True,"nome_leitor":""}
    livros[3]={"id_livro":4,"titulo": "Os Lusíadas", "disponivel": True,"nome_leitor":""}
    livros[4]={"id_livro":5,"titulo": "A Metamorfose", "disponivel": True,"nome_leitor":""}
    return 5


def main():
    MAX_ITEMS=100
    livros =np.empty(MAX_ITEMS,dtype=object)
    nr_livros=inicializar(livros)
    
    while True:
        selecao = menu()

        if selecao == 1:
            adicionar_livro(livros, nr_livros)
            nr_livros += 1

        if selecao == 2:
            listar_livros(livros, nr_livros)

        if selecao == 3:
            emprestar_livro(livros)

        if selecao == 4:
            devolver_livro(livros)

    #continuar aqui

# Ponto de entrada do programa (main loop)
if __name__ == "__main__":
    main()