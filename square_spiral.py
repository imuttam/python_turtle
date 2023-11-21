from my_color import random_color
import turtle 

t = turtle.Turtle()
s = turtle.Screen()
t.speed('fastest')
t.pensize(3)

def square():
  for _ in range(4):
    t.fd(100)
    t.lt(90)

for i in range(36):
  t.pencolor(random_color())
  square()
  t.lt(10)
  
turtle.mainloop()