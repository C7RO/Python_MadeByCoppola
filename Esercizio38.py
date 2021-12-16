isDividibilePerDue= lambda num: num%2==0
isDividibilePerTre= lambda num: num%3==0
isDividibilePerCinque= lambda num: num%5==0

n=int(input("Dammi un numero: "))
if(isDividibilePerCinque(n) | isDividibilePerDue(n) | isDividibilePerTre(n)):
    if(isDividibilePerDue(n)):
        print("Divisibile per 2\n")
    if(isDividibilePerTre(n)):
        print("Divisibile per 3\n")
    if(isDividibilePerCinque(n)):
        print("Divisibile per 5\n")
else:
    print("Non divisibile per 2, 3 e 5!\n")