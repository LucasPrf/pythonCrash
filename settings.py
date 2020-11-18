#!/usr/bin/python3

class Settings:
	"""Class to store the settings"""
	#screen settings
	def __init__(self):
		"""Setting init"""
		self.screen_width = 800
		self.screen_height = 600
		self.bg_color = (230,230,230) #LightGray
		self.ship_speed = 0.5 ## Pixel Per second
		#BULLETS
		self.bullet_speed = 1.0
		self.bullet_width = 3 
		self.bullet_height = 15
		self.bullet_color = (60,60,60)
		self.bullets_allow = 5