import turtle
snow=turtle.Turtle()
finestra=turtle.Screen()
f=open("./comandi.txt", "r")

riga=f.readline()
while(riga):
    ls= riga.split(":")
    if(ls[0]=="forward"):
        snow.forward(float(ls[1]))
    if(ls[0]=="back"):
        snow.back(float(ls[1]))
    if(ls[0]=="right"):
        snow.right(float(ls[1]))
    if(ls[0]=="left"):
        snow.left(float(ls[1]))
    if(ls[0]=="goto"):
        lr=str(ls[1]).split(",")
        snow.goto(float(lr[0]), float(lr[1]))
    riga=f.readline()

finestra.exitonclick()
f.close