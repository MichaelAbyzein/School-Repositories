
class Dog:

    owner = "Anta" # attribute di luar init ini di miliki oleh setiap attributes.
    
    def __init__(self, name): #fungsi konstruktor
        self.name = name
        self.age = 0 # starting age (month)
        self.isCute = True
        
    def sit(self):
        print(f"{self.name} is sitting right now")
        
    def roll_over(self):
        print(f"{self.name} rolled over")
        
    def sleep(self):
        print(f'{self.name} : "zzzzzz"')
    
    def increase_age(self, month):
        self.age += month
        
        # variable, lists, dict dkk -> attribute
        # functiomn -> method / ability

moly = Dog(name = "Moly") # moly =. object / instance
             # Dog() =. class / template
             
moly.sit()
moly.roll_over()
moly.sleep()

moly.increase_age(11)
print(moly.increase_age())