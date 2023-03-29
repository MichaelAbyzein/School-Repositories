
class Car:

    def __init__(self, name, type, color, time, owner, made_by):
        self.name = name
        self.type = type
        self.color = color
        self.time = time
        self.owner = owner
        self.made_by = made_by
        
    def get_descriptive(self):
        print(f"{self.name} is a {self.type} car, made by {self.made_by} in {self.time}. This one has a {self.color} with it's current owner is {self.owner}")

inv = Car("Innova Venturer", "Commercial", "Silver", 2016, 'Steve', "Toyota")
fer = Car("Ferrari 458", "Sport", "Red", 2010, 'John', "Ferrari")
panther = Car("Panther", "Commercial-Use", "Brown", 2011, 'Steve', "Isuzu")
inv.get_descriptive()
fer.get_descriptive()
panther.get_descriptive()