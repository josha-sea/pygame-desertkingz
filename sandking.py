import pygame
import random
import math


class Sandking(pygame.sprite.Sprite):

	# Takes hive object as argument
	def __init__(self, hive, config):
		# init for pygames Sprite class
		pygame.sprite.Sprite.__init__(self)

		self.config = config
		self.size = self.config.sandking_size
		self.image = pygame.Surface((self.size, self.size))
		self.image.fill(self.config.sandking_color)
		self.rect = self.image.get_rect()
		self.rect.center = hive.rect.center

		self.hive = hive
		self.home_pos = self.hive.rect.center
		self.speed = self.config.sandking_speed

		
		self.max_life = self.config.sandking_max_life
		self.life = self.max_life
		self.radius = self.config.sandking_attack_radius
		self.id = self.hive.id

		# state map
		self.state_map = {

				"is_fighting": False,
				"is_healing": False,
				"carry" : 0,
				"fighting_mode": 0,
				"to_die" : False


				}

	def move_to(self, x, y):
		if x > self.rect.centerx: self.rect.centerx += self.speed
		if x < self.rect.centerx: self.rect.centerx -= self.speed
		if y > self.rect.centery: self.rect.centery += self.speed
		if y < self.rect.centery: self.rect.centery -= self.speed

	def go_home(self):
		self.move_to(self.home_pos[0], self.home_pos[1])

	def is_home(self):
		return self.rect.collidepoint(self.home_pos)

	def position(self):
		return self.rect.center

	def fight(self):

		if self.state_map["fighting_mode"]:
			self.rect.centerx += 5
			self.state_map["fighting_mode"] = 0
		else:
			self.rect.centerx -= 5
			self.state_map["fighting_mode"] = 1

		self.life -= random.randint(self.config.sandking_attrition[0],self.config.sandking_attrition[1])

		# sandking dies
		if self.life <= 0: self.state_map["to_die"] = True

	def heal(self):
		if self.is_home() and self.life < self.max_life and self.hive.nutrition > 0:

			
			self.life += self.config.sandking_healing_amount
			self.hive.nutrition -= self.config.hive_sandking_healing_cost

	# Takes food-sprite-group as argument
	# Returns food-sprite with smallest distance to hive position
	def choose_food(self, all_foods):

		food_dist = []
		# Create list of tuples where [0] is hive-food-distance and list[1] is food sprite
		for food in all_foods.sprites():
			d = math.dist(self.home_pos, food.rect.center)
			food_dist.append((d, food))

		# Sort list by distance
		food_dist.sort(key=lambda x: x[0])

		return food_dist[0][1]








	

		



			
			
	