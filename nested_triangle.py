import turtle

# Turtle draws nested triangles
for i in range(6):
    for _ in range(3):
        turtle.forward(50)
        turtle.right(120)
    turtle.right(60)

turtle.done()
