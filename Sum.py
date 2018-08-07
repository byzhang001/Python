
total=1
colors=["red","yellow","blue","green","purple","orange"]

name=input("What's you name?")
print(name)

print(colors[0])
print(colors[1])
print(colors[2])
print(colors[3])

for x in range(4):
    print ("x=",x)
    print(colors[x])



for x in range(2,6):
    total=total+x
print("Hello " + name)

print("total=",total)

