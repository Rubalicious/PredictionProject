import turtle

r = [x**2 for x in range(11)]

bob = turtle.Turtle()

bob.speed(40)
bob.penup()
for i in range(91):
	bob.forward(34)
	bob.pendown()
	bob.dot()
	bob.penup()
	bob.setposition(0,0)
	bob.left(1)

bob.setposition(0,13)
for i in range(91):
	bob.forward(21)
	bob.pendown()
	bob.dot()
	bob.penup()
	bob.setposition(0,13)
	bob.left(1)

bob.setposition(-8,13)
for i in range(91):
	bob.forward(13)
	bob.pendown()
	bob.dot()
	bob.penup()
	bob.setposition(-8,13)
	bob.left(1)

bob.setposition(-8,8)
for i in range(91):
	bob.forward(8)
	bob.pendown()
	bob.dot()
	bob.penup()
	bob.setposition(-8,8)
	bob.left(1)
	
turtle.done()
