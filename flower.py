# Draw a flower pattern with petals and a center.

import turtle
import random
turtle.speed(3)
colors = ['red','blue','yellow','green','orange','pink','purple','brown']

turtle.shape('turtle')
turtle.pensize(4)
# Function to draw a petal
def draw_petal():
    turtle.begin_fill()
    turtle.forward(50)
    turtle.right(45) 
    turtle.forward(50)
    turtle.right(135)
    turtle.fillcolor(random.choice(colors))
    turtle.end_fill()

# Turtle draws a flower with petals and a center
for _ in range(8):  # Adjust the number of petals as needed
    draw_petal()
    turtle.left(45)
    draw_petal()

turtle.done()

