import pygame
import sys

class Screen:
	width = 500
	height = 500

	bg_color = (0, 255, 0)

	screen = pygame.display.set_mode((width, height))

	@classmethod
	def show(self):
		self.screen.fill(self.bg_color)

class Game:
	pygame.init()

	@classmethod
	def run(self):
		while True:
			Screen.show()
			pygame.display.flip()
			pygame.time.Clock().tick(25)

			self.add_event_listener()

	@classmethod
	def add_event_listener(self):
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()

if __name__ == '__main__':
	Game.run()