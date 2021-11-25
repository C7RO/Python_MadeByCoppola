def isPrimo(num):
    x=2
    primo=True
    while x < num and primo==True:
        primo= (num%x!=0)
        x+=1
    return primo

for n in range(1000):
    if(isPrimo(n)):
        print(n)