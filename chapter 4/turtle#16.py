# File: turtle#16.py
# Description: Use turtle loop graphics to the specific example. 
# Assignment Name and Number: Turtle Graphics Repeating Sqaures #16
#
# Name: Dimitri Perris
# GitHub: <YOUR GitHub>
#
# On my honor, <YOUR NAME>, this programming assignment is my own work
# and I have not provided this code to any other student.

import turtle

NUM_SQUARES = 100 
SIDE_LENGTH = 3 
ANGLE = 90         
ANIMATION_SPEED = 0  

turtle.speed(ANIMATION_SPEED)

for count in range(NUM_SQUARES):
    for count in range(4):
        turtle.forward(SIDE_LENGTH)
        turtle.left(ANGLE)
    SIDE_LENGTH += 3 

input('press any key to exit')


