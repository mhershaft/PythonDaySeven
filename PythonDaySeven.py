import turtle
import time
t = turtle.Pen()
def polygon(sides, degrees, length):
    for x in range(0, sides):
        t.pendown()
        t.forward(length)
        t.right(degrees)
    t.penup()
print "Hello! Let's make shapes using Turtle!"
while True==True:
    kind = raw_input("What kind of shape? Square, Triangle, Pentagon, Hexagon, Heptagon or Octagon?\n")
    kind = kind.lower()
    shapes = {"triangle":[3,120,50], "square":[4,90,50], "pentagon":[5,72,50], "hexagon":[6, 60, 50], "heptagon":[7, 51.4285714, 50], "octagon":[8, 45, 50]}
    coordinates = shapes[kind]
    polygon(coordinates[0], coordinates[1], coordinates[2])
    time.sleep(10)
    turtle.exitonclick()