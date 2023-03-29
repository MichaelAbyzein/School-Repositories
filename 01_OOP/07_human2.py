from random import choice

class Eye:
    def __init__(self):
        self.number = 2
        self.color = "grey"
        self.is_Big = True
    
class Mouth:
    def __init__(self, InfoHuman):
        self.sex = InfoHuman.sex
        self.number = 1
        self.teeths = 20
        self.has_toothache = choice([True, False])
        self.is_Clean = True
        
    def describe_sex(self):
        print(f"I'm a {self.sex}")

class Head:
    def __init__(self, InfoHuman):
        self.eyes = Eye()
        self.mouth = Mouth(InfoHuman)

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