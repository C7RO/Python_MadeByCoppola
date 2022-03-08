def bin2dec(bin):
    num=0
    for i,k in enumerate(bin[::-1]):
        num+=2**(i)*int(k)
    return num

def dec2bin(num, nbit):
    s=bin(num)[2:]
    s="0"*(nbit-len(s))+s
    return s

def IP_dec2bin(stringa):
    s=""
    ip=stringa.split(".")
    for i in ip:
        s+=dec2bin(int(i),8)
    return s

def IP_bin2dec(stringa):
    s=""
    for k in range(4):
        i=stringa[0+k*8:8+k*8]
        s+= str(bin2dec(i))+"."
    return s[:-1]
    
def calcolaSubnetMask(bit):
    bit=calcolaNbit(bit)
    indirizzo=""
    conta=0
    for n in range(4):
        sommabit=0
        for b in range(8):
            if(conta>= bit):
                break
            sommabit+=2 **(8-b-1)
            conta+=1
        indirizzo+=str(sommabit)+"."
    return indirizzo[:-1]

def calcolaNbit(stringa):
    if "/"in str(stringa):
        stringa=int(stringa[1:])
    if "."in str(stringa):
        stringa=IP_dec2bin(stringa)
        bit=0
        for k in stringa:
            bit+=int(k)
        stringa=bit
    return stringa

def calcolaIpRete(ip, nbit):
    nbit=calcolaNbit(nbit)
    ip=IP_dec2bin(ip)
    ip=ip[0:nbit]+"0"*(len(ip)-nbit)
    return IP_bin2dec(ip)

def calcolaIpBroadcast(ip, nbit):
    nbit=calcolaNbit(nbit)
    ip=IP_dec2bin(ip)
    ip=ip[0:nbit]+"1"*(len(ip)-nbit)
    return IP_bin2dec(ip)

def calcolaPrimoIp(ip, nbit):
    nbit=calcolaNbit(nbit)
    ipRete=calcolaIpRete(ip, nbit)
    ipRete=IP_dec2bin(ipRete)
    ipRete=ipRete[0:-1]+str(1)
    return IP_bin2dec(ipRete)

def calcolaUltimoIp(ip, nbit):
    nbit=calcolaNbit(nbit)
    ipBroadCast=calcolaIpBroadcast(ip, nbit)
    ipBroadCast=IP_dec2bin(ipBroadCast)
    ipBroadCast=ipBroadCast[0:-1]+str(0)
    return IP_bin2dec(ipBroadCast)
        

def main():
    ip="172.16.1.4"
    bit="/20"
    print(ip+" "+str(bit))
    ip=calcolaIpRete(ip,bit)
    print(f"Ip corretto:{ip}")
    print(calcolaSubnetMask(bit))
    ip_broadcast=calcolaIpBroadcast(ip,bit)
    print(f"Broadcast: {ip_broadcast}")
    print(calcolaPrimoIp(ip, bit))
    print(calcolaUltimoIp(ip, bit))
    

if __name__=="__main__":
    main()