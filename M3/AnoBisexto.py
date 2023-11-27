def Bisexto(Ano):
    if (Ano % 4 == 0 and Ano % 100 != 0) or Ano % 400 == 0:
        return True
    else:
        return False

def main():
    UserInput = int(input("Ano: "))
    print(Bisexto(UserInput))

if __name__ == "__main__":
    main()