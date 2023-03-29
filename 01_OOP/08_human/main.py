from random import choice

from head import Head
    
class Human:

    def __init__(self, name):
        
        self.name = name
        self.age = 0
        self.sex = choice(["Male", "Female"])
        self.head= Head(self)
    
    def describe_me(self):
        print(f"Hello, I'm {self.name} and now I'm {self.age} years old.")
        
hubert = Human(name="hubert")
hubert.head.mouth.describe_sex()