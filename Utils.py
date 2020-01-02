import random
import time


# JEU DU Feuille Papier Ciseau
def excusebidon() -> str:
    excuses = [
        "J'ai eternué",
        "T'as triché, je t'ai vue !",
        "Ma grand-mère est mourrante"
    ]

    return excuses[random.randint(0, len(excuses) - 1)]


def resultatfpc(choix: int, choix2: int) -> int:
    if choix == choix2:
        return 2
    elif choix == 1:
        return choix2 == 3
    elif choix == 2:
        return choix2 == 1
    elif choix == 3:
        return choix2 == 2


def choixfpc(choix: int) -> str:
    if choix == 1:
        return "Pierre"
    elif choix == 2:
        return "Feuille"
    elif choix == 3:
        return "Ciseau"


# Aide a l'affichage
def loadingbar(nbrsecond: int, timespeed: int = 1) -> None:
    for i in range(1, nbrsecond):
        print('.', end='')
        time.sleep(1 / timespeed)


def printas(name: str, text: str) -> None:
    print("[" + name.upper() + "] : " + text)


# Minijeu Marianne
tabDirection = ["à gauche", "devant", "à droite"]


def directionobstacle(direction: int) -> str:
    return tabDirection[direction]


def checksuccess(direction: int, text: str) -> bool:
    if text != "gauche" and text != "droite" and text != "saut":
        print("L'action n'est pas correct (faute de frappe ?)")
        return False
    elif direction == 0 and text == "droite" \
            or direction == 1 and text == "saut" \
            or direction == 2 and text == "gauche":
        return True
    else:
        return False


# Minijeu : Pendu


graphique = [['|', '-', '-', '|', '-'],
             ['|', '/', '', 'o', ''],
             ['|', '', '/', '|', '\\'],
             ['|', '\\', '/', '', '\\'],
             ['_', '_', '_', '_', '_']
             ]

zone = [[3, 3, 3, 3, 3],
        [2, 3, 4, 4, 4],
        [2, 4, 4, 4, 4],
        [2, 2, 4, 4, 4],
        [1, 1, 1, 1, 1]
        ]

words = ["voiture", "avion", "esclavage", "pourriture", "communiste", "baseball", "hamburger", "parentale"]


def motrandom() -> str:
    return words[random.randint(0, len(words) - 1)]


def afficherpendu(index: int) -> None:
    ligneindex = 0
    colonneindex = 0
    for l in graphique:
        for i in l:
            if zone[ligneindex][colonneindex] <= index:
                print(i, end='')
            colonneindex += 1
        print("")
        ligneindex += 1
        colonneindex = 0


def checkcharacter(charac: str, mot: str) -> int:
    bufferindex = mot.find(charac)
    if bufferindex == -1:
        print("Not in the word")
    else:
        print("Trouvé !")

    return bufferindex


def mot(lettre, mot) -> str:
    buffer = ""
    for b in mot:
        if b in lettre:
            buffer += b
        else:
            buffer += "*"
    return buffer
