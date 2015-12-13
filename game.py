import time
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

	
	cell1={"x":get_random_x(), "y":get_random_y(), "radius":random.randint(1,), "dy":dy, "dx":dx}
	z=create_cell(cell1)
	cells.append(z)
user_cell={"x":get_random_x(), "y":get_random_y(), "radius":random.randint(20,30), "dy":dy, "dx":dx}
n=create_cell(user_cell)
cells.append(n)
def check_border(cells):
	for a in cells:		
		wid=get_screen_width()
		hig=get_screen_height()
		if a.xcor()>=wid:
			x=a.get_dx()
			y=a.get_dy()
			a.set_dx(-x)
			a.set_dy(-y)
		if a.xcor()>=-wid:
			x=a.get_dx()
			y=a.get_dy()
			a.set_dx(-x)
			a.set_dy(-y)
		if a.ycor()>=hig:
			x=a.get_dx()
			y=a.get_dy()
			a.set_dx(-x)
			a.set_dy(-y)
		if a.ycor()>=-hig:
			x=a.get_dx()
			y=a.get_dy()
			a.set_dx(-x)
			a.set_dy(-y)

def n_eating(n):
	for cell in cells:	
		x1=cell.xcor()
		y1=cell.ycor()
		r1=cell.get_radius()
		ux=n.xcor()
		uy=n.ycor()
		ur=n.get_radius()
		if ((x1-ux)*(x1-ux)+(y1-uy)*(y1-uy))**0.5<=r1+ur:
			if ur>r1:
				nx=get_random_x()
				ny=get_random_y()
				cell.goto(nx,ny)
				n.set_radius(1+ur)
				cell.set_radius(r1+5)
def cells_eating_me(cells):
	for one in cells:
		x1=one.xcor()
		y1=one.ycor()
		r1=one.get_radius()
		ux=n.xcor()
		uy=n.ycor()
		ur=n.get_radius()
		if ((x1-ux)*(x1-ux)+(y1-uy)*(y1-uy))**0.5<=r1+ur:
			if ur<r1:
				bye()
move_cells(cells)
time.sleep(2)				
while True:
	dx,dy = get_user_direction(n)
	n.set_dx(dx)
	n.set_dy(dy)
	move_cells(cells)
	check_border(cells)
	n_eating(n)
	cells_eating_me(cells)	
cells.mainloop()
	
 
	
