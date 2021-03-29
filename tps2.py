d = dict()


class student:
    def input(self):
        self.name = input("enter student name\n")
        self.address = input("enter address\n")
        self.semester = input("enter semester\n")
        self.total = 0
        self.marks = []
        self.grade = ""
        self.percent = 0
        for m in range(0, 5):
            ma = int(input("enter marks"))
            self.marks.append(ma)
            self.total = self.total+ma
        self.percent = (self.total/250)*100

        if self.percent > 80:
            self.grade = "A"
        elif self.percent > 60 and self.percent < 80:
            self.grade = "B"
        else:
            self.grade = "C"
        self.update()

    def update(self):
        '''d.update({self.name: {
            "name": self.name,
            "address": self.address,
            "semester": self.semester,
            "marks": self.marks,
            "total": self.total,
            "percent": self.percent,
            "grade": self.grade
        }})'''
        d[self.name] = self.__dict__

    def search(self, name):
        flag = 0
        for key in d:
            if key == name:
                print("employee found")
                for i in d[key]:
                    print(i, d[key][i])
                    flag = 1
        if flag == 0:
            print("no record found")

    def printstu(self):
        for key in d:
            print(key, d[key])


st = student()
while True:
    ch = int(input(
        "\n 1 to add student \n 2 - print all student \n 3 - find a student by name \n 0-exit \n"))
    if ch == 1:
        st.input()
    elif ch == 2:
        st.printstu()
    elif ch == 3:
        name = input("enter the name of the employee to be searched")
        st.search(name)

    elif ch == 0:
        break

print("thank you for using student mangement system")
