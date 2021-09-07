#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Lila Hunter-Reay
Due September 8, 2021
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
turtle.penup()
turtle.goto(-120,170)
turtle.pendown()
turtle.color("gold")
turtle.pensize(1)
turtle.begin_fill()
turtle.goto(40,220)
turtle.goto(10,290)
turtle.goto(-10,260)
turtle.goto(-30,290)
turtle.goto(-50,260)
turtle.goto(-80,280)
turtle.goto(-90,240)
turtle.goto(-110,250)
turtle.goto(-120,220)
turtle.goto(-150,240)
turtle.goto(-120,170)
turtle.end_fill()
turtle.penup()

turtle.goto(70,30)
turtle.pendown()
turtle.color(105,105,105)
turtle.pensize(2)
turtle.circle(10)
turtle.penup()
turtle.goto(90,50)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.goto(110,70)
turtle.pendown()
turtle.circle(10)
turtle.penup()
turtle.goto(130,90)
turtle.pendown()
turtle.circle(15)
turtle.penup()
turtle.goto(155,115)
turtle.pendown()
turtle.circle(15)
turtle.penup()
turtle.goto(160,165)

turtle.pendown()
turtle.seth(-45)
#turtle.color("red")
turtle.circle(100,90)

#turtle.color("blue")
turtle.circle(50,90)

#turtle.color("red")
turtle.circle(100,90)

#turtle.color("blue")
turtle.circle(50,90)

turtle.penup()
turtle.write("I am the king", True, align= "left", font=("Arial", 20, "normal"))

turtle.goto(-155,270)
turtle.pendown()
turtle.color("red")
turtle.pensize(20)
turtle.goto(90,20)

turtle.penup()
turtle.goto(90,270)
turtle.pendown()
turtle.goto(-155,20)
turtle.penup()

turtle.goto(130,270)
turtle.pendown()
turtle.goto(310,110)
turtle.penup()

turtle.goto(310,270)
turtle.pendown()
turtle.goto(130,110)
turtle.penup()

turtle.goto(-200,-200)
turtle.seth(135)
turtle.pendown()
turtle.pensize(7)
turtle.color("red")
turtle.circle(50,90)
turtle.penup()
turtle.goto(-260,-160)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.goto(-230,-160)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(280,-210)
turtle.seth(135)
turtle.pendown()
turtle.circle(50,90)
turtle.penup()
turtle.goto(220,-170)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.goto(250,-170)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.penup()
turtle.goto(175,-50)
turtle.seth(135)
turtle.pendown()
turtle.circle(50,90)
turtle.penup()
turtle.goto(115,-10)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.goto(145 ,-10)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.penup()
turtle.goto(-270,0)
turtle.seth(135)
turtle.pendown()
turtle.pensize(7)
turtle.color("red")
turtle.circle(50,90)
turtle.penup()
turtle.goto(-330,40)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.goto(-300,40)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(-150,200)
turtle.seth(135)
turtle.pendown()
turtle.circle(50,90)
turtle.penup()
turtle.goto(-210,240)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()
turtle.goto(-180,240)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
turtle.penup()

turtle.goto(0,280)
turtle.write("BAD BEZOS", True, align= "center", font=("Arial", 70, "normal"))




#turtle.penup()
#turtle.goto(112,-120)
#turtle.pendown()
#turtle.circle(20)




#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()