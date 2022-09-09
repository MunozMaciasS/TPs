#Cree par Samuel Munoz
#Cree en septembre 2022
#But:compter les nombres des mots dans un pharase syntaxique ou pas syntaxique

phrase = input("ecrivez une phrase quelconque")
nbr_des_mots = str(len(phrase.split(" "))) #on se pare les mots en diffrents sous chianes et on nomme les nbr des chaines
print("il y a",nbr_des_mots,"mots") #on print le resultat


