import numpy

nMax = int(input("Numero máximo de contactos: "))

contactos = numpy.zeros((nMax, 2), 'U50')

def verContactos():
    print(contactos)

def adicionarContactos(nome, nTelm):

    nome = nome.capitalize()
    
    for l in range(nMax):
        if contactos[l, 0] != "":
            continue
        else:
            contactos[l, 0] = nome
            contactos[l, 1] = nTelm
            return
    print("")
    print("A agenda está cheia!")

def procurarContacto(nome):

    nome = nome.capitalize()

    for l in range(nMax):
        if contactos[l, 0] == nome:
            print(contactos[l, 1])
    print("")
    print("Contacto não encontrado!")

def alterarContactos(nome, nTelm):

    nome = nome.capitalize()

    for l in range(nMax):
        if contactos[l, 0] == nome:
            contactos[l, 1] = nTelm
            return
    print("")
    print("Contacto não encontrado!")

def removerContactos(nome):

    nome = nome.capitalize()

    if nome == "Cancelar":
        return
    
    for l in range(nMax):
        if contactos[l, 0] == nome:
            contactos[l, 0] = ""
            contactos[l, 1] = ""
            return
    print("")
    print("Contacto não encontrado!")

def main():
    while True:
        print("")
        print("1 - Ver contactos")
        print("2 - Procurar contacto")
        print("3 - Adicionar contactos")
        print("4 - Alterar contacto")
        print("5 - Remover contacto")
        print("")

        selection = int(input(""))

        if selection == 1:
            verContactos()

        if selection == 2:
            nome = input("Escreva o nome do contacto: ")
            procurarContacto(nome)

        if selection == 3:
            nome = input("Escreva o nome do contacto: ")
            nTelm = int(input("Escreva o numero de telemóvel do contacto: "))
            adicionarContactos(nome, nTelm)

        if selection == 4:
            nome = input("Escreva o nome do contacto que deseja alterar (Escreva 'Cancelar' para cancelar): ")

            if nome.capitalize() == "Cancelar":
                continue

            nTelm = int(input("Escreva o novo numero de telefone: "))
            alterarContactos(nome, nTelm)

        if selection == 5:
            nome = input("Escreva o nome do contacto que deseja remover (Escreva 'Cancelar' para cancelar): ")
            removerContactos(nome)

if __name__ == "__main__":
    main()