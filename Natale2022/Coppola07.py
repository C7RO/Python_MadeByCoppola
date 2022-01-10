#Il file prezzi.csv (separatore ;) contiene le serie storiche mensili dei
#prezzi di alcuni generi alimentari dal Settembre 2011 a Dicembre
#2016. Immagina una spesa costituita da 5 generi alimentari a tua
#scelta e crea una lista contenente la serie storica del prezzo della tua
#spesa ottenuta sommando i prezzi dei generi alimentari scelti.
#Calcola mese / anno in cui la tua spesa ha costi minimi e massimi.

prodotti=["Acqua minerale (cl. 900)","Birra nazionale (cl. 100)","Biscotti frollini (gr. 1000)"]
f=open("./prezzi.txt","r")
testo=str(f.readlines())
