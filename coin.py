import pygame
from settings import *

class Coin(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		# get the image and transform it
		self.image = pygame.image.load('assets/coin.png').convert_alpha()
		self.image = pygame.transform.scale(self.image, (tile_size, tile_size))
		self.rect = self.image.get_rect(topleft = pos) # get the rect

	def update(self, shift): # update
		self.rect.centerx += shift # shift the coin
