#Scrivere un programma che data una lista qualsiasi ne elimini i duplicati.

def eliminaDoppioni(l):
    for k in range(len(l)-1):
        j=k+1
        while j< len(l):
            if l[j] in l[:k+1]:#if l[k] ==l[j]: 
               l=l[:j]+l[j+1:] 
               j-=1
            j+=1
    return l

lista=[3,3,3,3,4,4,4,1,2,3,4,5,6,4,2,2,1,2,3,4,5,6,7,8,9,0,11,6,4,10,3]
lista=eliminaDoppioni(lista)
print(lista)
