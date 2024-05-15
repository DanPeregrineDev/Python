import utils, os

FILE_NAME = "tasks.txt"

def add():
    task = input("Tarefa: ")
    date = input("Data: ")
    
    with open(FILE_NAME, 'a', encoding='UTF-8') as file:
        file.write(f"{task};{date}\n")

    print("Tarefa registada com sucesso")


def listTasks():
    if os.path.exists(FILE_NAME) == False:
        print("Sem tarefas")
        return
    
    t = 1
    
    with open(FILE_NAME, 'r', encoding='UTF-8') as file:
        print("-" * 60)
        while True:
            line = file.readline()

            if not line:
                break

            line = line.split(';')
            print(f"{t} - {line[0]} | {line[1]}", end="")
            print("-" * 60)

            t = t + 1


def remove():
    if os.path.exists(FILE_NAME) == False:
        print("Sem tarefas")
        return
    
    number = int(input("Numero da tarefa para remover: ")) - 1

    with open(FILE_NAME, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    with open(FILE_NAME, 'w', encoding='UTF-8') as file:
        for i in range(len(lines)):
            if i != number:
                file.write(lines[i])
    
    print("Tarefa removida com sucesso")


def markAsCompleted():
    if os.path.exists(FILE_NAME) == False:
        print("Sem tarefas")
        return


def main():
    while True:
        option = utils.showmenu("Menu", ["Adicionar", "Listar", "Remover", "Marcar como concluída", "Terminar"])

        if option == 1:
            add()
        if option == 2:
            listTasks()
        if option == 3:
            remove()
        if option == 4:
            markAsCompleted()
        if option == 5:
            break

if __name__ == "__main__":
    main()