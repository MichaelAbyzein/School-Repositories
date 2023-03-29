class Person:

    def __init__(self, name, age):
            self.name = name
            self.age = age

    def display_name(self):
        print(f"My name is {self.name}")

    def isAdultInst(self):
        return self.age >=18

    @staticmethod
    def isAdult(age):
        return age >=18

schumander = Person("Schumander", 17)

print(Person.isAdult(20))
# print(Person.isAdultInst())
print(schumander.isAdult(10))
schumander.display_name()