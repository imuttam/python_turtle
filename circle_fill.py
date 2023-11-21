from turtle import Turtle, Screen 

t = Turtle()
s = Screen()

t.color('red')
t.fillcolor('yellow')

t.begin_fill()
while True:
    t.forward(200)
    t.left(100)
    print(abs(t.pos()))
    if abs(t.pos()) < 10:
        break

t.end_fill()
s.exitonclick()