from my_color import random_color

import turtle 
t = turtle.Turtle()
s = turtle.Screen()

t.speed('fastest')
t.pensize(4)



for i in range(36):
  t.pencolor(random_color())
  t.circle(100)
  t.lt(10)
  
turtle.mainloop()