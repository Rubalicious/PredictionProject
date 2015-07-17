import turtle

bob = turtle.Turtle()

bob.speed(30)

for i in range(180):
	bob.forward(100)
	bob.right(30)
	bob.forward(20)
	bob.left(60)
	bob.forward(50)
	bob.right(30)

	bob.penup()
	bob.forward(30)
	bob.pendown()
	bob.dot()

	bob.penup()
	bob.setposition(0,0)
	bob.pendown()

	bob.right(2)

turtle.done()
