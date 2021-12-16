nome=input("Dammi il nome: ")
cognome=input("Dammi il cognome: ")

giorno=int(input("Dammi il giorno di nascita: "))
mese=int(input("Dammi il mese di nascita: "))
anno=int(input("Dammi l'anno di nascita: "))

rubrica={"nome" : nome, "cognome":cognome, "data":str(giorno)+"/"+str(mese)+"/"+str(anno)}
f=open("rubrica.txt","w")
f.write(rubrica["nome"]+","+rubrica["cognome"]+","+rubrica["data"]+"\n")
f.close()