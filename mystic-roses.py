import turtle
import math
from itertools import combinations

numberOfPoints = int(input("number of points: "))
size = int(input("size: "))

speed = int(input("speed: "))

angle = 2 * math.pi / numberOfPoints

polarCoords = [(size, angle * i) for i in range(numberOfPoints)]
cartesianCoords = [(i[0] * math.cos(i[1]), i[0] * math.sin(i[1])) for i in polarCoords]

window = turtle.Screen()
window.bgcolor("black")

pen = turtle.Turtle(visible=False)
pen.speed(speed)
pen.color("white")
pen.up()

for i in combinations(cartesianCoords, 2):
    pen.goto(*i[0])
    pen.down()
    
    pen.goto(*i[1])
    pen.up()

input()
