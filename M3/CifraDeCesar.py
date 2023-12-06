def Decifrador(word):
    code = word.upper()
    FinalWord = ""
    for letter in code:
        currentLetter = ord(letter)
        currentLetter -= 1
        if currentLetter == 64:
            currentLetter = 90
        newLetter = chr(currentLetter)
        FinalWord = FinalWord + newLetter
    return FinalWord

def Codificador(code):
    code = code.upper()
    FinalWord = ""
    for letter in code:
        currentLetter = ord(letter)
        currentLetter += 1
        if currentLetter == 91:
            currentLetter = 65
        newLetter = chr(currentLetter)
        FinalWord = FinalWord + newLetter
    return FinalWord

def main():
    print("1 - Decifrar")
    print("2 - Codificar")
    print("-------------")
    Selection = int(input("Selecione a opção: "))

    if Selection == 1:
        UserInput = input("Escreva a palavra: ")
        print(Decifrador(UserInput))
    if Selection == 2:
        UserInput = input("Escreva a palavra: ")
        print(Codificador(UserInput))

if __name__ == "__main__":
    main()