import tkinter
import turtle
from turtle import Turtle, Screen, showturtle, xcor, ycor

    

#===================OBJECTS======================

win = Screen()
text = Turtle()
lines = Turtle()
messages = Turtle()
ui_addons = Turtle()
center_dot = Turtle()
center_circle = Turtle()
center_crosshair = Turtle()

#====================SETUP=========================


win.setup(width=450, height=400)
win.bgcolor("black")
text.penup()
lines.penup()
messages.penup()
ui_addons.penup()
center_dot.penup()
center_circle.penup()
center_crosshair.penup()
text.pencolor("white")
lines.pencolor("white")
messages.pencolor("white")
ui_addons.pencolor("white")
center_dot.pencolor("white")
center_circle.pencolor("white")
center_crosshair.pencolor("white")
text.hideturtle()
lines.hideturtle()
messages.hideturtle()
ui_addons.hideturtle()
center_dot.hideturtle()
center_circle.hideturtle()
center_crosshair.hideturtle()
text.goto(0,0)
lines.goto(0,0)
messages.goto(0,0)
ui_addons.goto(0,0)
center_dot.goto(0,0)
center_circle.goto(0,0)
center_crosshair.goto(0,0)
text.clear()
lines.clear()
messages.clear()
ui_addons.clear()
center_dot.clear()
center_circle.clear()
center_crosshair.clear()

#==========================LOADER=====================
import random
import time
import datetime
import ctypes
import winsound
import os
#===========================MAIN======================

def reboot(x,y):
    os.system("start cps-main.py")
    win.bye()
    exit()
def donex():
    win.listen()
    win.onclick(reboot)


center_dot.shape("square")
center_dot.showturtle()


dotsize = 0
for i in range(3):
    dotsize = dotsize + 0.1
    center_dot.shapesize(dotsize)
    center_dot.fillcolor("white")
    time.sleep(0.1)
    win.update()


center_circle.goto(0,-20)
center_circle.pendown()
center_circle.circle(20)
center_circle.penup()


center_crosshair.goto(random.randint(-100,100),random.randint(-100,100))
center_crosshair.showturtle()
deffs = random.randint(0,90)
text.goto(0,150)
text.pencolor("red") 
text.write("Not centered",align="center",font=("consolas",20,"normal"))



#for i in range(10):
#
#
#    center_crosshair.pencolor("red")
#    win.update()
#    win.delay(500)
#
#    center_crosshair.pencolor("orange")
#    win.update()


    
    
win.update()
center_crosshair.pencolor("red")
cy = center_crosshair.ycor()
print(cy)
cx = center_crosshair.xcor()
print(cx)
cym = cy
cxm = cx
done = 0
textclear = 0 
while True:
    cy = center_crosshair.ycor()
    ang = center_crosshair.heading()
    cx = center_crosshair.xcor()
    
    if cy < 0 :
        cym = cym + 1
    if cy > 0 :
        cym = cym - 1
    if cy == 0:
        cym = 0
        
    if cx < 0 :
        cxm = cxm + 1
    if cx > 0 :
        cxm = cxm - 1
    if cx == 0:
        cxm = 0
        
    cc = cy + cx
    if ang != 90:
        center_crosshair.left(10)
    
    
    if cc == 0:
        
        center_crosshair.pencolor("green")
        center_dot.pencolor("green")
        if textclear == 0:
            text.clear()
            textclear = 1
        if textclear == 1:
            pass
        
        if done == 0:
            done = 1
        if done == 1:
            donex()

        text.pencolor("green")
        text.write("Centered",align="center",font=("consolas",20,"normal"))
       
    center_crosshair.goto(cxm,cym)

