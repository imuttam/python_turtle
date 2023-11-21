import turtle

tim = turtle.Turtle()

def draw_shape(side):
  for i in range(side):
    angle = 360/side
    tim.forward(100)
    tim.left(angle)
tim.penup()  
tim.goto(-400,-100)
x = -400
tim.pendown()
colors = ['red','blue','yellow','green','orange','pink','purple','brown']
for i in range(3,11):
  
  tim.fillcolor(colors[10%i])
  tim.begin_fill()
  draw_shape(i)
  tim.end_fill() 
  x += 100
  tim.goto(x,-100)
  

turtle.mainloop()