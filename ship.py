#!/usr/bin/python3

import pygame

class Ship:
	"""Class to manage the ship"""
	def __init__(self,ai_game):
		self.screen = ai_game.screen
		self.screen_rect = ai_game.screen.get_rect()

		#Load the img
		self.image = pygame.image.load('imgs/mainrocket.bmp')
		self.rect = self.image.get_rect()
		#Star at the middle bottom 
		self.rect.midbottom = self.screen_rect.midbottom

		##Movment
		self.mov_right = False
		self.mov_left = False
		self.settings = ai_game.settings
		self.x = float(self.rect.x)


	def update(self):
		if self.mov_right and self.rect.right < self.screen_rect.right:
			self.x += self.settings.ship_speed
		if self.mov_left and self.rect.left > self.screen_rect.left:
			self.x -= self.settings.ship_speed
		self.rect.x = self.x

	def blitme(self):
		"""Draw the ship"""
		self.screen.blit(self.image,self.rect)	