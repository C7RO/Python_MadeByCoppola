#slicing
stringa = "classe quarta A robotica"
print(f"il primo carattere è: {stringa[0]}")
print(f"L'ultimo carattere è: {stringa[-1]}")
print(stringa[3:9])#slicing di stringhe
print(f"ciao:{stringa[6:]}")
print(stringa[2:14:2])#slicing step, stampa dal car 2 al 13 con balzi di 2
print(stringa[::-1])#inverte stringa
stringa_n= stringa[:14]+ "B"+stringa[15:]
print(stringa_n)