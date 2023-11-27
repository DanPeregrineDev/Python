def PerguntarNome():
    nome = input("Qual é o seu nome?: ")
    return nome

def Cumprimentar():
    print("Bom dia!")

def main():
    PerguntarNome()
    Cumprimentar()

if __name__ == "__main__":
    main()