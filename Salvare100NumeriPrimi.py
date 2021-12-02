def isPrimo(num):
    x=2
    primo=True
    while x < num and primo==True:
        primo= (num%x!=0)
        x+=1
    return primo

conta=0
num=0
f=open("./primi.txt","w")
while conta < 100:
    if(isPrimo(num)):
        f.write(f"{num}\n")
        conta+=1
    num+=1