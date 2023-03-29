
class Dog:

    owner = "Anta" # attribute di luar init ini di miliki oleh setiap attributes.
    
    def __init__(self, name): #fungsi konstruktor
        self.name = name
        self.age = 0 # starting age
        self.isCute = True
    

moly = Dog(name = "Moly") # moly =. object / instance
             # Dog() =. class / template
             
# print(moly)
print(moly.name)
print(moly.age)
print(moly.isCute)

goly = Dog(name="Goly")

print(goly.name)
print(goly.age)
print(goly.isCute)

Dog.owner = "Claude"
print(goly.owner)
print(moly.owner)

Dog.name = "Doly"
print(goly.name)