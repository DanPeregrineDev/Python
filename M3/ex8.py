import mdc
import sys

if len(sys.argv) != 3:
    print("Erro: tem de indicar 2 argumentos")
    sys.exit()

N1 = int(sys.argv[1])
N2 = int(sys.argv[2])

print(mdc.mdc(N1, N2))