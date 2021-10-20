# import "the neccessary stuff"
import pygame
from settings import *
from block import Block
from player import Player
from bullet import Bullet
from coin import Coin
from enemy import Enemy

class Level:
	def __init__(self, display_surface, map_layout, font):
		self.display_surface = display_surface
		self.map_layout = map_layout
		self.make_map(map_layout)
		self.world_shift = 0
		self.font = font
		self.game_active = True

	def make_map(self, map_layout):
		# Make all of the groups and list
		self.bullets = pygame.sprite.Group()
		self.blocks = pygame.sprite.Group()
		self.coins = pygame.sprite.Group()
		self.enemies = pygame.sprite.Group()
		self.boundaries = []
		self.player = pygame.sprite.GroupSingle()
		self.score = 0

		# how many of what we have created (checks for game win)
		self.coins_created = 0
		self.enemies_created = 0

		self.coins_collected = 0
		self.enemies_killed = 0

		# Go through each cell in the map layout
		for row_index, row in enumerate(map_layout):
			for col_index, cell in enumerate(row):
				# Set the position to be corresponding to the tile size and the current cell
				x = col_index * tile_size
				y = row_index * tile_size

				# Check what the cell is then add that item
				if cell == "X":
					self.blocks.add(Block((x, y)))
				elif cell == 'e':
					self.enemies.add(Enemy((x, y)))
					self.enemies_created += 1
				elif cell == 'b':
					self.boundaries.append(pygame.Rect(x, y, tile_size, tile_size))
				elif cell == 'O':
					self.player.add(Player((x, y)))
				elif cell == 'c':
					self.coins.add(Coin((x, y)))
					self.coins_created += 1

	def horizontal_collision(self): # horizontal collision check between blocks and the player (x axis)
		player = self.player.sprite # get the player

		# loop through all of the blocks and see if we're colliding with the current one in the loop
		for sprite in self.blocks.sprites():
			if sprite.rect.colliderect(player.rect):
				# check in which direction the player is headed
				# then stop the player and move him back so that he isn't inside the wall
				if player.x_vel < 0:
					player.x_vel = 0
					player.rect.left = sprite.rect.right
				elif player.x_vel > 0:
					player.x_vel = 0
					player.rect.right = sprite.rect.left

	def vertical_move_collision(self): # vertical collsion check between blacks and the player #* And move the player on the y axis
		player = self.player.sprite # get the player

		player.update_y() # Update the player's y

		# loop through all of the blocks and see if we're colliding with the current one in the loop
		for sprite in self.blocks.sprites():
			if sprite.rect.colliderect(player.rect):
				# Check which direction we're going on the y axis
				# (are we falling or jumping)
				# then make the player land on the floor or bump his head
				if player.y_vel > 0:
					player.y_vel = 0
					player.jumps = 0
					player.rect.bottom = sprite.rect.top
				elif player.y_vel < 0:
					player.y_vel = 0
					player.rect.top = sprite.rect.bottom

	def player_on_coin(self): # check collision between coins and the player
		player = self.player.sprite # get the player

		# loop through all of the coins and check if the player's colliding with one (or many) of them
		for coin in self.coins.sprites():
			if coin.rect.colliderect(player.rect):
				# if so, increase the score and destroy the coin
				self.score += 1
				self.coins_collected += 1
				coin.kill()

	def collision_enemy(self): # check collision between enemies and the player
		player = self.player.sprite # get the player

		# loop through all of the enemies and see if we're colliding with one of them
		for enemy in self.enemies.sprites():
			if player.rect.colliderect(enemy.rect):
				# check if we're falling
				# if so make the player bounce (same function as jump) and kill the enemy
				if player.y_vel > 0:
					player.jumps = 0
					player.jump()
					enemy.kill()
					self.score += 3
					self.enemies_killed += 1
				else:
		# This just returns True if we're dead, if we're alive it returns False
					return True
		return False

	def run(self):
		if self.game_active: self.display_surface.fill((20, 20, 20)) # Fill the screen with a grey-black color

		# update
		self.world_shift = self.player.sprite.update() # update the player and get the world_shift returned
		self.horizontal_collision() # player and blocks horizontal collision check
		self.vertical_move_collision() # player and blocks vertical collision check #* + UPDATE THE PLAYER ON THE Y AXIS

		self.blocks.update(self.world_shift) # shift the blocks
		self.coins.update(self.world_shift) # shift the coins

		# shift all of the enemy boundaries
		for boundary in self.boundaries: boundary.centerx += self.world_shift

		self.enemies.update(self.world_shift, self.boundaries) # shift the enemies and reverse its movement direction if it's colliding with a boundary

		# check if the player is dead and if so, reset the game
		dead = self.collision_enemy() # player on enemy
		if dead: self.make_map(map_layout)
		dead = self.player.sprite.in_void() # player in void (under the screen)
		if dead: self.make_map(map_layout)

		self.bullets.update(self.world_shift) # shift and move the bullets

		self.player_on_coin() # check if the player is colliding with a coin

		# Make the score
		score_text = self.font.render(f'Score: {self.score}', False, 'White')
		score_rect = score_text.get_rect(topleft = (25, 25))



		# draw EVERYTHING (almost)
		if self.game_active:
			self.blocks.draw(self.display_surface)
			self.enemies.draw(self.display_surface)
			self.coins.draw(self.display_surface)
			self.player.draw(self.display_surface)
			self.bullets.draw(self.display_surface)
			self.display_surface.blit(score_text, score_rect) # draw score

			# check if we've won
			if self.coins_created == self.coins_collected and self.enemies_created == self.enemies_killed:
				self.game_active = False
				win_text = self.font.render("YOU WIN!", False, 'White')
				win_rect = win_text.get_rect(center=(screen_width / 2, screen_height / 2))
				self.display_surface.blit(win_text, win_rect)