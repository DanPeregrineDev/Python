import sys

if len(sys.argv) != 3:
    print("Erro: tem de indicar 2 argumentos")
    sys.exit()

for values in sys.argv:
    print(values)

firstArg = sys.argv[1]
secondArg = sys.argv[2]
print(firstArg, secondArg)