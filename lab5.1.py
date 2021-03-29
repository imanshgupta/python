class STUDENT(object):
    def __init__(self, USN, NAME, AGE):
        self.USN = USN
        self.NAME = NAME
        self.AGE = AGE

    def display(self):
        print(self.USN)
        print(self.NAME)
        print(self.AGE)


class UGSTUDENT(STUDENT):
    def __init__(self):
        USN = input("enter your usn number")
        NAME = input("enter your name")
        AGE = input("enter your age")
        self.SEMESTER = input("enter semester")
        self.FEES = int(input("enter fees"))
        self.STIPEND = int(input("enter stipend"))
        STUDENT.__init__(self, USN, NAME, AGE)
        STUDENT.display(self)
        UGSTUDENT.display(self)

    def display(self):
        print(self.SEMESTER)
        print(self.FEES)
        print(self.STIPEND)


class PGSTUDENT(STUDENT):
    def __init__(self):
        USN = input("enter your usn number")
        NAME = input("enter your name")
        AGE = input("enter your age")
        self.SEMESTER = input("enter semester")
        self.FEES = int(input("enter fees"))
        self.STIPEND = int(input("enter stipend"))
        STUDENT.__init__(self, USN, NAME, AGE)
        STUDENT.display(self)
        PGSTUDENT.display(self)

    def display(self):
        print(self.SEMESTER)
        print(self.FEES)
        print(self.STIPEND)


while True:
    print("1-if a ug student \n 2-if a pg student")
    ch = int(input("enter a choice"))
    if not(ch):
        print("enter choice is empty")
    else:
        if ch == 1:
            ug = UGSTUDENT()
        elif ch == 2:
            pg = PGSTUDENT()
        else:
            print("wrong choice entered")
            break
