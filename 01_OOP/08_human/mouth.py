from random import choice

class Mouth:
    def __init__(self, InfoHuman):
        self.sex = InfoHuman.sex
        self.number = 1
        self.teeths = 20
        self.has_toothache = choice([True, False])
        self.is_Clean = True
        
    def describe_sex(self):
        print(f"I'm a {self.sex}")