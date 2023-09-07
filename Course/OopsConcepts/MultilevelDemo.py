class Apple:
    def hello_A(self):
        print("Apple method")
    def hello_world(self):
        print("Hello world from class A")

class Baloon(Apple):
    def hello_B(self):
        print("Baloon method")
    def hello_world(self):
        print("Hello world from class B")

class CaterPillar(Baloon):
    def hello_C(self):
        print("Cataz method")


c = CaterPillar()

c.hello_C()
c.hello_B()
c.hello_A()
c.hello_world()