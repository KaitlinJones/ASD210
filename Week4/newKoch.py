"""
File: koch.py
Project 7.3
This program displays a Koch snowflake using 
the user's input level.
"""
from turtle import Turtle, tracer, update
import turtle #import turtle
import math
import sys
import random

def drawKochFractal(width, height, size, level):
    """Draws a Koch fractal of the given level and size."""
    t = Turtle()
    t.hideturtle()
    t.up()
    t.goto(-width // 3, height // 4)
    t.down()
    drawFractalLine(t, size, 0, level)
    drawFractalLine(t, size, -120, level)
    drawFractalLine(t, size, 120, level)

def drawFractalLine(t, distance, theta, level):
    """Either draws a single line in a given direction
    or four fractal lines in new directions."""
    if (level == 0):
        drawPolarLine(t, distance, theta)
    else:
        turtle.colormode(255) #change color mode from 1.0 default to 255
        t.pencolor(random.randint(0,255), random.randint(0, 255), random.randint(0, 255))
        drawFractalLine(t, distance // 3, theta, level - 1)
        drawFractalLine(t, distance // 3, theta + 60, level - 1)
        drawFractalLine(t, distance // 3, theta - 60, level - 1)
        drawFractalLine(t, distance // 3, theta, level - 1)

def drawPolarLine(t, distance, theta):
    """Moves the given distance in the given direction."""
    t.setheading(theta)
    t.forward(distance)

def main():
    level = int(input("Enter the level: "))
    if level > 3:
        tracer(False)
    drawKochFractal(200, 200, 150, level)
    if level > 3:
        update()
if __name__ == "__main__":
   main()
