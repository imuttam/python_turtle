import turtle

# Turtle draws a colorful star pattern
colors = ["red", "blue", "green", "purple", "orange"]

for i in range(5):
    turtle.color(colors[i])
    turtle.forward(100)
    turtle.right(144)

turtle.done()
