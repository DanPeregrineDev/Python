"""
    Um programa para gerir uma agenda de contatos com um ficheiro binario
    Foncionalidades:
        - Adicionar Contato
        - Editar Contato
        - Remover Contato
        - Listar Contatos
    Dados:
        - Nome[100 Bytes]
        - Idade[4 Bytes]
        - Email[64 Bytes]
        - Telefone[9 Bytes]
"""

import struct, os
import utils

def add():
    name = input("Nome do contacto: ")
    age = int(input("Idade do contacto: "))
    email = input("Email do contacto: ")
    phone = input("Numero de telefone do contacto: ")

    with open('data.dat', 'ab') as file:
        file.write(struct.pack('100s', name.encode('UTF-8')))
        file.write(struct.pack('i', age))
        file.write(struct.pack('64s', email.encode('UTF-8')))
        file.write(struct.pack('9s', phone.encode('UTF-8')))

    print("Successfully added contact")


def list():
    if not os.path.exists('data.dat'):
        print("No contacts")
        return
    
    option = utils.showmenu("List Menu", ["List All", "List Specific", "Return"])

    if option == 1:
        with open('data.dat', 'rb') as file:
            print("=" * 60)

            while True:
                # Read name (100 bytes)
                name = file.read(100)
                if not name:
                    break
                name = name.split(b'\x00', 1)[0].decode('utf-8')
                print("Name:", name)

                # Read age (4 bytes)
                age_bytes = file.read(4)
                age = struct.unpack('i', age_bytes)[0]
                print("Age:", age)

                # Read email (64 bytes)
                email = file.read(64)
                email = email.split(b'\x00', 1)[0].decode('utf-8')
                print("Email:", email)

                # Read phone (9 bytes)
                phone = file.read(9)
                phone = phone.split(b'\x00', 1)[0].decode('utf-8')
                print("Phone:", phone)

                print('-' * 60)
    
    if option == 2:
        with open('data.dat', 'rb') as file:
            position = int(input("Contact number: "))
            position = (position - 1) * 177

            file.seek(position)

            # Read name (100 bytes)
            name = file.read(100)
            if not name:
                print("Not found")
                return
            name = name.split(b'\x00', 1)[0].decode('utf-8')
            print("Name:", name)

            # Read age (4 bytes)
            age_bytes = file.read(4)
            age = struct.unpack('i', age_bytes)[0]
            print("Age:", age)

            # Read email (64 bytes)
            email = file.read(64)
            email = email.split(b'\x00', 1)[0].decode('utf-8')
            print("Email:", email)

            # Read phone (9 bytes)
            phone = file.read(9)
            phone = phone.split(b'\x00', 1)[0].decode('utf-8')
            print("Phone:", phone)
    
    if option == 3:
        return


def main():
    while True:
        option = utils.showmenu("Main menu", ["Add contact", "Edit Contact", "Remove Contact", "List Contacts", "Exit"])

        if option == 1:
            add()
        if option == 4:
            list()
        if option == 5:
            break

if __name__ == "__main__":
    main()