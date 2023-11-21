import turtle 
import random 

tim = turtle.Turtle() 
tim.shape('turtle')
tim.pensize(10)
tim.speed('fastest')

screen = turtle.Screen()
screen.colormode(255)

colors = ['red','blue','yellow','green','orange','pink','purple','brown']
angle = [0, 90, 180, 270]

def random_color():
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  color = (r, g, b)
  return color
  
for i in range(100):
  tim.pencolor(random_color())
  tim.setheading(random.choice(angle))
  tim.forward(50)
  
# turtle.mainloop()
screen.exitonclick()