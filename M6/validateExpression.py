UserInput = input("Escreva a expressão: ")

parenteses = 0
parentesesRetos = 0
parentesesCoiso = 0

for i in UserInput:
    if i == "(" or i == ")":
        parenteses += 1
    if i == "[" or i == "]":
        parentesesRetos += 1
    if i == "{" or i == "}":
        parentesesCoiso += 1

if parenteses % 2 != 0:
    print("Invalida")

if parentesesRetos % 2 != 0:
    print("Invalida")

if parentesesCoiso % 2 != 0:
    print("Invalida")

Abriu = False
AbriuReto = False
AbriuCoiso = False

Fechou = False
FechouReto = False
FechouCoiso = False

for i in UserInput:
    if i == "]" and AbriuReto != True:
        print("Invalida")
        break
    if i == ")" and Abriu != True:
        print("Invalida")
        break
    if i == "}" and AbriuCoiso != True:
        print("Invalida")
        break
    if i == "(":
        Abriu = True
    if i == "[":
        AbriuReto = True
    if i == "{":
        AbriuCoiso = True