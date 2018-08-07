import turtle,random

t=turtle.Pen()
sides=eval(input("Enter a number of sides between 2 and 6"))
#t.pencolor("red")
turtle.bgcolor("black")
colors=["red","yellow","blue","green","purple","orange"]
for x in range(100):
    t.pencolor(colors[x%sides])
    t.forward(x)
    t.left(360/sides +1)


