#Il file covid-19_gen1.txt contiene la sequenza genomica RNA di un
#virus SARS-COV-2. L'RNA è una sequenza in cui si alternano 4
#simboli (detti nucleotidi): A, T, C, G. L'RNA del virus SARS-COV-2
#contiene 29903 nucleotidi. Leggi covid-19_gen1.txt il file e crea un
#dizionario Python avente come chiavi i nucleotidi A, T, C, G e come
#valori i rispettivi conteggi.

f=open("./covid-19_gen1.txt","r")
dizionario={"A":0,"T":0,"C":0,"G":0}
testo=str(f.readlines())
for n in testo:
    if n in dizionario:
        dizionario[n]+=1

#dizionario={c:dizionario2[c]+1 for c in testo if c in dizionario2}

print(dizionario)
f.close()