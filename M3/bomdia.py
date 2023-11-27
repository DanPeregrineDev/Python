def PerguntarNome():
    Nome = input("Qual é o seu nome?: ")
    return Nome

def Cumprimentar(Nome):
    print(f"Bom dia {Nome}!")

def main():
    Cumprimentar(PerguntarNome())

if __name__ == "__main__":
    main()