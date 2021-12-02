#le liste sono mutabili
lista=[3, 3.14, "ciao"]
#print(lista)
lista[1]="no"
#print(lista)
lista.append("Luigi")
#print(lista)
#print(f"La lunghezza è {len(lista)}")
numeri=[1,2,3,4,5]
lista=lista+numeri
#print(lista)
#print(numeri*3)

for numero in numeri:
    print(numero, end=" ")