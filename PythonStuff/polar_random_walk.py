#polar random walk
import turtle, math, random

ted = turtle.Turtle()
wn = turtle.Screen()
wh = wn.window_height()
ww = wn.window_width()
ted.speed(30)

def simulation(n):
    point = []
    curr_pos = ted.position()
    for i in range(n):
        c = i/float(n)
        ted.pencolor(((1-c)**5,c,c**2))
        r = random.random()*10 #edit radius
        theta = random.random()*180 #edit angle
        ted.forward(r)
        #added condition
        if i%2 ==0:
            ted.left(theta)
        else:
            ted.right(theta)
        #store positions
        
        point.append(curr_pos)
        if curr_pos in point:
            ted.dot()
        #wrap around
        p = ted.position()
        if p[0] < -ww/2:
            ted.penup()
            ted.setposition(p[0]+ww,p[1])
            ted.pendown()
        elif p[0] > ww/2:
            ted.penup()
            ted.setposition(p[0]-ww,p[1])
            ted.pendown()
        elif p[1] < -wh/2:
            ted.penup()
            ted.setposition(p[0],p[1]+wh)
            ted.pendown()
        elif p[1] > wh/2:
            ted.penup()
            ted.setposition(p[0],p[1]-wh)
            ted.pendown()
            

simulation(500)

        
turtle.done()
