import pygame


class Food(pygame.sprite.Sprite):

	# Takes tuple for position  as argument
	def __init__(self, pos, config):
		# init for pygames Sprite class
		pygame.sprite.Sprite.__init__(self)

		self.config = config
		self.size = self.config.food_size
		self.image = pygame.Surface((self.size, self.size))
		self.image.fill(self.config.food_color)
		self.rect = self.image.get_rect()
		self.rect.center = (pos[0], pos[1])

	
	def shrink(self):
		self.size = int(self.size * self.config.food_shrinking_rate)
		self.image = pygame.Surface((self.size, self.size))
		self.image.fill(self.config.food_color)
		self.rect.size = (self.size, self.size)
		if self.size < 10:
			self.kill()

	def position(self):
		return self.rect.center

	