import pygame
from settings import *

class Player(pygame.sprite.Sprite):
	def __init__(self, pos):
		super().__init__()
		# make the image
		self.image = pygame.Surface((tile_size, tile_size))
		self.image.fill((200, 0, 50))
		self.rect = self.image.get_rect(topleft = pos) # get the rect
		self.start_pos = pos # define the start position
		self.direction_x = 0 # in which direction on the x axis we're facingt
		# get the direction velocities
		self.x_vel = 0
		self.y_vel = 0
		self.jumps = 0 # how many times we've jumped
		self.double_jump_cooldown = 10 # how fast you can double jump

	def jump(self): # make the player jump
		# check that  haven't double jumped yet and that we're ready to jump
		if self.jumps < 1 and self.double_jump_cooldown < 0:
			if self.y_vel != 0: self.jumps += 1 # check if that jump was out doublejump, if so make it so that we can't doublejump again
			self.y_vel = -35 # make the y velocity negative so that we're going UP
			self.double_jump_cooldown = 10 # set the cooldown

	def get_input(self): # handle the keyboard input
		keys = pygame.key.get_pressed()

		# increase or decrese the x velocity depending on what direction key is pressed
		# ( gives a sliding illusion )
		if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
			self.x_vel += 1
			self.direction_x = 1
		if keys[pygame.K_LEFT] or keys[pygame.K_a]:
			self.x_vel -= 1
			self.direction_x = -1

		# jump if we're pressing x or space
		if keys[pygame.K_x] or keys[pygame.K_SPACE]:
			self.jump()

	def update_y(self):
		self.double_jump_cooldown -= 1 # decrease the player's jump cooldown
		self.y_vel += 3  # increase the y velocity (to make the player's fall quadratic)
		self.rect.centery += self.y_vel # increase the player's y with the y velocity (makes the player fall)

	def update(self):
		self.get_input() # get the input

		self.x_vel *= 0.9 # friction on the x axis (stops the player)

		# shift the world or shift the player
		shift = 0
		if self.rect.centerx < screen_width / 5 * 2 and self.x_vel < 0:
			shift = -self.x_vel
		elif self.rect.centerx > screen_width / 5 * 3 and self.x_vel > 0:
			shift = -self.x_vel
		else:
			self.rect.centerx += round(self.x_vel)
		return round(shift)

	def in_void(self):
		# check if we're in the void, if so return "we're dead"
		if self.rect.top > screen_height:
			# reset the player variables that can affect the start of the game
			self.rect.topleft = self.start_pos
			self.y_vel = 0
			self.jumps = 1
			return True
		return False
