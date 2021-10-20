import pygame
from settings import *

class Block(pygame.sprite.Sprite):
	def __init__(self, pos, block_type = 'normal'):
		super().__init__()
		# make the block image depending on the type of the block
		if block_type == 'normal':
			self.image = pygame.Surface((tile_size, tile_size))
			self.image.fill((70, 70, 70))
		self.rect = self.image.get_rect(topleft = pos) # get the rect

	def update(self, shift):
		self.rect.centerx += shift # shift the blocks
