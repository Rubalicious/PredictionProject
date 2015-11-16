#random walk
import turtle, math, random

angie = turtle.Turtle()
angie.speed(20)
def simulation(n):
    for i in range(1000):
        u = random.random()
        if u < 0.25:
            angie.left(90)
        elif u >=0.25 and u < 0.5:
            angie.left(180)
        elif u >= 0.5 and u < 0.75:
            angie.left(270)
        else:
            angie.left(0)
        angie.forward(n)


simulation(10)

turtle.done()
