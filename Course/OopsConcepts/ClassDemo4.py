class Person:

    def __init__(self):
        pass
    def __init__(self, f, l):
        self.fname =f
        self.lname=l
        print("Hello Person "+self.fname+" "+self.lname)

    def sum(self,*args):
        sum=0
        for n in args:
            sum =sum+n
        return sum


x= Person("Vijay","Chaitanya")

print(Person.sum(x,6,1,7,8,90,12))

#y= Person("Ajay","Ghosh")

