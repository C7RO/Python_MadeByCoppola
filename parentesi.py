#1) chiedere stinga a un utente

stringa=input("Dammi la stringa: ")
parentesi=[]
ok=True
conta=0
k=0
while k < len(stringa) and ok== True:
    if stringa[k]== '(' or stringa[k] == '[' or stringa[k]== '{':
        parentesi.append(stringa[k])
        conta+=1
    if stringa[k]== ')' or stringa[k] == ']' or stringa[k]== '}':
        if conta> 0:
            if chr(ord(parentesi[conta-1])+1) != stringa[k] and chr(ord(parentesi[conta-1])+2) != stringa[k]:
                ok= False
            else:
                parentesi.pop()
                conta-=1
        else : ok=False
    k+=1
if ok:
    print("Parentesi corrette")
else:
    print("Parentesi non corrette")