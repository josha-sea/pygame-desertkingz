import pygame
import itertools


class Hive(pygame.sprite.Sprite):

	# for unique instance id
	id_iter = itertools.count()

	# Takes tuple for position as argument
	def __init__(self, pos, config):
		# init for pygames Sprite class
		pygame.sprite.Sprite.__init__(self)

		self.config = config
		self.size = self.config.hive_size
		self.image = pygame.Surface((self.size, self.size))
		self.image.fill(self.config.hive_color)
		self.rect = self.image.get_rect()
		
		self.rect.center = (pos[0], pos[1])
		self.id = next(self.id_iter)

		self.life = self.config.hive_life
		self.nutrition = self.config.hive_nutrition

	def absorb_food(self):
		self.nutrition += self.config.food_nutrition

	def heal_self(self):
		#self.config.hive_self_healing_cost
		pass
	