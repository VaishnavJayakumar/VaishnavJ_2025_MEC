import turtle
import math

t = turtle.Turtle()
t.speed(0)
t.width(0)

#file start
t.clear()

c_brown = "#451417"
c_red = "#dd0900"
c_orange = "#f16009"
c_orange2 = "#ff7c01"
c_yellow = "#ffd700"
c_green = "#00ab17"
c_blue = "#003be8"
c_violet = "#7700ed"
c_violet2 = "#360087"
c_pink = "#ff45da"

def big_circle_of(func2,radius = 100,number = 3,offset = 0,*args, **kwargs):
    def bigcircle():

        t_temp_pos, t_temp_dir = t.pos(), t.heading() # storing inital pos and dir

        t.up()
        t.fd(radius)
        t.left(90)
        t.circle(radius, offset)
        t.right(270)

        for i in range(number):
            t.up()
            t.right(90)
            t.circle(radius,(360/number))
            t.right(90)
            t.down()
            func2(*args, **kwargs) # run inside function
            t.right(180)

        #original pos and dir
        t.up()
        t.setposition(t_temp_pos)
        t.setheading(t_temp_dir)

    return bigcircle


#function for setting style eazily`
def stylized(func1,fill = None,outline = None,*args,**kwargs):
    def setstyle():

        pre_color, pre_fillcolor = t.color() # storing inital colors and filles

        if outline is None:
            t.pensize(0)
        else:
            t.color(outline)

        if fill is not None:
            t.fillcolor(fill)
            t.begin_fill()

        func1(*args, **kwargs)  # run inside function

        if fill is not None:
            t.end_fill()

        #original colors
        t.color(pre_color)
        t.fillcolor(pre_fillcolor)

    return setstyle

#GO TO CENTER
def go_to_center():
    t.penup()
    t.goto(0,0)

#Make circle and and go to original position
def circle_center(r,fill = None,outline = None):
    go_to_center()
    t.fd(r)
    t.left(90)
    t.down()

    if fill is not None:
        t.fillcolor(fill)
        t.begin_fill()

    if outline is not None:
        t.pencolor(outline)

    t.circle(r)

    if fill is not None:
        t.end_fill()

    t.up()
    go_to_center()

#Flower Petal Shape
def petal_arc(length = 100, angle = 60):

    t_temp_pos, t_temp_dir = t.pos(),t.heading()
    
    r = length/(2*math.sin(math.radians(angle/2)))

    t.right(angle/2)
    t.circle(r,angle)

    t.setheading(t_temp_dir + (180-(angle/2)))

    t.circle(r,angle)

    #go back to original angles
    t.setposition(t_temp_pos)
    t.setheading(t_temp_dir)

def wedge():
    t.right(20)
    t.circle(50,360,3)
    t.left(20)

def gradient_circle(radius = 50):
    for i in range(radius):
        # gradent creator b/w 3 colors
        ratio = i/radius
        color1 = (1.0, 0.0, 0.0) # rED
        color2 = (1.0, 0.88, 0.0)  #yellow
        color3 = (1.0, 1.0, 1.0)#white
        if ratio < 0.5:
            r = color1[0] + (color2[0] - color1[0]) * (ratio * 2)
            g = color1[1] + (color2[1] - color1[1]) * (ratio * 2)
            b = color1[2] + (color2[2] - color1[2]) * (ratio * 2)
        else:
            r = color2[0] + (color3[0] - color2[0]) * ((ratio - 0.5) * 2)
            g = color2[1] + (color3[1] - color2[1]) * ((ratio - 0.5) * 2)
            b = color2[2] + (color3[2] - color2[2]) * ((ratio - 0.5) * 2)

        t.color(r, g, b)
        t.circle(radius-i)

    t.color("black")
    t.circle(radius)

#outer ring
shape1 = big_circle_of(stylized(petal_arc,angle = 120,length = 135,fill = c_red,outline = c_red), radius = 250,number = 36)
shape2 = big_circle_of(stylized(petal_arc,angle = 120,length = 120,fill = c_orange,outline = c_orange),radius = 235, number = 36,offset=5)
shape3 = big_circle_of(stylized(petal_arc,angle = 120,length = 105,fill = c_orange2,outline = c_orange2),radius = 220, number = 36,offset=0)
shape4 = big_circle_of(stylized(petal_arc,angle = 120,length = 90,fill = c_yellow,outline = c_yellow),radius = 205, number = 36,offset=5)

#middle ring
shape5 = big_circle_of(stylized(t.circle,radius = 50,fill = c_blue,outline = "black"),radius = 205, number = 8)
shape6 = big_circle_of(stylized(t.circle,radius = 30,fill = c_pink,outline = c_brown),radius = 190, number = 8,offset = 5)

shape7 = big_circle_of(stylized(wedge,fill = c_green,outline = "black"),radius = 190, number = 8,offset = 22)

shape8 = big_circle_of(stylized(petal_arc,angle = 120,length = 100,fill = c_yellow,outline = "black"),radius = 125, number = 8,offset=36.25)

#inner ring
shape9 = big_circle_of(stylized(gradient_circle,fill = c_yellow,outline = "black"),radius = 75, number = 4,offset=0)
shape10 = big_circle_of(stylized(gradient_circle,fill = c_yellow,outline = "black"),radius = 75, number = 4,offset=45)

### Drawing ####################

circle_center(387,fill = "black",outline = "black")
circle_center(385,fill = c_brown,outline = "black")
shape1()
shape2()
shape3()
shape4()
circle_center(270,fill = "black",outline = "black")
circle_center(265,fill = c_violet,outline = "violet")
circle_center(250,fill = c_violet2,outline = c_violet2)
circle_center(200,fill = c_orange2,outline = c_orange2)
t.pensize(4)

shape7()

shape5()
shape6()

t.pensize(3)
shape8()

shape9()
shape10()

circle_center(50,fill = c_blue,outline = "black")
circle_center(30,fill = c_violet2,outline = c_violet2)
circle_center(10,fill = c_pink,outline = c_pink)


turtle.mainloop()