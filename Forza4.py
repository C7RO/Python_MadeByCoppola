#Implementare il gioco Forza 4 in Python utilizzando soltanto il
#terminale (https://it.wikipedia.org/wiki/Forza_quattro)

#Made by Coppola, DO NOT TOUCH WITHOUT PERMISSION OF THE ONLY COPPOLA, thanks

def formattaCampo(n):
    campo=[]
    for k in range(n):
        riga =[" "]*n
        campo.append(riga)
    return campo

def stampaCampo(campo, n):
    print(" ",end='')
    for r in range(n):
        print(r, end=' ')
    print("\n",end='')
    for k in range(n):
        print(k,end='')
        for j in range(n):
            print(campo[k][j], end='')
            if j< n-1:
                print("|",end='')
        print("\n",end='')

def is4(campo, r,c,n):
    win=False 
    if r >= 3:
        k=0
        win=True
        while k <= 3 and win == True:
            if campo[r-k][c]!=campo[r][c]:
                win=False
            k+=1  
        if win==True: return True     
        if c >= 3:
            k=0
            win=True
            while k <= 3 and win == True:
                if campo[r-k][c-k]!=campo[r][c]:
                    win=False
                k+=1
            if win==True: return True   
        if c <= n-4:    
            k=0
            win=True
            while k <= 3 and win == True:
                if campo[r-k][c+k]!=campo[r][c]:
                    win=False
                k+=1    
            if win==True: return True             
    if c >= 3:
        k=0
        win=True
        while k <= 3 and win == True:
            if campo[r][c-k]!=campo[r][c]:
                win=False
            k+=1  
        if win==True: return True   
    if c <= n-4:  
        k=0
        win=True
        while k <= 3 and win == True:
            if campo[r][c+k]!=campo[r][c]:
                win=False
            k+=1       
        if win==True: return True        
    return win

def controllaVittoria(campo, n, car):
    righe=n-1
    colonne=0
    vittoria=False
    while righe >= 0 and vittoria == False:
        while colonne < n and vittoria == False:
            if campo[righe][colonne]==car:
                vittoria=is4(campo,righe,colonne,n)
            colonne+=1
        righe-=1
    return vittoria

def isLibera(campo, n, c):
    k=n-1
    while (campo[k][c]=="X" or campo[k][c]=="0") and k >=0:
        k-=1
    return k

n=5#Changing this little number you can choise the size of the map
campo= formattaCampo(n)
partitaFinita=False
car1="X"
car2="0"
mossag1=0
mossag2=0
stampaCampo(campo,n)
while(partitaFinita==False):
    mossag1=int(input("Giocatore 1 dammi la mossa(0-"+str(n)+")")) #chiedere mossa g1
    while isLibera(campo,n,mossag1) < 0:  #verifica cella libera
        print("Colonna non disponibile\n")
        mossag1=int(input("Giocatore 1 dammi la mossa(0-"+str(n)+")")) #chiedere mossa g1

    campo[isLibera(campo,n,mossag1)][mossag1]=car1
    stampaCampo(campo,n)#stampa griglia
    if(controllaVittoria(campo,n,car1)):    #controlla Vittoria
        print("Complinti, il g1 ha vinto!!!")
        partitaFinita=True
    else:
        mossag2=int(input("Giocatore 2 dammi la mossa(0-"+str(n)+")")) #chiedere mossa g1
        while(isLibera(campo,n,mossag2) < 0):  #verifica cella libera
            print("Cella già occupata!!\n")
            mossag2=int(input("Giocatore 2 dammi la mossa(0-"+str(n)+")"))
        campo[isLibera(campo,n,mossag2)][mossag2]=car2
        stampaCampo(campo,n)#stampa griglia
        if(controllaVittoria(campo,n,car2)):    #controlla Vittoria
            print("Complinti, il g2 ha vinto!!!")
            partitaFinita=True