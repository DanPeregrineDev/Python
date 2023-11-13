Word = "Banana"
UserWord = "-" * len(Word)
Lives = 7

while Lives > 0:
    acertou = False
    if Word != UserWord:
        UserLetter = input("Letra: ")
    UserLetter = UserLetter.lower()

    Temp = ""

    for i in range(len(Word)):
        if UserLetter ==  Word[i]:
            Temp += UserLetter
            acertou = True
        else:
            Temp += UserWord[i]

        if Word == UserWord:
            print("Parabens acertou a palavra!")
            break
    if Word == UserWord:
        break
    
    UserWord = Temp

    if acertou == False:
        Lives -= 1

    print(UserWord)
    print(f"Tentativas restantes {Lives}")

if Lives <= 0:
    print(f"Ficou sem vidas! A palavra era: {Word}")