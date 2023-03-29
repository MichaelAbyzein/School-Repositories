
class Dog:
    
    name = "Moly"
    age = 0
    isCute = True
    

moly = Dog() # moly =. object / instance
             # Dog() =. class / template
             
# print(moly)
print(moly.name)
print(moly.age)
print(moly.isCute)

goly = Dog()

print(goly.name)
print(goly.age)
print(goly.isCute)

moly.age += 1
print(goly.age) # 0/1 ?
print(moly.age)