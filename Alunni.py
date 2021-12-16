def main():
    nome=input("Dammi il nome dell'alunno(0 per interrompere il programma): ")
    f=open("./testo.txt","w")
    while(nome != "0"):
        voto=int(input("Dammi il voto in condotta: "))
        f.write(nome[0]+("*"*(len(nome)-1))+","+str(voto)+"\n")
        nome=input("Dammi il nome dell'alunno(0 per interrompere il programma): ")
    f.close()

if __name__ == "__main__":
    main()