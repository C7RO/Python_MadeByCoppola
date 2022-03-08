"""
012X
X34X
5678
XXX9
"""

def main():
    mappa = [[0,0,0,1], [1,0,0,1], [0,0,0,0], [1,1,1,0]]
    nrighe=4
    ncolonne=4

    Movimenti={}

    for i,k in enumerate(mappa):
        for i2, j in enumerate(k):
            if j!= 0:
                Movimenti[i,i2]="Muro"
            else:
                Movimenti[i,i2]=""
                if i> 0:
                    if mappa[i-1][i2]==0:
                        Movimenti[i,i2]=Movimenti[i,i2]+"sopra "
                if i< nrighe-1:
                    if mappa[i+1][i2]==0:
                        Movimenti[i,i2]=Movimenti[i,i2]+"sotto "
                if i2> 0:
                    if mappa[i][i2-1]==0:
                        Movimenti[i,i2]=Movimenti[i,i2]+"sinistra "
                if i2< ncolonne-1:
                    if mappa[i][i2+1]==0:
                        Movimenti[i,i2]=Movimenti[i,i2]+"destra "

    print(Movimenti)

if __name__=="__main__":
    main()