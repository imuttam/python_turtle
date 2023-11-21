import turtle
"""Draw a pattern combining circles and squares."""
# Turtle draws a pattern
for _ in range(4):
    turtle.circle(50)
    turtle.forward(50)

turtle.done()


# **************************************************
"""Draw a house with a square as the base and a triangle as the roof."""
# Turtle draws a house
# Base (square)
for _ in range(4):
    turtle.forward(100)
    turtle.right(90)

# Roof (triangle)
turtle.forward(100)
turtle.left(45)
turtle.forward(70.71)
turtle.left(90)
turtle.forward(70.71)

turtle.done()
