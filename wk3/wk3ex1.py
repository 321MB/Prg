#
# wk3ex1.py
#
# Naam:
#
# Turtle graphics en recursie
#

import time
from turtle import *
from random import *
import turtle


def tri(n):
    """Draws n 100-pixel sides of an equilateral triangle.
    Note that n doesn't have to be 3 (!)
    """
    if n == 0:
        return  # Geen zijden om te tekenen, dus stop met tekenen
    else:
        width(2 * n + 1)  # lijn dikte is 2x de lengte n
        forward(100)
        left(120)
        tri(n - 1)  # Gebruik recursie om de overige zijden te tekenen!


def spiral(initial_length, angle, multiplier):
    """Spiral-drawing function.  Arguments:
    initial_length = the length of the first leg of the spiral
    angle = the angle, in degrees, turned after each spiral's leg
    multiplier = the fraction by which each leg of the spiral changes
    """
    if initial_length <= 1 or initial_length >= 1000:
        return  # Niets meer te tekenen, dus beëindig deze aanroep naar spiral
    else:
        forward(initial_length)  # Hier moet je de functie forward aanroepen...
        left(angle)  # Hier moet je een draai maken...
        spiral(
            initial_length * multiplier, angle, multiplier
        )  # Hier komt je recursie! Dat betekent dat je hier een nieuwe aanroep naar spiral doet...


def chai(size):
    """Our chai function!"""
    if size < 5:
        return
    else:
        forward(size)
        left(90)
        forward(size / 2)
        right(90)
        chai(size / 2)
        right(90)
        forward(size)
        left(90)
        chai(size / 2)
        left(90)
        forward(size / 2.0)
        right(90)
        backward(size)
        return


def svtree(trunklength, levels):
    """svtree: draws a side-view tree
    trunklength = the length of the first line drawn ("the trunk")
    levels = the depth of recursion to which it continues branching
    """
    if levels == 0:
        return
    else:
        forward(trunklength)  # Teken de oorspronkelijke stam (1 regel)
        left(45)  # Draai een stukje om de eerste subboom te positioneren (1 regel)
        color("blue")  #
        svtree(
            trunklength / 2, levels - 1
        )  # Voer recursie uit! met een kleinere stam en minder niveaus (1 line)
        right(
            90
        )  # Draai de andere kant op om de tweede subboom te positioneren (1 regel)
        color("yellow")  # on right turn change to yellow
        svtree(trunklength / 2, levels - 1)  # Voer opnieuw recursie uit! (1 regel)
        left(45)  # Draai en ga TERUG (2 stappen: 2 regels)
        color("red")  # on left turn cange to red
        backward(trunklength)


def flakeside(sidelenght, levels):
    if levels == 0:
        forward(sidelenght)
        return
    else:
        flakeside(sidelenght, levels - 1)
        color("blue")
        color("red")
        right(60)
        flakeside(sidelenght, levels - 1)
        color("yellow")
        left(120)
        flakeside(sidelenght, levels - 1)
        color("green")
        right(60)
        flakeside(sidelenght, levels - 1)
        return


def snowflake(sidelength, levels):
    """Fractal snowflake function, complete.
    sidelength: pixels in the largest-scale triangle side
    levels: the number of recursive levels in each side
    """
    turtle.fillcolor("green")
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
    flakeside(sidelength, levels)
    left(120)
