import pygame
import sys
import os

from sandking import Sandking
from hive import Hive
from food import Food 
from config import Config


window_width = 700
window_height = 500
fps = 60

# set up assets folder
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")


# initialize pygame, create window
pygame.init()
screen = pygame.display.set_mode([window_width, window_height])
pygame.display.set_caption("DesertkingZ")
clock = pygame.time.Clock()


# Define sprite groups
all_sandkings = pygame.sprite.Group()
all_hives = pygame.sprite.Group()
all_foods = pygame.sprite.Group()

# Instanciate entity-objects
# Config object
config = Config(window_width, window_height)

# Hive and sandking objects
for i in config.hive_list:
	hive = Hive(i, config)
	all_hives.add(hive)

	for j in range(config.sandking_start_amount):
		sandking = Sandking(hive, config)
		all_sandkings.add(sandking)

# Food object
food = Food(config.food_start_pos, config)

all_foods.add(food)


total_sandkings = all_sandkings.sprites()


# Game loop
while True:
	
	clock.tick(fps)

	### Process input (events) ###
	# Event loop
	for event in pygame.event.get():
		# Exit case
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	## Update section ##
	# Update section for sandkings
	for sandking in all_sandkings.sprites():

		sandking.state_map["is_fighting"] = False

		# Create list of enemy sandkings by id
		enemy_sandkings = list(filter(lambda x: sandking.id != x.id, total_sandkings))

		# Check for fighting
		if enemy_sandkings:
			for enemy in enemy_sandkings:
				if pygame.sprite.collide_circle(sandking, enemy):
					sandking.fight()
					sandking.state_map["is_fighting"] = True


		# When not fighting
		if sandking.state_map["is_fighting"] == False:

			# if there is any food and not carrying food already, go to food
			# NOTE: atm refers to first of all_foods
			if all_foods and sandking.state_map["carry"] == 0:

				food = sandking.choose_food(all_foods)

				sandking.move_to(food.position()[0], food.position()[1])


			# When sandking touches any food and not carrying food
			if pygame.sprite.spritecollide(sandking, all_foods, False) and sandking.state_map["carry"] == 0:
				sandking.state_map["carry"] = 1

				# Find food with which sandking is colliding and shrink food
				for food in all_foods.sprites():
					if pygame.sprite.collide_rect(food, sandking):
						food.shrink()



			if sandking.state_map["carry"] == 1 or not all_foods:
				sandking.go_home()

			if sandking.is_home():
				sandking.heal()
				if sandking.state_map["carry"] == 1:
					sandking.state_map["carry"] = 0
					sandking.hive.absorb_food()

				


		# When dying, turn to food and die
		if sandking.state_map["to_die"]:

			food = Food(sandking.position(), config)
			all_foods.add(food)

			sandking.kill()

	# Update section for hives
	for hive in all_hives.sprites():
		pass 


			

	# Update list of all sandkings
	total_sandkings = all_sandkings.sprites()
	
	### Draw section ###
	screen.fill((51, 51, 0))

	all_hives.draw(screen)
	all_foods.draw(screen)
	all_sandkings.draw(screen)
	


	# flip is the last thing in the game loop_
	# after drawing everything, flip the display
	pygame.display.flip()



pygame.quit()
sys.exit()