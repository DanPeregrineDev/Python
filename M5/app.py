
# Função que permite ao utilizador adicionar um livro
# O livro novo estará sempre disponivel
# Verifique se ainda existe espaço no array antes de adicionar
# Tenha atenção para não repetir o id do livro
def adicionar_livro(livros):
    titulo = input("Escreva o titulo do livro: ")
    
    if len(livros) > 0:
        id_livro = livros[len(livros) - 1]["id_livro"] + 1
    else:
        id_livro = 1
    
    novo = {'id_livro': id_livro, 'titulo': titulo, 'disponivel': True, 'nome_leitor': ""}
    livros.append(novo)

# Função para mostrar os livros
# deve permitir escolher se lista todos ou só os disponíveis ou só os indisponíveis
def listar_livros(livros):
    op = input("1 - Listar todos\n2 - Listar disponíveis\n3 - Listar indesponíveis")

    for livro in livros:
        if op == "1" or (op == "2" and livro["disponivel"] == True) or (op == "3" and livro["disponivel"] == False):
            for chave, valor in livro.items():
                print(f"{chave}{valor}")
            
            print("#" * 20)

# Função que muda o estado do livro e regista o nome do leitor
def emprestar_livro(livros):
    # Ler o id_livro a emprestar
    id_livro = int(input("Qual o id do livro emprestar: "))

    # Procurar livro
    for livro in livros:
        # Se existir ler o nome do leitor e alterar o estado
        if id_livro == livro["id_livro"]:
            if livro["disponivel"] == False:
                print("Livro esta emprestado")
                return
            nome = input("Qual o leitor: ")
            livro["nome_leitor"] = nome
            livro["disponivel"] = False
            return
        print("Esse id de livro nao existe")

#Função que torna o livro disponível e apaga o nome do leitor
def devolver_livro(livros):
    # Ler o id_livro a devolver
    id_livro = int(input("Qual o id do livro a devolver: "))

    # Procurar livro
    for livro in livros:
        # Se existir ler alterar o estado
        if id_livro == livro["id_livro"]:
            if livro["disponivel"] == True:
                print("Livro ja foi devolvido")
                return
            livro["nome_leitor"] = ""
            livro["disponivel"] = True
            return
        print("Esse id de livro nao existe")

#Função que apresenta as opções ao utilizador e devolve a sua escolha
def menu():
    while True:
        print("1 - Adicionar\n2 - Listar\n3 - Emprestar\n4 - Devolver\n5 - Sair")
        op = int(input("\n> "))
        if op <1 or op >5:
            print("Essa opção não é válida")
        else:
            return op

#função para gerar (seed) dados iniciais
def inicializar(livros):
    livros.append({"id_livro":1,"titulo": "Dom Quixote", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":2,"titulo": "A Arte da Guerra", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":3,"titulo": "1984", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":4,"titulo": "Os Lusíadas", "disponivel": True,"nome_leitor":""})
    livros.append({"id_livro":5,"titulo": "A Metamorfose", "disponivel": True,"nome_leitor":""})

def main():
    livros = []
    inicializar(livros)

    op = 0

    while op != 5:
        op = menu()

        if op == 1:
            adicionar_livro(livros)

        if op == 2:
            listar_livros(livros)

        if op == 3:
            emprestar_livro(livros)

        if op == 4:
            devolver_livro(livros)

# Ponto de entrada do programa (main loop)
if __name__ == "__main__":
    main()
