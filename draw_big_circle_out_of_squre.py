import turtle
jack = turtle.Turtle()
jack.color("yellow")
def draw_square():
    for side in range(4):
        jack.forward(100)
        jack.right(90)

jack.speed(0)
for square in range(80):
    draw_square()
    jack.forward(5)
    jack.left(5)
