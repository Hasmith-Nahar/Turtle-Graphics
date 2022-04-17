from turtle import Turtle, Screen

# import turtle as t
Timmy = Turtle()
# Timmy.shape("turtle")
# Timmy_the_Turtle.color("Purple")
# Timmy_the_Turtle.forward(100)
# Timmy_the_Turtle.right(90)

''' Challenge 1'''
# for _ in range(4):
#     Timmy.forward(100)
#     Timmy.right(90)

''' Challenge 2 '''
# for _ in range(15):
#     Timmy.forward(10)
#     Timmy.penup()
#     Timmy.forward(10)
#     Timmy.pendown()

''' Challenge 3 '''
# import random
# colours = ["blue", "cornflower blue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
#            "Wheat", "SlateGray", "SeaGreen"]
#
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         Timmy.forward(100)
#         Timmy.right(angle)
#
#
# for shape_side_n in range(3, 8):
#     Timmy.color(random.choice(colours))
#     draw_shape(shape_side_n)

''' Challenge 4 '''
import random
colours = ["blue", "cornflower blue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen",
           "Wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
Timmy.pensize(10)
Timmy.speed("fastest")   # option for() fastest = 0, fast = 10 , normal = 6 , slow = 3, slowest = 1

for _ in range(250):
    Timmy.color(random.choice(colours))
    Timmy.forward(30)
    Timmy.setheading(random.choice(directions))

screen = Screen()
screen.exitonclick()
