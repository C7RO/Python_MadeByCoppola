rubrica={"luca":380, "marco":120}
nome=input("Dammi il nome: ")
print(rubrica[nome])
nuovo_amico=input("Dammi il nome da aggiungere: ")
nuovo_telefono=input("Dammi il numero: ")
rubrica.append(nuovo_amico, nuovo_telefono)
print(rubrica)