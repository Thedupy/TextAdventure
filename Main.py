import random
import time

import Utils
from Character import Character

# myChar = Character("Allegorie", 10, 100)
# myChar.status()
#
# # -----------INTRO--------
# print("----------------------------------------------------------------")
# print("Dans cette aventure, vous jouez Allegorie, un fière cowboy...")
# print("----------------------------------------------------------------")
#
# print("Allégorie rentre dans le bar de la ville pour commander un rafraichissement.")
# drink = 0
# while int(drink) != 1:
#     Utils.printas("barman", "On a plusieurs choix de rafraichissement, fais ton choix !")
#     drink = int(input("[1] : Jus de cactus / [2] : Bière / [3] : Whisky : "))
#     if int(drink) != 1:
#         Utils.printas("barman", "C'est pas vraiment une boisson pour toi, concentre toi bien et fais le bon choix")
#
# Utils.printas(myChar.name, "J'ai fait le bon choix !")
#
# # Rencontre avec Julien
# Utils.printas("julien",
#               "Bonjour, je suis Julien, et j'ai trouvé un moyen très "
#               "simple de se faire de l'argent facilement depuis chez soi !")
#
# Utils.printas("julien", "Je te défie a un Pierre Feuille Ciseau, si tu gagne, tu sera libre de partir, mais si je gagne, tu devras aller chercher du jus de cactus")
#
# # Papier Feuille Ciseau
# # CHOIX
# resultat = ""
# Utils.printas("julien", "On va s'affronter a Pierre Feuille Ciseau, choisis ton élement :")
# while resultat != 0:
#     choixJulien = random.randint(1, 3)
#     choixUser = int(input("[1] : Pierre / [2] : Feuille / [3] : Ciseau : "))
#     while choixUser < 1 or choixUser > 3:
#         Utils.printas("narrateur", "Choix incorrect, assurez vous de choisir une des trois options")
#         choixUser = int(input("[1] : Pierre / [2] : Feuille / [3] : Ciseau : "))
#     # Execution
#     Utils.printas("narrateur", "Alors qu'Allegorie a choisis de faire " + Utils.choixfpc(choixUser) + ", Julien a lui décidé de faire " + Utils.choixfpc(choixJulien))
#     resultat = Utils.resultatfpc(choixUser, choixJulien)
#     if resultat == 1:
#         Utils.printas("julien", Utils.excusebidon() + ", on est obligé de recommencer !")
#     elif resultat == 0:
#         Utils.printas("julien", "Tu as perdu, tu dois donc me rendre un p'tit service !")
#     else:
#         Utils.printas("julien", "Egalité, on recommence")


# TODO MINIJEU MARIANNE
# jeu obstacle : 5 secondes pour taper droite si obstacle a gauche, gauche si obstacle a droite
runSuccess = 0
runTimer = time.time()
runLength = 30
obstacleTimer = time.time()
nextObstacle = random.randint(1, 3)
while runSuccess != 1:
    time.sleep(1)
    print(".", end='')
    if time.time() - runTimer >= runLength:
        runSuccess = 1
    elif time.time() - obstacleTimer >= nextObstacle:
        #Affichage Obstacle
        obstacleDirection = random.randint(1, 3)
        print("Un Obstacle !")
        #Resolution Obstacle

        #Reset timer obstacle

        nextObstacle = random.randint(1, 10)
print("Sortie!")
