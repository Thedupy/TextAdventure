import random

import Utils
from Character import Character

myChar = Character("Allegorie", 10, 100)
myChar.status()

# -----------INTRO--------
print("----------------------------------------------------------------")
print("Dans cette aventure, vous jouez Allegorie, un fière cowboy...")
print("----------------------------------------------------------------")

print("Allégorie rentre dans le bar de la ville pour commander un rafraichissement.")
drink = 0
while int(drink) != 1:
    Utils.printas("barman", "On a plusieurs choix de rafraichissement, fais ton choix !")
    drink = int(input("[1] : Jus de cactus / [2] : Bière / [3] : Whisky : "))
    if int(drink) != 1:
        Utils.printas("barman", "C'est pas vraiment une boisson pour toi, concentre toi bien et fais le bon choix")

Utils.printas(myChar.name, "J'ai fait le bon choix !")

# Rencontre avec Julien
Utils.printas("julien",
              "Bonjour, je suis Julien, et j'ai trouvé un moyen très "
              "simple de se faire de l'argent facilement depuis chez soi !")

Utils.printas("julien",
              "Je te défie a un Pierre Feuille Ciseau, si je gagne, tu devras faire quelque chose pour moi, "
              "mais si tu g")

# Papier Feuille Ciseau
# CHOIX
resultat = ""
Utils.printas("julien", "On va s'affronter a Pierre Feuille Ciseau, choisis ton élement :")
while resultat != 0:
    choixJulien = random.randint(1, 3)
    choixUser = int(input("[1] : Pierre / [2] : Feuille / [3] : Ciseau : "))
    while choixUser < 1 or choixUser > 3:
        Utils.printas("narrateur", "Choix incorrect, assurez vous de choisir une des trois options")
        choixUser = int(input("[1] : Pierre / [2] : Feuille / [3] : Ciseau : "))
    # Execution
    Utils.printas("narrateur", "Alors qu'Allegorie a choisis de faire " + Utils.choixfpc(choixUser) +
                  ", Julien a lui décidé de faire " + Utils.choixfpc(choixJulien))
    resultat = Utils.resultatfpc(choixUser, choixJulien)
    if resultat == 1:
        Utils.printas("julien",
                      Utils.excusebidon() + ", on est obligé de recommencer !")
    elif resultat == 0:
        Utils.printas("julien", "Tu as perdu, tu dois donc me rendre un p'tit service !")
    else:
        Utils.printas("julien", "Egalité, on recommence")

# TODO CHOIX OBJET
# Utils.printas("narrateur", "Alors qu'Allegorie se dirige vers sa tortue Marianne, il entend une voix qui l'appelle")
# Utils.printas("marchande",
#                   "Eh toi, avant de partir, passe donc par ma boutique, j'ai tout ce qu'il te faut pour tuner ")
# Utils.printas("marchande", "Tu as le choix entre 3 objet, attention tu ne peux en prendre qu'un")
# choixObjet = int(input("[1] : Pot Debridé / [2] : Carapace fibre de verre / [3] : Jantes chromées : "))


# TODO MINIJEU MARIANNE


# TODO MINIJEU RECHERCHE CACTUS JUTEUX
