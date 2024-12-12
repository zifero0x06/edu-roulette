# -*-coding:Utf-8 -*

from random import randint
from math import ceil
import time

def nbre_pair(nbre):
    if nbre % 2 == 0:
        return True
    else:
        return False

print("")
print("~ ~ ~ Bienvenue au casino TÉFOCHÉ ~ ~ ~")
print("C'est parti pour quelques tours de roulette.")
print("Vous gagnez si vous trouvez le bon numéro (gain de 3 fois la mise) ou sa couleur (gain de 1,2 fois la mise).")
print("Autremment, vous perdez la somme misée.")
print("Dans tous les cas, rappelez-vous que c'est toujours le casino qui gagne à la fin ;)")
print("")
somme = 30
print("Votre somme de départ est fixée à " + str(somme) + "€.")
print("")
continuer = True

# Démarrons la partie et permettons au joueur de quitter la partie s'il le souhaite
while continuer:
    quitter = input("Si vous souhaitez quitter la partie, pressez la touche 'q' sinon pressez n'importe quelle touche : ") 
    if quitter == 'q' or somme == 0:
        print("Vous quittez la table de roulette avec la somme de : " + str(somme) + "€ en main. A bientôt !")
        continuer = False
        break
    
    # Définissons la mise et controlons sa valeur
    mise_existe = False
    while mise_existe is False:
        mise = input("Saisissez le montant de votre mise pour la prochaine partie : ")
        try:
            mise = int(mise)
            if mise > somme:
                print("Vous n'avez pas assez d'argent pour effectuer une telle mise.")
            else:
                mise_existe = True
                print("Vous avez parié la somme de " + str(mise) + "€.")
        except:
            print("Veuillez entrer un nombre valide.")
    
    # Définissons le choix du nombre sur lequel miser
    choix_existe = False
    while choix_existe is False:
        choix = input("Faîtes vos jeux, choisissez un nombre entre 1 et 50 [les nombres pairs sont noirs, les impairs sont rouges] : " )
        try:
            choix = int(choix)
            choix_existe = True
            if nbre_pair(choix):
                print(str(choix) + " pair noir, rien ne vas plus !")
            else:
                print(str(choix) + " impair rouge, rien ne vas plus !")
        except:
            print("Veuillez entrer un nombre valide.")

    time.sleep(0.9)
    # Procédons au tirage et annonçons le résultat
    print("C'est parti pour le tirage !")
    
    for i in ("La...", "  ...roulette...", "        ...tourne...", "  ...et..."):
        print(i)
        time.sleep(0.9)
    
    tirage = randint(0, 49) + 1
    if nbre_pair(tirage):
        print("     ..." + str(tirage) + " pair noir au résultat !")
    else:
        print("     ..." + str(tirage) + " impair rouge au résultat !")

    # Calculons les gains/pertes et mettons la somme posséder à jour    
    time.sleep(0.9)
    if choix == tirage:
        gain = mise * 3
        somme = somme + gain
        print("Quelle CHANCE ! Vous avez gagné " + str(gain) + "€ et vous avez désormais " + str(somme) +"€ en main.")
    elif (nbre_pair(tirage) == nbre_pair(choix)):
        gain = ceil(mise * 1.0) # Ajustement pour conserver la mise en cas favorable pair/impair
        # somme = somme + gain
        print("OUF ! Vous conservez vos " + str(gain) + "€ et vous avez donc " + str(somme) +"€ en main.")
    else:
        somme = somme - mise
        print("MINCE ! Vous avez perdu " + str(mise) + "€ et vous avez désormais " + str(somme) +"€ en main.")
