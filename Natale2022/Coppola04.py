#Implementare il gioco Forza 4 in Python utilizzando soltanto il
#terminale (https://it.wikipedia.org/wiki/Forza_quattro)

#Made by Coppola, DO NOT TOUCH WITHOUT PERMISSION OF THE ONLY COPPOLA, thanks

def formattaCampo(n):
    campo=[]
    for k in range(n):
        riga =[]
        for j in range(n):
            riga.append(" ")
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
    if r >= n-4:
        k=0
        win=True
        while k <= 3 and win == True:
            if campo[r-k][c]!=campo[r][c]:
                win=False
            k+=1  
        if win==True: return True     
        if c >= n-4:
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
    if r <= n-4:
        k=0
        win=True
        while k <= 3 and win == True:
            if campo[r+k][c]!=campo[r][c]:
                win=False
            k+=1   
        if win==True: return True            
        if c >= n-4:   
            k=0
            win=True
            while k <= 3 and win == True:
                if campo[r+k][c-k]!=campo[r][c]:
                    win=False
                k+=1  
            if win==True: return True             
        if c <= n-4:  
            k=0
            win=True
            while k <= 3 and win == True:
                if campo[r+k][c+k]!=campo[r][c]:
                    win=False
                k+=1    
            if win==True: return True        
    if c >= n-4:
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
    righe=0
    colonne=0
    vittoria=False
    while righe < n and vittoria == False:
        while colonne < n and vittoria == False:
            if campo[righe][colonne]==car:
                vittoria=is4(campo,righe,colonne,n)
            colonne+=1
        righe+=1
    return vittoria

def isLibera(campo, n, r, c):
    libera=False
    if r >= 0 and r < n and c>= 0 and c < n:
        if campo[r][c]==" ":
            libera=True
    return libera

n=5#Changing this little number you can choise the size of the map
campo= formattaCampo(n)
partitaFinita=False
car1="X"
car2="0"
mossag1=[0,0]
mossag2=[0,0]
stampaCampo(campo,n)
while(partitaFinita==False):
    mossag1[0]=int(input("Giocatore 1 dammi la mossa(0-"+str(n-1)+")(0-"+str(n-1)+"): ")) #chiedere mossa g1
    mossag1[1]=int(input("Colonna: "))
    while(isLibera(campo,n,mossag1[0],mossag1[1])==False):  #verifica cella libera
        print("Cella già occupata!!\n")
        mossag1[0]=int(input("Giocatore 1 dammi la mossa(0-"+str(n-1)+")(0-"+str(n-1)+"): "))
        mossag1[1]=int(input("Colonna: "))
    campo[mossag1[0]][mossag1[1]]=car1
    stampaCampo(campo,n)#stampa griglia
    if(controllaVittoria(campo,n,car1)):    #controlla Vittoria
        print("Complinti, il g1 ha vinto!!!")
        partitaFinita=True
    else:
        mossag2[0]=int(input("Giocatore 2 dammi la mossa(0-"+str(n-1)+")(0-"+str(n-1)+"): ")) #chiedere mossa g1
        mossag2[1]=int(input("Colonna: "))
        while(isLibera(campo,n,mossag2[0],mossag2[1])==False):  #verifica cella libera
            print("Cella già occupata!!\n")
            mossag2[0]=int(input("Giocatore 2 dammi la mossa(0-"+str(n-1)+")(0-"+str(n-1)+"): "))
            mossag2[1]=int(input("Colonna: "))
        campo[mossag2[0]][mossag2[1]]=car2
        stampaCampo(campo,n)#stampa griglia
        if(controllaVittoria(campo,n,car2)):    #controlla Vittoria
            print("Complinti, il g2 ha vinto!!!")
            partitaFinita=True