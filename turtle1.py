from turtle import Turtle, Screen

t = Turtle()
s = Screen()
t.shape('turtle')

for steps in range(100):
    for c in ('blue', 'red', 'green'):
        t.color(c)
        t.forward(steps)
        t.right(30)



s.exitonclick()
