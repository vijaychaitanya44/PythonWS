class Base:

    def base_method(self):
        print("Base class")


class Child(Base):
    company = "Automation"
    def child_method(self):

        print("I m in child class")


c =Child()
b= Base()


c.child_method()
c.base_method()

print(c.company)
