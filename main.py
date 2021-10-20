from settings import *
from bullet import Bullet
from level import Level
import sys
import pygame
pygame.init()

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pygaman')
clock = pygame.time.Clock()

font = pygame.font.Font('font/Pixeltype.ttf', 54)

level = Level(screen, map_layout, font)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_z:
				level.bullets.add(Bullet(level.player.sprite.rect.center, level.player.sprite.direction_x * 20)) # make a new bullet in the center of the sprite

	level.run()

	pygame.display.update()
	clock.tick(30)
