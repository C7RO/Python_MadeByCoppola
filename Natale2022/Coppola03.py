#Scrivere un programma che data una lista ne stampi una sua
#permutazione casuale.

import random

def permutaLista(l):
    k=0
    while k < len(l):
        r=random.randint(0,len(l)-1)
        l[k],l[r]=l[r],l[k]
        k+=1
    return l

lista=[1,2,3,4]
lista=permutaLista(lista)#random.shuffle(lista)
print(lista)