""" Basic Reinforcement Learning environment using Turtle Graphics """
    
#imported libraries required for this project
import turtle
#import numpy as np


""" Environment """

#initialise the screen using a turtle object
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Basic_Reinforcement_Learning_Environment")
wn.bgpic("game_background.gif")

#this function initializes the 2D environment
def grid(size): 
    #this function creates one square
    def create_square(size,color="white"):
        greg.color(color)
        greg.pd()
        for i in range(4):
            greg.fd(size)
            greg.lt(90)
        greg.pu()
        greg.fd(size)
    #this function creates a row of sqaures based on simply one square
    def row(size,color="white"):
            for i in range(6):
                create_square(size)
            greg.hideturtle()
            
    row(size)       

greg = turtle.Turtle()
greg.speed(0)
greg.setposition(-150,0)
grid(50)


""" Agent """

#create a player token - this will be our agent
player = turtle.Turtle()
player.color("blue")
player.shape("circle")
player.penup()
player.speed(0)
player.setposition(-125,25)
player.setheading(90)

""" Set up Agent Movement """

playerspeed = 50

def move_left():
    x = player.xcor()
    x -= playerspeed
    if x < -150:
        x = -125
    player.setx(x)

        
def move_right():
    if player.xcor() == 125 and player.ycor() == 25:
        player.goto(-125,25)
    else:
        x = player.xcor()
        x += playerspeed
        if x > 150:
            x = 125
        player.setx(x)
     
    
#Create Keyboard Bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")

print("hi")

delay = input("Press enter to finish.")