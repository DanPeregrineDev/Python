def Listar(mesas):
    # Listar as mesas livres
    print("Lista de mesas livres: ")
    for m in range(len(mesas)):
        if mesas[m] == 0:
            print(m + 1)

    # Listar as mesas ocupadas
    print("Lista de mesas ocupadas")
    for m in range(len(mesas)):
        if mesas[m] != 0:
            print(m + 1)

def main():
    NR_MESAS = 6
    mesas = np.zeros(NR_Mesas, 'i')
    
    # -----Menu-----

    while True:
        op = menu()
        if op == "1":
            Entrada(mesas)
        elif op == "2":
            Saida(mesas)
        elif op == "3":
            Listar(mesas)
        elif op == "4":
            break
        else:

if __name__ == "__main__":
    main()