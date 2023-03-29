
class Unicycle:
	def __init__(self, name, color, made):
		self.name = name
		self.color = color
		self.made = made 

	def describe(self):
		print(f"This is a {self.name} unicycle. The color of it is {self.color}, and it's made by {self.made}.")

class Bicycle(Unicycle):
	def __init__(self, price, speed, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.price = price
		self.speed = speed
	def describe(self):
		print(f"This is {self.name} bicycle. It is made by {self.made}, with a price of $ {self.price}, and its color is {self.color}. It has a speed of {self.speed} km/h.")
	def change_color(self, new_color):
		self.color = new_color
		print(f"Successfully painted to {self.color}.")

class MotorCycle(Bicycle):
	def __init__(self, owner, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.owner = owner
	def describe(self):
		print(f"This is {self.name} motorcycle. It is made by {self.made}, with {self.color} as it color and with a speed of {self.speed} km/h. It has a price of $ {self.price} and its owner is {self.owner}.")
	def filling_fuel(self):
		print("This motorcycle doesn't need any fuel, its still full.")

takuya = Unicycle('takuya', 'blue', 'dasuka')
bmx = Bicycle('200', '12', 'bmx', 'red', 'united bike')
gsx3000 = MotorCycle('gerald', '210', '35', 'gsx-3000', 'black', 'suzuki')

takuya.describe()
bmx.describe()
bmx.change_color('grey')
gsx3000.describe()
gsx3000.filling_fuel()
gsx3000.change_color('blue')



