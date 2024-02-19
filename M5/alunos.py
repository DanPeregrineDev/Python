import numpy

def menu():
    print("")
    print("1 - Search a student")
    print("2 - Add a student")
    print("3 - Change student data")
    print("4 - Add student grades")
    print("5 - Remove student") #TODO maybe
    print("")

    selection = int(input("> "))
    print("")

    if selection > 5 or selection < 1:
        print("")
        print("Invalid selection")
        menu()
    
    return selection

def searchStudent(students, nStudents, name):
    for i in range(nStudents):
        if students[i]["name"] == name:
            return students[i]
    return None

def addStudent():
    name = input("Student's name: ")
    age = input("Student's age: ")
    address = input("Student's address: ")
    email = input("Student's email: ")

    studentData = {"name": name, "age": age, "address": address, "email": email}

    return studentData

def main():
    MAX_STUDENTS = 100
    students = numpy.zeros(MAX_STUDENTS, dtype = object)
    nStudents = 0

    while True:
        selection = menu()

        if nStudents == MAX_STUDENTS:
            continue

        if selection == 1:
            toSearch = input("Student's name: ")
            toSearch = toSearch.capitalize()
            print("")
            result = searchStudent(students, nStudents, toSearch)

            if result != None:
                print(result)
            else:
                print("Not found!")

        if selection == 2:
            students[nStudents] = addStudent()

            nStudents += 1

        if selection == 3:
            toChange = input("Student's name: ")
            student = searchStudent(students, nStudents, toChange)
            if student is not None:
                student["age"] = input("Type the student's new age: ")
                student["address"] = input("Type the student's new address: ")
                student["email"] = input("Type the student's new email: ")

        if selection == 4:
            toAddGrades = input("Student's name: ")
            grade = int(input("Student's grade: "))
            grades = numpy.zeros((MAX_STUDENTS, 1), 'U50')
            for student in range(MAX_STUDENTS):
                if grades[student, 0] == 0:
                    grades[student, 0] = toAddGrades
                    grades[student, 1] = grade
        
        if selection == 5:
            print(grades)

if __name__ == "__main__":
    main()

#TODO NOT FINISHED