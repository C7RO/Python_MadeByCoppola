import turtle

def disegnaPoligono(nLati):
    matite[1].left(180)
    matite[0].forward(50)
    matite[1].forward(50)
    matite[0].right(360/nLati)
    matite[1].left(360/nLati)
    for k in range(nLati-1):
        matite[0].forward(100)
        matite[1].forward(100)
        matite[0].right(360/nLati)
        matite[1].left(360/nLati)
        

matite=[turtle.Turtle(), turtle.Turtle()]
finestra=turtle.Screen()
n=int(input("Dammi il numero di lati del poligono: "))
disegnaPoligono(n)

finestra.exitonclick()