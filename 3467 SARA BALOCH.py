import math
import time
import turtle

screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.colormode(1.0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def heart_x(angle):
    return 16 * math.sin(angle) ** 3


def heart_y(angle):
    return (
        13 * math.cos(angle)
        - 5 * math.cos(2 * angle)
        - 2 * math.cos(3 * angle)
        - math.cos(4 * angle)
    )    

        
N = 140
outer_scale = 18.0
inner_scale = 5.0
steps = 14

c_outer = (1.0, 0.70, 0.78)
c_inner = (0.0, 0.0, 0.0)

for i in range(N):
    angle = 2 * math.pi * i / N
    
    x0 = heart_x(angle) * outer_scale
    y0 = heart_y(angle) * outer_scale
    
    x1 = heart_x(angle) * inner_scale
    y1 = heart_y(angle) * inner_scale
    

    for j in range(steps):
        f1 = j / steps
        f2 = (j + 1) / steps

        x_start = x0 + (x1 - x0) * f1
        y_start = y0 + (y1 - y0) * f1

        x_end = x0 + (x1 - x0) * f2
        y_end = y0 + (y1 - y0) * f2

        r = c_outer[0] + (c_inner[0] - c_outer[0]) * f1
        g = c_outer[1] + (c_inner[1] - c_outer[1]) * f1
        b = c_outer[2] + (c_inner[2] - c_outer[2]) * f1

        w = 2.2 - (1.7 * f1)
        
        t.pencolor(r, g, b)
        t.pensize(w)
        t.penup()
        t.goto(x_start, y_start)
        t.pendown()
        t.goto(x_end, y_end)
        
    time.sleep(0.02)    

turtle.done()    
