class Person:

    population = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.population += 1

    @classmethod
    def get_population(self):
        print(Person.population)

schumander = Person("Schumander", 27) # "Salamader are finger lickin good" - Colonel Sanders at his visit at the Yellowstone National Park, 1932
# print(Person.population)
# print(schumander.population)

Person.get_population()
schumander.get_population()