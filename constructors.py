class Abc:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def add(self):
        print(self.x+self.y)
ob=Abc(5,6)
ob.add()



class Cal(Abc):
    ob=Abc(5,5)
    ob.add()




