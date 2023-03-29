import pygame

pygame.init()


screen = pygame.display.set_mode([500, 500])
screen_rect = screen.get_rect()

platform = pygame.image.load("images/land.png")
platform_rect = platform.get_rect()
platform = pygame.transform.scale(platform, (2*screen_rect.width, platform_rect.height))
platform_rect = platform.get_rect()
# platform_rect.y = screen_rect.height - platform_rect.height
# platform_rect.x = screen_rect.width//2 - platform_rect.width//2
platform_rect.midbottom = screen_rect.midbottom

def platform_move():
	platform_rect.x -= 5
	if platform_rect.centerx <= 0:
		platform_rect.left = screen_rect.left


bird = pygame.image.load("images/bird.png")
bird_rect = bird.get_rect()
bird_rect.center = screen_rect.center


pipe = pygame.Rect(0, 0, 0.15*screen_rect.width, 0.4*screen_rect.height)
pipe.topright = screen_rect.topright

def pipe_move():
	pipe.x -= 5
	if pipe.right <= 0:
		pipe.left = screen_rect.right

pipe2 = None




def mainloop():

	while True:
		screen.fill([107, 52, 235]) #RGB -> Green
		screen.blit(platform, platform_rect)
		platform_move()

		screen.blit(bird, bird_rect)		

		pygame.draw.rect(screen, (0, 200, 0), pipe)
		pipe_move()

		pygame.time.Clock().tick(25)
		pygame.display.flip()

		for every_event in pygame.event.get():
			if every_event.type == pygame.QUIT:
				pygame.quit()

mainloop()

