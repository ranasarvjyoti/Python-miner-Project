from calendar import firstweekday
from email.contentmanager import raw_data_manager
import turtle
from turtle import color, pencolor
import random

def pen(colour):
    turtle.color(colour)

def fireworks(size):
    for num in range(20):
        turtle.forward(size)
        turtle.rt(180-(360/20))

def move():
    turtle.penup()
    x=random.randint(-165,165)
    y=random.randint(-165,165)
    turtle.goto(x,y)
    turtle.pendown()

turtle.bgcolor("black")
turtle.speed(0)
colors=['red','yellow','green','cyan','blue','magenta','orange','pink','gold','silver']
for _ in range(30):
    color=random.choice(colors)
    pen(color)
    fireworks(random.randint(50,100))
    move()

turtle.done()