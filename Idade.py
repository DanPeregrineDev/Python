Age = input("Escreva a sua idade: ")

# Validation
if Age.isdigit() == False:
    print("A idade intruduzida está invalida")

Age = int(Age)

if Age < 0 or Age > 120:
    print("A idade intruduzida está invalida")

# Operation

if Age <= 11:
    print("Está na Infância")
elif Age > 11 and Age <= 20:
    print("Está na Adolescência")
elif Age > 20 and Age <= 74:
    print("É Adulto")
elif Age > 74 and Age <= 120:
    print("Está na velhice")