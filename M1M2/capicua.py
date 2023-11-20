UserInput = input("Escreva uma palavra: ")
TransformedWord = ""

# Validation

# Not required

# Operation

for i in range(len(UserInput)-1, -1, -1):
    TransformedWord = TransformedWord + UserInput[i]

if UserInput == TransformedWord:
    print("É uma capicua")
else:
    print("Não é uma capicua")

print(TransformedWord)