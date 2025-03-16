import time
import sqlite3

class student():
    def __init__(self,name,surname,gender,age):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.age = age

    def __str__(self):
        return "Student info;\nName: {}\nSurname: {}\nGender: {}\nAge: {}".format(self.name,self.surname,self.gender,self.age)

class Class1():
    def __init__(self):
        self.connecting()

    def connecting(self):
        self.connection = sqlite3.connect("Classes.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Class_1 (Name TEXT,Surname TEXT,Gender TEXT,Age INT)")
        self.connection.commit()

    def deconnnecting(self):
        self.connection.close()

    def showStudents(self):
        self.cursor.execute("Select * From Class_1")
        students = self.cursor.fetchall()
        if not students:
            print("There is 0 students in this class...")
        else:
            for i in students:
                person = student(i[0],i[1],i[2],i[3])
                print(person)
                print("\n")

    def addStudents(self, person):
        self.cursor.execute("SELECT COUNT(*) FROM Class_1")
        student_count = self.cursor.fetchone()[0]
        if student_count < 5:
            self.cursor.execute("INSERT INTO Class_1 VALUES(?,?,?,?)",
                                (person.name, person.surname, person.gender, person.age))
            self.connection.commit()
            print("Student added successfully...")
        else:
            print("This class is full...")

    def removeStudents(self,person):
        self.cursor.execute("DELETE FROM Class_1 WHERE Name = ?",(person,))
        self.connection.commit()
        print("Student removed successfully...")

    def changeClass(self, person):
        classes = ["Class_1", "Class_2", "Class_3", "Class_4"]
        found_class = None
        student = None

        for class_name in classes:
            self.cursor.execute(f"SELECT * FROM {class_name} WHERE Name = ?", (person,))
            student = self.cursor.fetchone()
            if student:
                found_class = class_name
                break

        if not student:
            print("Student not found in any class.")
            return

        choice = int(input("Which class do you want to move this person to? (1-4): "))

        if choice < 1 or choice > 4:
            print("This class does not exist...")
            return

        target_class = f"Class_{choice}"

        self.cursor.execute(f"SELECT COUNT(*) FROM {target_class}")
        student_count = self.cursor.fetchone()[0]

        if student_count >= 5:
            print("This class is full...")
            return

        self.cursor.execute(f"INSERT INTO {target_class} (Name, Surname, Gender, Age) VALUES (?, ?, ?, ?)",
                            (student[0], student[1], student[2], student[3]))

        self.cursor.execute(f"DELETE FROM {found_class} WHERE Name = ?", (person,))

        self.connection.commit()

        print(f"Student moved to {target_class} successfully!")

class Class2():
    def __init__(self):
        self.connecting()

    def connecting(self):
        self.connection = sqlite3.connect("Classes.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Class_2 (Name TEXT,Surname TEXT,Gender TEXT,Age INT)")
        self.connection.commit()

    def deconnnecting(self):
        self.connection.close()

    def showStudents(self):
        self.cursor.execute("Select * From Class_2")
        students = self.cursor.fetchall()
        if not students:
            print("There is 0 students in this class...")
        else:
            for i in students:
                person = student(i[0],i[1],i[2],i[3])
                print(person)
                print("\n")

    def addStudents(self, person):
        self.cursor.execute("SELECT COUNT(*) FROM Class_2")
        student_count = self.cursor.fetchone()[0]
        if student_count < 5:
            self.cursor.execute("INSERT INTO Class_2 VALUES(?,?,?,?)",
                                (person.name, person.surname, person.gender, person.age))
            self.connection.commit()
            print("Student added successfully...")
        else:
            print("This class is full...")

    def removeStudents(self,person):
        self.cursor.execute("DELETE FROM Class_2 WHERE Name = ?",(person,))
        self.connection.commit()
        print("Student removed successfully...")

    def changeClass(self, person):
        classes = ["Class_1", "Class_2", "Class_3", "Class_4"]
        found_class = None
        student = None

        for class_name in classes:
            self.cursor.execute(f"SELECT * FROM {class_name} WHERE Name = ?", (person,))
            student = self.cursor.fetchone()
            if student:
                found_class = class_name
                break

        if not student:
            print("Student not found in any class.")
            return

        choice = int(input("Which class do you want to move this person to? (1-4): "))

        if choice < 1 or choice > 4:
            print("This class does not exist...")
            return

        target_class = f"Class_{choice}"

        self.cursor.execute(f"SELECT COUNT(*) FROM {target_class}")
        student_count = self.cursor.fetchone()[0]

        if student_count >= 5:
            print("This class is full...")
            return

        self.cursor.execute(f"INSERT INTO {target_class} (Name, Surname, Gender, Age) VALUES (?, ?, ?, ?)",
                            (student[0], student[1], student[2], student[3]))

        self.cursor.execute(f"DELETE FROM {found_class} WHERE Name = ?", (person,))

        self.connection.commit()

        print(f"Student moved to {target_class} successfully!")

class Class3():
    def __init__(self):
        self.connecting()

    def connecting(self):
        self.connection = sqlite3.connect("Classes.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Class_3 (Name TEXT,Surname TEXT,Gender TEXT,Age INT)")
        self.connection.commit()

    def deconnnecting(self):
        self.connection.close()

    def showStudents(self):
        self.cursor.execute("Select * From Class_3")
        students = self.cursor.fetchall()
        if not students:
            print("There is 0 students in this class...")
        else:
            for i in students:
                person = student(i[0],i[1],i[2],i[3])
                print(person)
                print("\n")

    def addStudents(self, person):
        self.cursor.execute("SELECT COUNT(*) FROM Class_3")
        student_count = self.cursor.fetchone()[0]
        if student_count < 5:
            self.cursor.execute("INSERT INTO Class_3 VALUES(?,?,?,?)",
                                (person.name, person.surname, person.gender, person.age))
            self.connection.commit()
            print("Student added successfully...")
        else:
            print("This class is full...")

    def removeStudents(self,person):
        self.cursor.execute("DELETE FROM Class_3 WHERE Name = ?",(person,))
        self.connection.commit()
        print("Student removed successfully...")

    def changeClass(self, person):
        classes = ["Class_1", "Class_2", "Class_3", "Class_4"]
        found_class = None
        student = None

        for class_name in classes:
            self.cursor.execute(f"SELECT * FROM {class_name} WHERE Name = ?", (person,))
            student = self.cursor.fetchone()
            if student:
                found_class = class_name
                break

        if not student:
            print("Student not found in any class.")
            return

        choice = int(input("Which class do you want to move this person to? (1-4): "))

        if choice < 1 or choice > 4:
            print("This class does not exist...")
            return

        target_class = f"Class_{choice}"

        self.cursor.execute(f"SELECT COUNT(*) FROM {target_class}")
        student_count = self.cursor.fetchone()[0]

        if student_count >= 5:
            print("This class is full...")
            return

        self.cursor.execute(f"INSERT INTO {target_class} (Name, Surname, Gender, Age) VALUES (?, ?, ?, ?)",
                            (student[0], student[1], student[2], student[3]))

        self.cursor.execute(f"DELETE FROM {found_class} WHERE Name = ?", (person,))

        self.connection.commit()

        print(f"Student moved to {target_class} successfully!")

class Class4():
    def __init__(self):
        self.connecting()

    def connecting(self):
        self.connection = sqlite3.connect("Classes.db")
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Class_4 (Name TEXT,Surname TEXT,Gender TEXT,Age INT)")
        self.connection.commit()

    def deconnnecting(self):
        self.connection.close()

    def showStudents(self):
        self.cursor.execute("Select * From Class_4")
        students = self.cursor.fetchall()
        if not students:
            print("There is 0 students in this class...")
        else:
            for i in students:
                person = student(i[0],i[1],i[2],i[3])
                print(person)
                print("\n")

    def addStudents(self, person):
        self.cursor.execute("SELECT COUNT(*) FROM Class_4")
        student_count = self.cursor.fetchone()[0]
        if student_count < 5:
            self.cursor.execute("INSERT INTO Class_4 VALUES(?,?,?,?)",
                                (person.name, person.surname, person.gender, person.age))
            self.connection.commit()
            print("Student added successfully...")
        else:
            print("This class is full...")

    def removeStudents(self,person):
        self.cursor.execute("DELETE FROM Class_4 WHERE Name = ?",(person,))
        self.connection.commit()
        print("Student removed successfully...")

    def changeClass(self, person):
        classes = ["Class_1", "Class_2", "Class_3", "Class_4"]
        found_class = None
        student = None

        for class_name in classes:
            self.cursor.execute(f"SELECT * FROM {class_name} WHERE Name = ?", (person,))
            student = self.cursor.fetchone()
            if student:
                found_class = class_name
                break

        if not student:
            print("Student not found in any class.")
            return


        choice = int(input("Which class do you want to move this person to? (1-4): "))

        if choice < 1 or choice > 4:
            print("This class does not exist...")
            return

        target_class = f"Class_{choice}"

        self.cursor.execute(f"SELECT COUNT(*) FROM {target_class}")
        student_count = self.cursor.fetchone()[0]

        if student_count >= 5:
            print("This class is full...")
            return

        self.cursor.execute(f"INSERT INTO {target_class} (Name, Surname, Gender, Age) VALUES (?, ?, ?, ?)",
                            (student[0], student[1], student[2], student[3]))

        self.cursor.execute(f"DELETE FROM {found_class} WHERE Name = ?", (person,))

        self.connection.commit()

        print(f"Student moved to {target_class} successfully!")

























