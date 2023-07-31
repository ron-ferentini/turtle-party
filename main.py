import turtle

def back(len):
  turtle.penup()
  turtle.backward(len)
  turtle.pendown()

def move(len):
  back(len * -1)
  
def polygon(numberOfSides, size, direction):
  length = 360 / numberOfSides
  for i in range(numberOfSides):
    turtle.forward(size)
    if direction == 'right':
      turtle.right(length )
    else:
      turtle.left(length)
 
def sprial(len, angle):
  for i in range(len, 5, -5):
      turtle.forward(i)
      turtle.right(angle)

turtle.color("blue")  
sprial(75, 45)
move(150)
turtle.color("red")  
sprial(100, 90)
