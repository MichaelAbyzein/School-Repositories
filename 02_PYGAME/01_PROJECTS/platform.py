import pygame

class Platform():

	def __init__(self, game):
		self.settings = game.settings
		self.screen = game.screen
		self.screen_rect = game.screen_rect

		self.image = pygame.transform.scale(pygame.image.load("images/land.png"), (2*self.screen_rect.width, self.screen_rect.height//5))
		self.rect = self.image.get_rect()

		self.rect.midbottom = self.screen_rect.midbottom

	def move(self):
		self.rect.x -= self.settings.land_speed
		if self.rect.centerx <= 0:
			self.rect.left = self.screen_rect.left

	def show(self):
		self.screen.blit(self.image, self.rect)