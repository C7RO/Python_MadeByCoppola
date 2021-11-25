n=int(input("Quale operazione vuole fare?\n 0-> somma 1-> sottrazione 2-> moltiplicazione 3-> divisione"))
n1=float(input("Dammi il primo numero: "))
n2=float(input("Dammi il secondo numero"))
calcoli={0: n1+n2, 1:n1-n2, 2:n1*n2, 3:n1/n2}
print(calcoli[n])