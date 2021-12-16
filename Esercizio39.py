import turtle

def disegnaPoligono(nLati):
    for k in range(nLati):
        turtle.forward(100)
        turtle.right(360/nLati)

poligono=turtle.Turtle()
finestra=turtle.Screen()
n=int(input("Dammi il numero di lati del poligono: "))
disegnaPoligono(n)

finestra.exitonclick()