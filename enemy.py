import pygame
from settings import *

class Enemy(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		# make the image
		self.image = pygame.Surface((tile_size, tile_size))
		self.image.fill('Orange')
		self.rect = self.image.get_rect(topleft = pos) # get the rect
		self.direction = 1 # direction, pos or neg
		self.speed = 3 # the speed (doesn't change)

	def update(self, shift, boundaries):
		self.rect.centerx += self.direction * self.speed # move the enemy in the direction * speed
		self.rect.centerx += shift # shift the player

		# reverse the direction if we're inside one of the boundaries
		for boundary in boundaries:
			if self.rect.colliderect(boundary):
				self.direction = -self.direction
