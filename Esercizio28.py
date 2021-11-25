def isPrimo(num):
    x=2
    primo=True
    while x < num and primo==True:
        primo= (num%x!=0)
        x+=1
    return primo

num=int(input("Dammi un numero"))
if(isPrimo(num)):
    print("Numero Primo")
else: 
    print("Numero NON Primo")