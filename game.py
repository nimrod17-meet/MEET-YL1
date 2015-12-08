from meet import *
cells=[]
for i in range(20):
	x_direction = random.randint(0,1)
	y_direction = random.randint(0,1)
	dy=0
	dx=0
	if x_direction == 1:
		if y_direction == 1:
			dx = random.random()
			dy = random.random()
		elif y_direction == 0:
			dx = random.random()
			dy = random.random() * -1

	elif x_direction == 0:
		if y_direction == 1:
			dx = random.random() * -1
			dy = random.random()
		elif y_direction == 0:
			dx = random.random() * -1
			dy = random.random() * -1

	
	cell1={"x":get_random_x(), "y":get_random_y(), "radius":random.randint(1,50), "dy":dy, "dx":dx}
	z=create_cell(cell1)
	cells.append(z)
get_screen_width()
get_screen_width() * -1
