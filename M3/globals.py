Nome = "Joaquim"
X = 0
Y = 0
R = 0

def Cumprimentar():
    print(f"Bom dia {Nome}!")

def Somar():
    R = X + Y
    X = 0

def main():
    Cumprimentar()
    Y = 5
    X = 10
    Somar()
    print(R)

if __name__ == "__main__":
    main()