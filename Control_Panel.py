from Class import *

print("""
****************************************

WELCOME TO CLASS CONTROL PANEL

THERE IS THE FUNCTION LIST OF THIS PANEL

1. SHOW STUDENTS
2. ADD STUDENT
3. REMOVE STUDENT
4. CHANGE CLASS
5. PRESS 'q' TO QUIT 

****************************************
""")

class_1 = Class1()
class_2 = Class2()
class_3 = Class3()
class_4 = Class4()

while True:

    class_choice = input("Which class you want to organize?")

    if(class_choice == "1"):
        func_choice = input("Which funtion you want to use?")

        if(func_choice == "q"):
            print("Thanks for using control panel...")
            break
        elif(func_choice == "1"):
            class_1.showStudents()
        elif(func_choice == "2"):
            name = input("Name : ")
            surname = input("Surname : ")
            gender = input("Gender : ")
            age = input("Age : ")

            new_person = student(name, surname, gender, age)

            class_1.addStudents(new_person)
        elif(func_choice == "3"):
            removedStudent = input("Which student you want to remove?")
            class_1.removeStudents(removedStudent)
        elif(func_choice == "4"):
            changedClass = input("Which student you want to change class?")
            class_1.changeClass(changedClass)
        else:
            print("Wrong input...")

    elif (class_choice == "2"):
        func_choice = input("Which funtion you want to use?")

        if (func_choice == "q"):
            print("Thanks for using control panel...")
            break
        elif (func_choice == "1"):
            class_2.showStudents()
        elif (func_choice == "2"):
            name = input("Name : ")
            surname = input("Surname : ")
            gender = input("Gender : ")
            age = input("Age : ")

            new_person = student(name, surname, gender, age)

            class_2.addStudents(new_person)
        elif (func_choice == "3"):
            removedStudent = input("Which student you want to remove?")
            class_2.removeStudents(removedStudent)
        elif (func_choice == "4"):
            changedClass = input("Which student you want to change class?")
            class_2.changeClass(changedClass)
        else:
            print("Wrong input...")

    elif (class_choice == "3"):
        func_choice = input("Which funtion you want to use?")

        if (func_choice == "q"):
            print("Thanks for using control panel...")
            break
        elif (func_choice == "1"):
            class_3.showStudents()
        elif (func_choice == "2"):
            name = input("Name : ")
            surname = input("Surname : ")
            gender = input("Gender : ")
            age = input("Age : ")

            new_person = student(name, surname, gender, age)

            class_3.addStudents(new_person)
        elif (func_choice == "3"):
            removedStudent = input("Which student you want to remove?")
            class_3.removeStudents(removedStudent)
        elif (func_choice == "4"):
            changedClass = input("Which student you want to change class?")
            class_3.changeClass(changedClass)
        else:
            print("Wrong input...")

    elif (class_choice == "4"):
        func_choice = input("Which funtion you want to use?")

        if (func_choice == "q"):
            print("Thanks for using control panel...")
            break
        elif (func_choice == "1"):
            class_4.showStudents()
        elif (func_choice == "2"):
            name = input("Name : ")
            surname = input("Surname : ")
            gender = input("Gender : ")
            age = input("Age : ")

            new_person = student(name, surname, gender, age)

            class_4.addStudents(new_person)
        elif (func_choice == "3"):
            removedStudent = input("Which student you want to remove?")
            class_4.removeStudents(removedStudent)
        elif (func_choice == "4"):
            changedClass = input("Which student you want to change class?")
            class_4.changeClass(changedClass)
        else:
            print("Wrong input...")
