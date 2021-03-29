d = {}
try:
    # from helloe import njsnfßß

    class student:
        def input(self):
            self.name = input("enter student name\n")
            if not self.name:
                raise Exception("you pressed enter without adding anything")
            self.address = input("enter address\n")
            self.semester = int(input("enter semester as a number\n"))
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
                raise recordnotfounderror("RECORD NOT FOUND")
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

            # st.search(name)
            for i in d:
                if i == name:
                    no = int(input("enter the subject you want to modify"))
                    marks = int(input("enter modified marks"))
                    d[i][marks][no] == marks
                    total = total+ma
                    percent = (total/250)*100
            print(d)
        elif ch == 0:
            break
    print(d)

except ValueError:
    print("STRING ENTERED WHERE INTEGER WAS EXPECTED")
except IndentationError:
    print("indentation error")
except NameError:

    print("the defined variable is not defined anywhere")
except ModuleNotFoundError:
    print("current module not found")
except ImportError:
    print("module not properly imported Raised when the import statement has troubles trying to load a module")
except IndexError:
    print("wrong index position reached")
except KeyboardInterrupt:
    print("interrupt happened because somethin unusual pressed")
except Exception as e1:
    print(e1)
except KeyError:
    print("key not present in the dictionary")
except MemoryError:
    print("Memory Error is raised when an operation does not get enough memory to process further.")
except recordnotfounderror as e:
    print("RECORD NOT FOUND", e.data)

print("thank you for using student mangement system")
