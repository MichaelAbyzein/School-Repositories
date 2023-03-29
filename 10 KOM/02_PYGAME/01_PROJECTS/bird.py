import pygame

class Birb():

	image = pygame.image.load("images/bird.png")
	rect = image.get_rect()
	fly = False
	pass_pipe = False

	def __init__(self, game):
		self.settings = game.settings
		self.screen = game.screen
		self.screen_rect = game.screen_rect

		self.rect.center = self.screen_rect.center

	#@classmethod
	def move(self):
		if self.fly:
			self.rect.y -= self.settings.bird_fly_speed
		else:
			self.rect.y += self.settings.bird_fall_speed

	#@classmethod
	def show(self):
		self.screen.blit(self.image, self.rect)