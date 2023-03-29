"""

Human -> Head -> Eye (jumlah=2, warna pupil="biru"), Mouth, Nose
      -> Body -> Leg (kiri dan kanan), Hand, Torso
"""
from random import choice

class Eye:
    def __init__(self):
        self.number = 2
        self.color = "grey"
        self.is_Big = True
    
class Mouth:
    def __init__(self):
        self.number = 1
        self.teeths = 20
        self.has_toothache = choice([True, False])
        self.is_Clean = True

class Head:
    def __init__(self):
        self.eyes = Eye()
        self.mouth = Mouth()

class Human:

    def __init__(self, name):
        
        self.name = name
        self.age = 0
        self.sex = choice(["Man", "Female"])
        self.head= Head()
    
    def describe_me(self):
        print(f"Hello, I'm {self.name} and now I'm {self.age} years old.")
        
hubert = Human(name="hubert")
stan = Human(name="stan")
print(stan.head.eyes.number)
print(stan.head.mouth.has_toothache)

hubert.describe_me()
stan.describe_me()