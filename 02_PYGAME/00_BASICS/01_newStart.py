import pygame
import sys
from random import randint
from random import choice

pygame.init()

screen = pygame.display.set_mode((500, 500))
screen_rect = screen.get_rect()

platform = pygame.image.load("images/land.png")
platform_rect = platform.get_rect()
platform = pygame.transform.scale(platform, (2*screen_rect.width, platform_rect.height))
platform_rect = platform.get_rect()
# platform_rect.x = (screen_rect.width // 2) - (platform_rect.width // 2)
# platform_rect.y = screen_rect.height - platform_rect.height
platform_rect.midbottom = screen_rect.midbottom

def platform_move():
	platform_rect.x -= 5
	if platform_rect.centerx <= 0:
		platform_rect.left = screen_rect.left

def pipe_move():
	global bird_pass_pipe, screen_rect, platform_rect, pipe, pipe_2
	pipe.x -= 5
	pipe_2.x -= 5
	if pipe.right <= 0:
		pipe_2.height = platform_rect.height + (0.1*screen_rect.height) + choice([0, 50, 100, 150, 200]) #randint(50, 100)
		pipe.height = screen_rect.height - pipe_2.height - (0.2*screen_rect.height)

		pipe = pygame.Rect(0, 0, pipe.width, pipe.height)
		pipe_2 = pygame.Rect(0, 0, pipe_2.width, pipe_2.height)

		#pipe.left = screen_rect.right
		#pipe_2.left = screen_rect.right
		pipe.topleft = screen_rect.topright
		pipe_2.bottomleft = screen_rect.bottomright
		bird_pass_pipe = False
	pipe_head.midbottom = pipe.midbottom
	pipe_head2.midtop = pipe_2.midtop

def bird_move():
	global bird_fly
	if bird_fly:
		bird_rect.y -= 5
	else:
		bird_rect.y += 2

bird_pass_pipe = False

score_num = 0
def check_point():
	global pipe, bird_rect, score_num, bird_pass_pipe, score_label_image
	if (pipe.centerx <= bird_rect.centerx) and not bird_pass_pipe:
		score_num += 1
		score_label_image = score_label.render(f"Score : {score_num}", True, (255, 255, 255))
		bird_pass_pipe = True

def pipe_collision():
	global pipe, pipe2, pipe_head, pipe_head2, bird, health_amount, start, score_num

	collide_top_edge = bird_rect.y <= 0
	collide_pipe = bird_rect.colliderect(pipe)
	collide_pipe_head = bird_rect.colliderect(pipe_head)
	collide_pipe2 = bird_rect.colliderect(pipe_2)
	collide_pipe_head2 = bird_rect.colliderect(pipe_head2)
	collide_platform = bird_rect.colliderect(platform_rect)

	if collide_pipe or collide_pipe_head or collide_pipe2 or collide_pipe_head2 or collide_platform or collide_top_edge:
		health_amount -= 1
		score_num -= 1
		start = False
		sys.exit()
		return True
	return


start = False

def event_listener():
	global bird_fly, play_button_rect, start
	for every_event in pygame.event.get():
		if every_event.type == pygame.QUIT:
			pygame.quit()

		elif every_event.type == pygame.KEYDOWN:
			if every_event.key == pygame.K_SPACE:
				bird_fly = True

		elif every_event.type == pygame.KEYUP:
			if every_event.key == pygame.K_SPACE:
				bird_fly = False

		elif every_event.type == pygame.MOUSEBUTTONDOWN:
			mouse_position = pygame.mouse.get_pos()
			# print(mouse_position)
			if play_button_rect.collidepoint(mouse_position) and not start:
				start = True
				# print(start)

play_button = pygame.image.load("images/play_button.png")
play_button_rect = play_button.get_rect()
play_button = pygame.transform.scale(play_button, (0.1 * play_button_rect.width, 0.1 * play_button_rect.height))
play_button_rect = play_button.get_rect()
play_button_rect.center = screen_rect.center
play_button_rect.y += screen_rect.height//10

title_label = pygame.font.Font("fonts/BirdyGame.ttf", 40)
title_label_image = title_label.render("Flappy Bird", True, (255, 255, 255))
title_label_image_rect = title_label_image.get_rect()
title_label_image_rect.center = screen_rect.center
title_label_image_rect.y -= screen_rect.height//10

score_label = pygame.font.Font("fonts/BirdyGame.ttf", 20)
score_label_image = score_label.render(f"Score : {score_num}", True, (255, 255, 255))
score_label_image_rect = score_label_image.get_rect()
score_label_image_rect.topleft = screen_rect.topleft
score_label_image_rect.x += 10
score_label_image_rect.y += 10

health_amount = 1

health = {
	"image" : pygame.transform.scale(pygame.image.load("images/hearthealth.png"), (32, 32))
}

health["rect"] = health["image"].get_rect()

healths = [ health for _ in range(health_amount) ]

def health_pos():
	global health, health_amount, healths
	counter, health_width = 0, health['rect'].width
	if health_amount > 0:
		for health in healths:
			health['rect'].topright = screen_rect.topright
			health['rect'].x -= (10*(counter+1)) + (health['rect'].width*(counter))
			health['rect'].y += 10
			counter += 1
			screen.blit(health["image"], health["rect"])


bird = pygame.image.load("images/bird.png")
bird_rect = bird.get_rect()
bird_rect.center = screen_rect.center

bird_fly = False

pipe = pygame.Rect(0, 100, 0.15*screen_rect.width, 0.4*screen_rect.height)
pipe.topright = screen_rect.topright
pipe_head = pygame.Rect(0, 0, 1.2*pipe.width, 0.15*pipe.height)
pipe_head.midbottom = pipe.midbottom

pipe_2 = pygame.Rect(0, 100, 0.15*screen_rect.width, 0.4*screen_rect.height)
pipe_head2 = pygame.Rect(0, 0, 1.2*pipe.width, 0.15*pipe.height)
pipe_2.bottomright = screen_rect.bottomright
pipe_head2.midtop = pipe_2.midtop

def mainloop():

	global bird_fly, start

	while True:
		screen.fill([200, 200, 255]) # RGB -> Red Green Blue

		pygame.draw.rect(screen, (0, 90, 0), pipe_2)
		pygame.draw.rect(screen, (0, 90, 0), pipe)
		pygame.draw.rect(screen, (0, 80, 0), pipe_head)
		pygame.draw.rect(screen, (0, 80, 0), pipe_head2)

		screen.blit(bird, bird_rect)
		check_point()
		pipe_collision()

		if start:
			screen.blit(score_label_image, score_label_image_rect)
			health_pos()
			bird_move()
			platform_move()
			pipe_move()

		else:
			screen.blit(play_button, play_button_rect)
			screen.blit(title_label_image, title_label_image_rect)

		screen.blit(platform, platform_rect)

		pygame.time.Clock().tick(64)
		pygame.display.flip()

		event_listener()

mainloop()