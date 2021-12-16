import turtle

def quadrato(lato):
    for n in range(4):
        matita.forward(lato)
        matita.right(90)

def griglia(lato, n):
    coordinate=[0,0]
    for _ in range(n):
        for _ in range(n):
            matita.goto(coordinate[0],coordinate[1])
            quadrato(lato)
            coordinate[0]+=lato
        coordinate[0]=0
        matita.goto(0,coordinate[1])
        coordinate[1]-=lato

matita=turtle.Turtle()
finestra=turtle.Screen()
lato=int(input("Dammi il lato: "))
n=int(input("Grandezza griglia: "))
griglia(lato, n)

finestra.exitonclick()