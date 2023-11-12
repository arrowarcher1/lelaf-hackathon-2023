import turtle as tur
import time
t=tur.Turtle()
t.speed(100)
t.penup()
t.goto(-30,-50) #centering in the screen
t.pensize(10)
t.pencolor("black")
x = 0
lett = ''
#t.hideturtle()
while x == 0:
    lett = input()
    t.clear()
    t.goto(-30,50)
    t.right(t.towards(0,50))
    if lett == 'a':   
        t.pendown()
        t.right(65)
        t.forward(100)

        t.setpos(-30,50)
        t.right(50)
        t.forward(100)

        t.penup()
        t.setpos(-50,-10)
        t.right(65)
        t.pendown()
        t.backward(50)
        t.penup()
        t.right(180)
    
    if lett == 'b':  
        t.penup()
#draw straight line
        t.goto(-30,50) #centering in the screen
        t.pendown()
        t.goto(-30,-150)

        t.penup()
        t.goto(-30,50) #centering in the screen
        #draw first curve
        t.pendown()
        #t.right(-90)
        t.circle(-50,180)


        t.penup()
        t.goto(-30,-50) #centering in the screen
        #draw second curve
        t.pendown()
        t.right(180)
        t.circle(-50,180)
        t.penup()
        t.right(180)
    if lett == 'c':
        t.goto(-30,50) #centering in the screen
        t.pendown()
        t.pensize(10)
        t.right(180)
        t.circle(50,180)
        t.penup()
