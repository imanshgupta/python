class Abc:

    def fun(self,a):
        return a*a
    
    def fun(self,a,b):
        return a*a*a

object1= Abc()
a=int(input("enter a number"))
b=object1.fun(a)
print("answer is {}".format(a))