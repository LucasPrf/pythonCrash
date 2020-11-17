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