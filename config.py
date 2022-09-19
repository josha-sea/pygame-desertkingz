
class Config:
	def __init__(self, width, height):

		self.hive_list = [
				(width*0.25,height*0.25),
				(width*0.75,height*0.25),
				(width*0.25,height*0.75),
				(width*0.75,height*0.75)
					]

		self.sandking_start_amount = 10



		self.sandking_max_life = 100
		self.sandking_size = 21
		self.sandking_speed = 1
		self.sandking_attack_radius = self.sandking_size*1.5
		self.sandking_color = (0,0,0)
		self.sandking_attrition = (0,1)
		self.sandking_healing_amount = 1
		# yet to impliment
		self.sandking_spawning_cost = 0



		self.hive_life = 1000
		self.hive_nutrition = 1000
		self.hive_size = 50
		self.hive_color = (0,255,0)
		self.hive_sandking_healing_cost = 1
		self.hive_self_healing_cost = 1
		# yet to impliment
		self.hive_mainting_cost = 0

		self.food_size = 30
		self.food_color = (0,0,255)
		self.food_shrinking_rate = 0.9 
		self.food_start_pos = ((width/2, height/2))

		self.food_nutrition = 1
