stringhe=["ciaoqwqwqwqwqwqwq", "marcooo", "Luigisalvadanaio"]
parola_lunga=stringhe[0]
for parola in stringhe[1:]:
    if len(parola_lunga)< len(parola):
        parola_lunga=parola
print(parola_lunga)
