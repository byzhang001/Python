import turtle

turtle.speed(0)
turtle.Turtle().screen.delay(0)

t = turtle.Pen()


colors = ["red", "blue", "green", "yellow", "orange", "purple"]
turtle.bgcolor("black")
#sides = 3
sides=eval(input("Enter a umber of sides between 2 and 6:"))

for x in range(360):
    t.pencolor(colors[x % sides])
    t.forward(x * 3 / sides + x)
    t.left(360 / sides + 1)
    t.width(x * sides / 200)
#input("Press any key to continue... ...")
