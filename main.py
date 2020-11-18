#!/usr/bin/python3

import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
	"""Main Window Calss"""

	def __init__(self):
		"""Init the Pygame Module"""
		pygame.init()
		self.settings = Settings()
		self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		pygame.display.set_caption("Alien Invasion")

	def _check_events(self):
		"""Respond to the mouse and keyboard events"""
		for evt in pygame.event.get():
			if evt.type == pygame.QUIT:
				sys.exit()

			##MOVING RIGHT
			elif evt.type == pygame.KEYDOWN:
				self._check_keydown_evts(evt)
			elif evt.type == pygame.KEYUP:
				self._check_keyup_evts(evt)

	def _check_keydown_evts(self,evt):
		if evt.key == pygame.K_d:
			self.ship.mov_right = True
		elif evt.key == pygame.K_a:
			self.ship.mov_left = True
		elif evt.key == pygame.K_ESCAPE:
			sys.exit()
		elif evt.key == pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_evts(self,evt):
		if evt.key == pygame.K_d:
			self.ship.mov_right = False
		elif evt.key == pygame.K_a:
			self.ship.mov_left = False

	def _update_screen(self):
		"""Update the screen"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		pygame.display.flip()

	def _fire_bullet(self):
		if len(self.bullets) < self.settings.bullets_allow:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)

	def _update_bullets(self):
		self.bullets.update()

		##remove bullets

		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
		print(len(self.bullets))	

	def run_game(self):
		"""Star the Main loop for Run the game"""
		while True:
			self._check_events()
			self.ship.update()
			self._update_bullets()		
			self._update_screen()


if __name__ == '__main__':
	#Alien Instance
	ai = AlienInvasion()
	ai.run_game()