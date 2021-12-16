p=open("./testo.txt","r")
testo=str(p.readlines())
nuovo_testo=""
num=int(input("Dammi il codice: "))
f=open("./testo.txt","w")

for k in range(2,len(testo)-2):
    nuovo_testo+= chr(ord(testo[k])+num)
    print(nuovo_testo)
f.write(f"{nuovo_testo}")

print(nuovo_testo)
print(testo)
nuovo_testo="" 

f.close()
p.close()