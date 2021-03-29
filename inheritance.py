"""class vehicle(object):
    def __init__(self, veh, color):
        self.veh = veh
        self.color = color

    def display(self):
        print(self.veh)
        print(self.color)


class car(vehicle):
    def __init__(self, veh, color, brand, size):
        self.brand = brand
        self.size = size
        # to call constructor of the parent class
        vehicle.__init__(self, veh, color)
        # super(car,self).__init__()
        # super().__init__()

    def display(self):
        vehicle.display(self)
        print(self.brand)
        print(self.size)


ob = car("vehicle", "white", "maruti", "big")
ob.display()
ob1 = car("veh", "wh", "ma", "b")
ob1.display()

--------------------------------------------
#mutiple inheritance
class parent1:
    def method1(self):
        print("call to parent 1")
class parent2(parent1):
    def method1(self):
        print("call to parent 2")
class child(parent2):
    ob=child()
    ob.method1()#to show that call to parent 1 is done which is in oreder from top

-----------
"""

# public private and protected class variables and functions


class ppp:
    name = "ansh"  # public
    _rollno = 74  # private
    __sex = "male"  # protected

    def hi(self):  # public fun
        pass

    def _protected(self):  # protected fun
        pass

    def __private(self):  # private fun
        pass
