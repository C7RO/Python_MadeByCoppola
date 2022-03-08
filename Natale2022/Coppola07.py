#Il file prezzi.csv (separatore ;) contiene le serie storiche mensili dei
#prezzi di alcuni generi alimentari dal Settembre 2011 a Dicembre
#2016. Immagina una spesa costituita da 5 generi alimentari a tua
#scelta e crea una lista contenente la serie storica del prezzo della tua
#spesa ottenuta sommando i prezzi dei generi alimentari scelti.
#Calcola mese / anno in cui la tua spesa ha costi minimi e massimi.

def main():
    prezzo_spesa=[]
    mesi=[]
    prodotti=[]
    f=open("./prezzi.txt","r")

    testo=f.readline()
    prodot=testo.split(";")
    prodot.pop(0)
    prodot.pop(0)
    for l in prodot:
        prodotti.append(l)

    testo=f.readlines()
    for riga in testo:
        somma=0
        campi=riga.split(";")
        mesi.append(campi[1]+campi[0])
        campi.pop(0)
        campi.pop(0)
        for l in range(len(prodotti)-2):
            somma+=float(campi[l])
            prezzo_spesa.append(somma)
    print(prezzo_spesa)

if __name__ =="__main__":
    main()