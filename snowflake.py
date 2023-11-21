import turtle

# Turtle draws a snowflake
for _ in range(3):
    for _ in range(3):
        turtle.forward(50)
        turtle.backward(50)
        turtle.right(60)
    turtle.left(60)

turtle.mainloop()
