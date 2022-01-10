#Scrivere un programma che data una lista qualsiasi la trasformi in un
#dizionario avente come chiavi gli indici della lista e come valori gli
#elementi.

def formaDizionario(l):
    dizionario={}
    for k in range(len(l)):#for k, elemento in enumerate(lista):
        dizionario[k]=l[k]#dizionario={k: elemento for k,elemento in enumarate(lista)}
    return dizionario

lista=[5,4,3,2,1]
print(formaDizionario(lista))
