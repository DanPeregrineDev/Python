#Daniel M. Nº4

import os, pickle
import utils

FILE_NAME = 'data.pkl'

def add():
    with open(FILE_NAME, 'ab') as file:
        veiculo = {
            'matricula': input("Matrícula: ").upper(),
            'marca': input("Marca: ").capitalize(),
            'modelo': input("Modelo: "),
            'anoFabrico': utils.intInput("Ano de fabrico: ")
        }

        pickle.dump(veiculo, file)

        print("Adicionado com sucesso!")


def list():
    if os.path.exists(FILE_NAME) == False:
        print("Sem veículos")
        return

    with open(FILE_NAME, 'rb') as file:
        t = 1

        while True:
            try:
                veiculos = pickle.load(file)

                print(f"{t} - {veiculos['matricula']} | {veiculos['modelo']} | {veiculos['marca']} | {veiculos['anoFabrico']}")
                
                t = t + 1

            except EOFError:
                break


def listMoreThan10YearsOld():
    if os.path.exists(FILE_NAME) == False:
        print("Sem veículos")
        return
    
    with open(FILE_NAME, 'rb') as file:
        foundAnything = False
        t = 1

        while True:
            try:
                veiculos = pickle.load(file)

                if (2024 - veiculos['anoFabrico']) >= 10:
                    print(f"{t} - {veiculos['matricula']} | {veiculos['modelo']} | {veiculos['marca']} | {veiculos['anoFabrico']}")
                    foundAnything = True

                t = t + 1

            except EOFError:
                break
    
    if foundAnything == False:
        print(f"Nenhum veículo com mais de 10 anos não encontrado!")


def showBrandWithMoreVehicles():
    if os.path.exists(FILE_NAME) == False:
        print("Sem veiculos")
        return
    
    with open(FILE_NAME, 'rb') as file:
        brands = {}

        while True:
            try:
                veiculos = pickle.load(file)

                if veiculos['marca'] not in brands.keys():
                    brands[f'{veiculos['marca']}'] = 1
                else:
                    brands[f'{veiculos['marca']}'] += 1
            
            except EOFError:
                break

    t1 = 0
    t2 = ""

    for brand, quantity in brands.items():
        if quantity >= t1:
            t1 = quantity
            t2 = brand
    
    print(f"{t2} - {t1}")


def search():
    if os.path.exists(FILE_NAME) == False:
        print("Sem veículos")
        return
    
    toSearch = input("Marca: ").capitalize()

    with open(FILE_NAME, 'rb') as file:
        foundAnything = False
        t = 1

        while True:
            try:
                veiculos = pickle.load(file)

                if veiculos['marca'] == toSearch:
                    print(f"{t} - {veiculos['matricula']} | {veiculos['modelo']} | {veiculos['marca']} | {veiculos['anoFabrico']}")
                    foundAnything = True

                    t = t + 1

            except EOFError:
                break

    if foundAnything == False:
        print(f"Veículo com a marca {toSearch} não encontrado!")


def remove():
    if os.path.exists(FILE_NAME) == False:
        print("Sem veículos")
        return
    
    toRemove = input("Matricula: ").upper()
    
    with open(FILE_NAME, 'rb') as rFile:
        removed = 0

        with open('temp.dat', 'wb') as wFile:
            while True:
                try:
                    veiculo = pickle.load(rFile)

                    if veiculo['matricula'] != toRemove:
                        pickle.dump(veiculo, wFile)
                    else:
                        removed = removed + 1
                
                except EOFError:
                    break

    os.remove(FILE_NAME)
    os.rename('temp.dat', FILE_NAME)

    if removed == 0:
        print(f"Nenhum carro com a matrícula {toRemove} encontrado")
    else:
        print(f"Foram removidos {removed} veículos")


def main():
    while True:
        option = utils.showmenu("Main menu", ["Adicionar", "Listar", "Listar com mais de 10 anos", "Mostrar marca com mais veiculos", "Pesquisar", "Remover", "Sair"])

        if option == 1:
            add()
        if option == 2:
            list()
        if option == 3:
            listMoreThan10YearsOld() # Bonus
        if option == 4:
            showBrandWithMoreVehicles() # Bonus
        if option == 5:
            search()
        if option == 6:
            remove()
        if option == 7:
            break

if __name__ == "__main__":
    main()