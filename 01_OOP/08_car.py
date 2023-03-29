#inheritance

class Car:
    def __init__(self, make, model, year, color, new, manual):
        
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.new = new
        self.manual = manual
        self.odometer = 0
        
    def get_desc(self):
        return f"This car is a {self.make}'s car.\nIts models is {self.model}-{self.year}.\nIt has {self.color} color."
        
    def increment_odometer(self, kms):
        self.odometer += kms
        print(f"The odometer has been updated to {self.odometer} kms.")
        
    def fill_gas_tank(self):
        print("The car is full of fuel now!")
        
    def change_color(self, new_color):
        self.color = new_color
        print(f"The color has been updated to {self.color}.")
        
class ElectricCar(Car):
    def __init__(self, *args, **kwargs):
        #super().__init__(*args, **kwargs)
        Car.__init__(self, *args, **kwargs)
    
    
    #def __init__(self, make, model, year, color, new, manual):
    #super().__init__(make, model, year, color, new, manual)
    
    def fill_gas_tank(self):
        print("This car doesn't need gas...") # overwrite
        
    def charge_battery(self):
        print("This car has been fully charged.")
        
class ElectricBus(ElectricCar):
    
    def __init__(self, capacity, *args, **kwargs):
        ElectricCar.__init__(self, *args, **kwargs)
        self.capacity = capacity

    def adding_passenger(self):
        print(f"Adding {self.capacity} Passenger to {self.make}...")
        
hyundai = ElectricCar("hyundai", "kona-ev", 2021, "white", True, False)
print(hyundai.get_desc())
hyundai.increment_odometer(200)
hyundai.change_color("green")
hyundai.fill_gas_tank()
hyundai.charge_battery()
volvo = ElectricBus(68, "volvo-7900", "hybrid", 2011, "green", False, True)
volvo.adding_passenger()
        
#toyota = Car("toyota", "yaris", 2020, "red", True, True)
#print(toyota.get_desc())
#toyota.increment_odometer(1000)
#toyota.fill_gas_tank()
#toyota.change_color("grey")



