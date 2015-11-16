import turtle

angie = turtle.Turtle()
angie.shape("turtle")

angie.penup()
size = 7
for i in range(50):
	angie.stamp()
	size = size + 2
	angie.forward(size)
	angie.forward(size)
	angie.right(24)

turtle.done()
