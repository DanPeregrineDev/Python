def isPalindromo(word):
    inverted = ""
    for letter in word:
        inverted = letter + inverted
    inverted = inverted.lower()
    word = word.lower()
    if word == inverted:
        return True
    else:
        return False

def main():
    UserInput = input("Escreva a palavra: ")
    print(isPalindromo(UserInput))

if __name__ == "__main__":
    main()