import turtle
amani = turtle.Turtle()
amani.color("red")
amani.speed(0)

for side in range(50):
    amani.forward(side*10)
    amani.right(120)
