isPalindroma= lambda stringa: (stringa == stringa[::-1])

isMaiuscola = lambda stringa: (stringa[0]>= 'A') & (stringa[0]<= 'Z')

stringhe=["Ciao", "marco","Anna", "gioia", "anna"]
stringa_Maiuscola=[nome for nome in stringhe if(isMaiuscola(nome))]
print(stringa_Maiuscola)
stringa_Palindroma=[parola for parola in stringhe if(isPalindroma(parola))]
print(stringa_Palindroma)