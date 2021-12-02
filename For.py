classi= ["4arob", "3achi", "5arob"]
dizionario={"rob":"robotica", "chi":"chimica"}
indice=0
for classe in classi:   #for numero in range(x, y) 
    print(f"La classe {classe} è dell'indirizzo {dizionario[classe[-3:]]} di indice {indice}\n\n")
    indice+=1