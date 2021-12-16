import random

def movimento():
    return random.randrange(-1, 2, 2)

nGiorni=int(input("Dammi il numero di giorni passati: "))

listaMovimenti=[movimento() for num in range(60*60*24*nGiorni)]

sommaMovimenti=0
for n in listaMovimenti:
    sommaMovimenti+=n
print(f"Somma dei movimenti: {sommaMovimenti}")
