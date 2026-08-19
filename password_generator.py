############################################
###      Random password generator       ###
###                                      ###
###              By Anthony              ###
###                                      ###
###                  V1                  ###
############################################

import pyperclip, secrets, string
from colorama import Style, init

# For Colorama, if you want the autoreset:
# init(autoreset=True)

# Beginning of the program
password = ""

length = -1 # Initial value to enter the while loop
upper = -1
lower = -1
spe_char = -1
nb = -1

def def_length(length=-1):
    while type(length) != int or not 5 <= length <= 20:
        length = int(input(Style.BRIGHT + "What length / How many characters?" + Style.RESET_ALL + " (Between 5 and 20)\n--> "))
        return length


def def_upper(upper=-1):    
    while type(upper) != bool:
        upper = input(Style.BRIGHT + "Uppercase letters?" + Style.RESET_ALL + " Y/N\n--> ")
        if upper.lower() in ["o", "oui", "ou", "yes", "y"]:
            upper = True
            return upper
        elif upper.lower() in ["n", "non", "no", ""]:
            upper = False
            return upper
        else:
            print("You need to answer Yes or No.")
            upper = -1

def def_lower(lower=-1):
    while type(lower) != bool:
        lower = input(Style.BRIGHT + "Lowercase letters?" + Style.RESET_ALL + " Y/N\n--> ")
        if lower.lower() in ["o", "oui", "ou", "yes", "y"]:
            lower = True
            return lower
        elif lower.lower() in ["n", "non", "no", ""]:
            lower = False
            return lower
        else:
            print("You need to answer Yes or No.")
            lower = -1

def def_spe_char(spe_char=-1):
    while type(spe_char) != bool:
        spe_char = input(Style.BRIGHT + "Special characters?" + Style.RESET_ALL + " Y/N\n--> ")
        if spe_char.lower() in ["o", "oui", "ou", "yes", "y"]:
            spe_char = True
            return spe_char
        elif spe_char.lower() in ["n", "non", "no", ""]:
            spe_char = False
            return spe_char
        else:
            print("You need to answer Yes or No.")
            spe_char = -1

def def_nb(nb=-1):
    while type(nb) != bool:
        nb = input(Style.BRIGHT + "Numbers?" + Style.RESET_ALL + " Y/N\n--> ")
        if nb.lower() in ["o", "oui", "ou", "yes", "y"]:
            nb = True
            return nb
        elif nb.lower() in ["n", "non", "no", ""]:
            nb = False
            return nb
        else:
            print("You need to answer Yes or No.")
            nb = -1

length = def_length()
upper = def_upper()
lower = def_lower()
spe_char = def_spe_char()
nb = def_nb()

# while 1 of the 4 attributes is not chosen
while not upper and not lower and not spe_char and not nb:
    choice = -1
    while type(choice) != int or choice not in [1, 2, 3, 4]:
        choice = int(input("You need to " + Style.BRIGHT + "choose" + Style.RESET_ALL + " at least 1 of the 4 attributes (1, 2, 3 or 4):" + Style.BRIGHT + "\n1. Uppercase letters\n2. Lowercase letters\n3. Special characters\n4. Numbers" + Style.RESET_ALL + "\n--> "))
    if choice == 1:
        upper = def_upper()
    elif choice == 2:
        lower = def_lower()
    elif choice == 3:
        spe_char = def_spe_char()
    elif choice == 4:
        nb = def_nb()

# Adding elements that meet the selected criteria to a large string
final = ""
if upper:
    final += string.ascii_uppercase
if lower:
    final += string.ascii_lowercase
if spe_char:
    final += string.punctuation
if nb:
    final += string.digits

# Password creation
while len(password) != length:
    password += secrets.choice(final) # Adding a character in the password

print(password)

pyperclip.copy(password)
print("Password copied!")