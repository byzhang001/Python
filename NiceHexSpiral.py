import turtle

colors=['red','purple','blue','green','yellow','orange']
t=turtle.Pen()
turtle.bgcolor('black')
for x in range(100):
    print(colors[x%6])
    print (x%6)

for x in range(300):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(40)

#input("Press any key to continue... ...")