#Scrivere un programma in Python che prenda in input il nome file di
#un programma scritto in C. Il programma deve leggere il file e:
#1. Contare il numero di righe totali
#2. Contare il numero di chiamate alla funzione “printf”
#3. Contare il numero di linee di commento.

f=open("./main.c","r")
testo=str(f.readlines())
contaRighe=0
contaPrint=0
contaCommenti=0
for n,l in enumerate(testo):
    if testo[n:n+2]=="\\n":
        contaRighe+=1
    if testo[n:n+6]=="printf":
        contaPrint+=1
    if testo[n:n+2]== "//" or testo[n:n+2]=="/*":
        contaCommenti+=1

print(contaRighe)
print(contaPrint)
print(contaCommenti)
f.close()