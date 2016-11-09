import turtle
# import pdb
# pdb.set_trace()

def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def main():
    bob = turtle.Turtle()

    bob.speed(20)

    theta = 137.508
    a = 1
    b = 1
    c = 1
    #radius = c*theta**0.5

    for r in range(500):
        radius = a + b*r**(1/c)
        # red = r/500.0
        # gre = r/500.0
        # blu = r/500.0
        # if r%3 == 0:
        #     bob.pencolor((1,1-gre,0))
        # elif r%3 == 1:
        #     bob.pencolor((1,1,0))
        # else:
        #     bob.pencolor((1,gre,blu))
        bob.dot()
        bob.penup()
        bob.left(theta)
        bob.forward(radius)

    turtle.done()

main()
