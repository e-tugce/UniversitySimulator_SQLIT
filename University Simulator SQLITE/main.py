import sqlite3

class University:
    def __init__(self,name,country):
        self.name = name
        self.country = country
        self.status = True

        self.connectDatabase()

    def run(self):
        self.menu()

        choice = self.choice()

        if choice == 1:
            self.addStudent()
        if choice==2:
            self.deleteStudent()
        if choice ==3:
            self.updateStudent()
        if choice ==4:
            while True:
                try:
                    orderby = int(input("1) Faculty\n2) Department\n3) Type\n4) Status\n5) All\nSelect: "))
                    if orderby<1 or orderby>5:
                        continue
                    break
                except ValueError:
                    print("It must be an integer!")

            self.showAllStudents(orderby)

        if choice==5:
            self.systemExit()

    def menu(self):
        print("***** {} Administration System *****".format(self.name))
        print("\n1) Add Student\n2) Delete Student\n3) Update Student\n4) Show Student\n5) Exit\n")

    def choice(self):
        while True:
            try:
                choice = int(input("Select: "))
                if choice<1 or choice>5:
                   print("Operation number must be between 1-5. Please select correct number!")
                   continue
                break
            except ValueError:
                print("Operation must be an integer number. Please write correct type.")

        return choice

    def addStudent(self):
        print("*** Student Information ***")

        name = input("Student's Name: ").lower().capitalize()
        surname = input("Student's Surname: ").lower().capitalize()
        faculty = input("Student's Faculty: ").lower().capitalize()
        department = input("Student's Department: ").lower().capitalize()
        stid = int(input("Student's ID: "))
        while True:
            try:
                typ = int(input("Student's Education Type (Normal/Evening): "))
                if typ<1 or typ>2:
                    print("Student's Education Type must be 1  or 2.")
                    continue
                break
            except ValueError:
                print("Type must be integer(1 or 2)\n")

        status = "Active"

        self.cursor.execute("INSERT INTO Students VALUES('{}','{}','{}','{}','{}',{},'{}')".format(name,surname,faculty,department,stid,typ,status))

        self.connect.commit()

        print("The student named {} {} has been successfully added.".format(name,surname))


    def deleteStudent(self):
        self.cursor.execute("SELECT * FROM Students")

        allStudents = self.cursor.fetchall()
        convertAllStr = lambda x: [str(y) for y in x]
        for i,j in enumerate(allStudents,1):
            print("{}) {} ".format(i," ".join(convertAllStr(j))))

        while True:
            try:
                select = int(input("Select the student to be deleted: "))
                break
            except ValueError:
                print("Please write correct type(int).")

        self.cursor.execute("DELETE FROM Students WHERE rowid={}".format(select))
        self.connect.commit()

        print("\nStudent is successfully deleted.")


    def updateStudent(self):
        self.cursor.execute("SELECT * FROM Students")

        allStudents = self.cursor.fetchall()
        convertAllStr = lambda x: [str(y) for y in x]
        for i, j in enumerate(allStudents, 1):
            print("{}) {} ".format(i, " ".join(convertAllStr(j))))

        while True:
            try:
                select = int(input("\nSelect the student to be updated: "))
                break
            except ValueError:
                print("Please write correct type(int).")

        while True:
            try:
                updateSelect = int(input("1) Name\n2) Surname\n3) Faculty\n4) Department\n5) Student ID\n6) Education Type(Normal/Evening)\n7) Status\nSelect: "))
                if updateSelect<1 or updateSelect>7:
                    continue
                break
            except ValueError:
                print("It must be an integer!")

        operations = ["name","surname","faculty","department","stid","typ","status"]

        if updateSelect == 6:
            while True:
                try:
                    newValue = int(input("Enter the new value: "))
                    if newValue not in (1,2):
                        continue
                    break
                except ValueError:
                    print("It must be an integer!\n")

            self.cursor.execute("UPDATE Students SET typ={} WHERE rowid={}".format(newValue,select))
        else:
            newValue = input("Enter the new value: ")
            self.cursor.execute("UPDATE Students SET {}='{}' WHERE rowid={}".format(operations[updateSelect-1],newValue,select))

        self.connect.commit()
        print("It is been successfully updated!")

    def showAllStudents(self,by):
        if by == 5:
            self.cursor.execute("SELECT * FROM Students")

            allStudents = self.cursor.fetchall()
            convertAllStr = lambda x: [str(y) for y in x]
            for i, j in enumerate(allStudents, 1):
                print("{}) {} ".format(i, " ".join(convertAllStr(j))))

        if by ==1 :
            self.cursor.execute("SELECT faculty FROM Students")

            faculties = list(enumerate(list(set(self.cursor.fetchall())),1))
            for i,j in faculties:
                print("{}) {}".format(i,j[0]))

            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("It must be an integer!")

            self.cursor.execute("SELECT * FROM Students WHERE faculty='{}'".format(faculties[select - 1][1][0]))

            allStudents = self.cursor.fetchall()
            convertAllStr = lambda x: [str(y) for y in x]
            for i, j in enumerate(allStudents, 1):
                print("{}) {} ".format(i, " ".join(convertAllStr(j))))


        if by == 2:
            self.cursor.execute("SELECT department FROM Students")

            departments = list(enumerate(list(set(self.cursor.fetchall())), 1))
            for i, j in departments:
                print("{}) {}".format(i, j[0]))

            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("It must be an integer!")

            self.cursor.execute("SELECT * FROM Students WHERE department='{}'".format(departments[select - 1][1][0]))

            allStudents = self.cursor.fetchall()
            convertAllStr = lambda x: [str(y) for y in x]
            for i, j in enumerate(allStudents, 1):
                print("{}) {} ".format(i, " ".join(convertAllStr(j))))

        if by == 3:
            self.cursor.execute("SELECT typ FROM Students")

            types = list(enumerate(list(set(self.cursor.fetchall())), 1))
            for i, j in types:
                print("{}) {}".format(i, j[0]))

            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("It must be an integer!")

            self.cursor.execute("SELECT * FROM Students WHERE typ='{}'".format(types[select - 1][1][0]))

            allStudents = self.cursor.fetchall()
            convertAllStr = lambda x: [str(y) for y in x]
            for i, j in enumerate(allStudents, 1):
                print("{}) {} ".format(i, " ".join(convertAllStr(j))))

        if by == 4:
            self.cursor.execute("SELECT status FROM Students")

            statuss = list(enumerate(list(set(self.cursor.fetchall())), 1))
            for i, j in statuss:
                print("{}) {}".format(i, j[0]))

            while True:
                try:
                    select = int(input("\nSelect: "))
                    break
                except ValueError:
                    print("It must be an integer!")

            self.cursor.execute("SELECT * FROM Students WHERE status='{}'".format(statuss[select - 1][1][0]))

            allStudents = self.cursor.fetchall()
            convertAllStr = lambda x: [str(y) for y in x]
            for i, j in enumerate(allStudents, 1):
                print("{}) {} ".format(i, " ".join(convertAllStr(j))))


    def systemExit(self):
        self.status = False

    def connectDatabase(self):
        self.connect = sqlite3.connect("university.db")
        self.cursor = self.connect.cursor()

        self.cursor.execute("CREATE TABLE IF NOT EXISTS Students(name TEXT,surname TEXT,faculty TEXT,department TEXT,stid TEXT,typ INT,status TEXT)")

        self.connect.commit()

ODTU = University("Orta Dogu Teknik Universitesi","Turkiye")

while ODTU.status:
    ODTU.run()