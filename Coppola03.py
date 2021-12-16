def calcolaSubnetMask(bit):
    indirizzo=""
    conta=0
    for n in range(4):
        sommabit=0
        for b in range(8):
            if(conta>= bit):
                break
            sommabit+=2 **(8-b-1)
            conta+=1
            
        indirizzo+=str(sommabit)
        if n < 3:
            indirizzo+="."
    return indirizzo

ip_address=["192.168.222.0/27","192,168.100.0/24","192.168.200.0/28","192.168.50.0/22"]
separatore=[ip.split("/") for ip in ip_address]
subnet=[calcolaSubnetMask(int(separatore[k][1]))for k in range(4)]
f=open("./mask.txt","w")
for mask in subnet:
    f.write(mask+"\n")

f.close()