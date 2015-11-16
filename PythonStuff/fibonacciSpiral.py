import turtle
import math

bob = turtle.Turtle()

bob.speed(10)

#making the fibonaccis sequence

def fib(n):
    if n == 0: return 1
    if n == 1: return 1
    else: return fib(n-1) + fib(n-2)

#making fibonacci squares

def make_square(n):
    for i in range(6):
        bob.forward(n)
        bob.left(90)
    bob.right(90)

#start with n = 1

def run_simulation(n):
    for i in range(n):
        make_square(fib(i))


def draw_spiral(n):
    for i in range(n):
        bob.pencolor((1-i/float(n),1-i/float(n),i/float(n)))
        bob.circle(fib(i),90)


run_simulation(13)
bob.penup()
bob.setposition(0,0)
bob.pendown()
bob.right(90)
draw_spiral(13)

turtle.done()
