import pygame

class Bullet(pygame.sprite.Sprite):
	def __init__(self, pos, x_speed):
		super().__init__()
		# make the image
		self.image = pygame.Surface((20, 5))
		self.image.fill((255, 125, 0))
		self.rect = self.image.get_rect(topleft = pos) # get the rect
		self.speed = x_speed # how fast the bullet is traveling

	def update(self, shift): # update the bullet
		self.rect.centerx += shift # shift it
		self.rect.centerx += self.speed # move it (x speed)