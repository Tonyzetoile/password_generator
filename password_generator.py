############################################
### Générateur de mot de passe en Python ###
###                                      ###
###             Par Anthony              ###
###                                      ###
###                  V1                  ###
############################################

import pyperclip, secrets, string
from colorama import Style, init

# Pour Colorama, si autoreset souhaité, décommenter ça :
# init(autoreset=True)

# Début du programme
mot_de_passe = ""

taille = -1 # Valeur initiale pour rentrer dans le while
maj = -1
min = -1
car_spe = -1
nb = -1

def def_taille(taille=-1):
    while type(taille) != int or not 5 <= taille <= 20:
        taille = int(input(Style.BRIGHT + "Quelle taille / Combien de caractères ?" + Style.RESET_ALL + " (Entre 5 et 20)\n--> "))
        return taille


def def_maj(maj=-1):    
    while type(maj) != bool:
        maj = input(Style.BRIGHT + "Majuscules ?" + Style.RESET_ALL + " O/N\n--> ")
        if maj.lower() in ["o", "oui", "ou", "yes", "y"]:
            maj = True
            return maj
        elif maj.lower() in ["n", "non", "no", ""]:
            maj = False
            return maj
        else:
            print("Vous devez répondre soit oui, soit non.")
            maj = -1

def def_min(min=-1):
    while type(min) != bool:
        min = input(Style.BRIGHT + "Minuscules ?" + Style.RESET_ALL + " O/N\n--> ")
        if min.lower() in ["o", "oui", "ou", "yes", "y"]:
            min = True
            return min
        elif min.lower() in ["n", "non", "no", ""]:
            min = False
            return min
        else:
            print("Vous devez répondre soit oui, soit non.")
            min = -1

def def_car_spe(car_spe=-1):
    while type(car_spe) != bool:
        car_spe = input(Style.BRIGHT + "Caractères spéciaux ?" + Style.RESET_ALL + " O/N\n--> ")
        if car_spe.lower() in ["o", "oui", "ou", "yes", "y"]:
            car_spe = True
            return car_spe
        elif car_spe.lower() in ["n", "non", "no", ""]:
            car_spe = False
            return car_spe
        else:
            print("Vous devez répondre soit oui, soit non.")
            car_spe = -1

def def_nb(nb=-1):
    while type(nb) != bool:
        nb = input(Style.BRIGHT + "Nombres ?" + Style.RESET_ALL + " O/N\n--> ")
        if nb.lower() in ["o", "oui", "ou", "yes", "y"]:
            nb = True
            return nb
        elif nb.lower() in ["n", "non", "no", ""]:
            nb = False
            return nb
        else:
            print("Vous devez répondre soit oui, soit non.")
            nb = -1

taille = def_taille()
maj = def_maj()
min = def_min()
car_spe = def_car_spe()
nb = def_nb()

# Tant que l'un des 4 critères n'est pas choisi
while maj == False and min == False and car_spe == False and nb == False:
    choix = -1
    while type(choix) != int or choix not in [1, 2, 3, 4]:
        choix = int(input("Vous devez " + Style.BRIGHT + "choisir" + Style.RESET_ALL + " au moins l'un des 4 critères suivants (1, 2 ou 3):" + Style.BRIGHT + "\n1. Majuscules\n2. Minuscules\n3. Caractères spéciaux\n4. Nombres" + Style.RESET_ALL + "\n--> "))
    if choix == 1:
        maj = def_maj()
    elif choix == 2:
        min = def_min()
    elif choix == 3:
        car_spe = def_car_spe()
    elif choix == 4:
        nb = def_nb()

# Ajout, dans une grande chaîne de caractères, des éléments appartenant aux critères choisi
final = ""
if maj:
    final += string.ascii_uppercase
if min:
    final += string.ascii_lowercase
if car_spe:
    final += string.punctuation
if nb:
    final += string.digits

# Création du mot de passe
while len(mot_de_passe) != taille:
    mot_de_passe += secrets.choice(final) # Ajout d'un caractère dans le mot de passe

print(mot_de_passe)

pyperclip.copy(mot_de_passe)
print("Mot de passe copié !")