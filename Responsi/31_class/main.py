
class MyApp:
#function / method -> (self)
#self.[obj] -> semua object bisa dipakai ke semua function
	def __init__(self, color):
		self.color = color

	def run(self):
		print(self.color)
		print("ok")

class App2:
	def __init__(self, color):
		MyApp.__init__(self, color) #copy paste dari class yang beda

	def run(self):
		print("!!")

if __name__ == '__main__':
	App = App2('green')
	App.run()