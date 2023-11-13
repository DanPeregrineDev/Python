# Daniel Madeira
# Exercicio 5

N = int(input("Escreva um numero inteiro: "))

while N < 0:
    N = int(input("Não pode ser menor que 0, escreva novamente: "))

if N % 2 == 0:
    print("É par")
elif N % 2 != 0:
    print("É ímpar")