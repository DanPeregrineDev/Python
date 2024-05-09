"""
    Por Daniel Madeira
"""
import os
import utils

data = 'appData.txt'

def addTask():
    taskDescription = input("Descrição da tarefa: ")
    taskDate = input("Data de conclusão da tarefa: ")

    with open(data, 'a', encoding='UTF-8') as file:
        file.write(f"{taskDescription};{taskDate}\n")


def listTasks():

    t = 0

    with open(data, 'r', encoding='UTF-8') as file:
        while True:
            task = file.readline()

            if not task:
                break

            task = task.split(';')

            print("-" * 60)
            print(f"{t + 1} - {task[0]} | {task[1]}")

            t += 1


def listCompleted():
    t = 0

    with open(data, 'r', encoding='UTF-8') as file:
        while True:
            task = file.readline()

            if not task:
                break

            task = task.split(';')

            if "[Concluida]" in task[0]:
                print("-" * 60)
                print(f"{t + 1} - {task[0]} | {task[1]}")

                t += 1


def listMonth():
    month = input("Escreva o mês da tarefa: ")

    t = 0

    with open(data, 'r', encoding='UTF-8') as file:
        while True:
            task = file.readline()

            if not task:
                break

            task = task.split(';')

            if month in task[1]:
                print("-" * 60)
                print(f"{t + 1} - {task[0]} | {task[1]}")

                t += 1


def removeTask():
    if os.path.exists(data) == False:
        print("Sem dados")
        return
    
    taskNumber = int(input("Numero da tarefa: "))

    with open(data, 'r', encoding='UTF-8') as readFile:
        with open("temp.txt", 'w', encoding='UTF-8') as tempFile:
            t = 1
            while True:
                line = readFile.readline()

                if not line:
                    break

                if t != taskNumber:
                    tempFile.write(line)

                t += 1

    os.remove(data)
    os.rename("temp.txt", data)


def markAsCompleted():
    if os.path.exists(data) == False:
        print("Sem dados")
        return
    
    taskNumber = int(input("Numero da tarefa: "))

    with open(data, 'r', encoding='UTF-8') as readFile:
        with open('temp.txt', 'w', encoding='UTF-8') as tempFile:
            t = 1
            while True:
                line = readFile.readline()

                if not line:
                    break

                line = line.split(';')

                if t == taskNumber:
                    line[0] = f"{"[Concluida]" + line[0]}"
                
                tempFile.write(f"{line[0]};{line[1]}")

                t += 1

    os.remove(data)
    os.rename('temp.txt', data)


def main():
    while True:
        option = utils.showMenu("Menu Principal", ["Adicionar Tarefa", "Listar Tarefas", "Listar Tarefas Concluidas", "Listar Tarefas de um determinado mês", "Remover Tarefa", "Marcar tarefa como concluída", "Sair"])

        if option == 1:
            addTask()
        if option == 2:
            listTasks()
        if option == 3:
            listCompleted()
        if option == 4:
            listMonth()
        if option == 5:
            removeTask()
        if option == 6:
            markAsCompleted()
        if option == 7:
            break

if __name__ == "__main__":
    main()