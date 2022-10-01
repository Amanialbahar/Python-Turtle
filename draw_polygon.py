import turtle

def polygon(sides, length):
  t = turtle.Turtle()
  t.color("lime")
 # t.speed(0)
  angle = 360 / sides
  for side in range(sides):
    t.forward(length)
    t.right(angle)
  t.hideturtle()


for i in range(10):
    polygon(i+3, 35)
