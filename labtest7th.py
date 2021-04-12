class employee:
    def __init__(self, first, last, empid, pay):
        self.first = first
        self.last = last
        self.empid = empid
        self.pay = pay

    def rais(self):
        raiseamt = 1.04
        self.pay = int(self.pay*raiseamt)
        return self.pay

    def display(self):
        print("First name:", self.first)
        print("Last name:", self.last)
        print("Employee Id:", self.empid)
        print("Pay:", self.pay)


class developer(employee):
    def rais(self):
        raiseamt = 1.05
        self.pay = int(self.pay*raiseamt)
        return self.pay


class manager(employee):
    def rais(self):
        raiseamt = 1.06
        self.pay = int(self.pay*raiseamt)
        return self.pay


while True:
    print("1:Developer employee details:")
    print("2:Manager employee details:")
    print("3:CLICK 0 TO EXIT")
    choice = int(input("Enter your choice:"))
    first = input("Enter your first name :")
    last = input("Enter your last name :")
    empid = input("Enter your id :")
    try:
        pay = int(input("Enter your pay :"))
    except Exception:
        print("Pay is not integer type")
    if choice == 1:
        developer_object = developer(first, last, empid, pay)
        print("Initial pay of developer:", developer_object.pay)
        print("Pay of developer after applying raise",
              developer_object.rais())
        print("Manager employee details:", developer_object.display())
    elif choice == 2:
        emp2 = manager(first, last, empid, pay)
        print("Initial pay of developer:", emp2.pay)
        print("Pay of developer after applying raise", emp2.rais())
        print("Manager employee details:", emp2.display())
    elif choice == 0:
        break
