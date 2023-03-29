
class Restaurant:
    
    def __init__(self, name, type, take_away=True):
        self.name = name
        self.type = type
        self.take_away = take_away
        
    def desc(self):
        print(f"{self.name} is serving {self.type} food.")
        
    def serve(self, ticknum):
        print(f"Now serving customer : {ticknum}.")
    
pizhut = Restaurant("Pizza Hut", "Russian (lol)")
sederhana = Restaurant("Sederhana", "Padang", False)
mcd = Restaurant("MCD", "Western")

pizhut.desc()
sederhana.desc()

pizhut.serve(21)
mcd.serve(212)