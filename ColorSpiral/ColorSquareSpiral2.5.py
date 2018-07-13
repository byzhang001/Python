import turtle

turtle.speed(0)
turtle.Turtle().screen.delay(0)

t = turtle.Pen()


colors = ["red", "blue", "green", "yellow", "orange", "purple"]
turtle.bgcolor("black")
sides = 6
for x in range(100):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
#input("Press any key to continue... ...")
