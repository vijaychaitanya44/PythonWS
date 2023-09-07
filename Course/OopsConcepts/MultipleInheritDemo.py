class classA:
    def methodA(self):
        print("Class A method")

    def helloWorld(self):
        print("hello world classA")

class classB:
    def methodB(self):
        print("Class B method")

    def helloWorld(self):
        print("Hello world Class B")

class classC(classA,classB):
    def methodC(self):
        print("Class C method")
   


c = classC()

c.methodA()
c.methodC()
c.methodB()
c.helloWorld()
print(classC.__mro__)



