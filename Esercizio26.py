x=[]
n=int(input("se non vuole inserire un numero digiti 0: "))
while n != 0:
    val=int(input("Dammi un numero"))
    x.append(val)
    n=int(input("se non vuole inserire un numero digiti 0: "))
print(x)