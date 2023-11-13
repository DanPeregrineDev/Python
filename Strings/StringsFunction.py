from string import punctuation

Frase = input("Frase: ")

for i in range(len(Frase)):
    # Is alphanumeric abc
    if Frase[i].isalpha():
        print("Is Alpha")
    # Is a number 123
    if Frase[i].isdigit():
        print("Is Digit")
    # Is a space " "
    if Frase[i].isspace():
        print("Is Space")
    # Is a punctuation !?.,
    if Frase[i] in punctuation:
        print("Is punctiation")