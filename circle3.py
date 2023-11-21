from turtle import Turtle, Screen 

t = Turtle()
s = Screen()

t.color('red')
t.fillcolor('yellow')

t.begin_fill()
for i in range(10):
  if 1 == 4 or i==5:
    t.penup()
  else:
    t.forward(200)
    t.left(150)
   

t.end_fill()
s.exitonclick()