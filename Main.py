import random


def printas(name: str, text: str):
    print("[" + name.upper() + "] : " + text)


def resultatfpc(choix: int, choix2: int) -> bool:
    if choix == 1:
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


class Character:
    def __init__(self, _name: str, _damage: int, _life: int):
        self.name = _name
        self.damage = _damage
        self.life = self.maxLife = _life

    def status(self):
        print("[" + self.name + "] | Vie : " + str(self.life) + " \\ " + str(self.maxLife))


myChar = Character("Allegorie", 10, 100)
myChar.status()

# -----------INTRO--------
print("----------------------------------------------------------------")
print("Dans cette aventure, vous jouez Allegorie, un fière cowboy...")
print("----------------------------------------------------------------")

print("Allégorie rentre dans le bar de la ville pour commander un rafraichissement.")
drink = 0
while int(drink) != 1:
    printas("barman", "On a plusieurs choix de rafraichissement, fais ton choix !")
    drink = input("[1] : Jus de cactus / [2] : Bière / [3] : Whisky : ")
    if int(drink) != 1:
        printas("barman", "C'est pas vraiment une boisson pour toi, concentre toi bien et fais le bon choix")

printas(myChar.name, "J'ai fait le bon choix !")

# Rencontre avec Julien
printas("julien",
        "Bonjour, je suis Julien, et j'ai trouvé un moyen très "
        "simple de se faire de l'argent facilement depuis chez soi !")

# Papier Feuille Ciseau
# CHOIX
resultat = ""
while not resultat:
    printas("julien", "On va s'affronter a Pierre Feuille Ciseau, choisis ton élement :")
    choixJulien = random.randint(1, 3)
    choixUser = int(input("[1] : Pierre / [2] : Feuille / [3] : Ciseau : "))
    while choixUser < 1 or choixUser > 3:
        printas("narrateur", "Choix incorrect, assurez vous de choisir une des trois options")
        choixUser = int(input("[1] : Pierre / [2] : Feuille / [3] : Ciseau : "))
    # Execution
    printas("narrateur", "Alors qu'Allegorie a choisis de faire " + choixfpc(choixUser) +
            ", Julien a lui décidé de faire " + choixfpc(choixJulien))
    resultat = resultatfpc(choixUser, choixJulien)
    if resultat:
        printas("julien",
                "Tu as gagné le droit d'avoir mon secret pour atteindre la richesse sans bouger de chez toi !")
    else:
        printas("julien", "Tu as perdu,désolé, je te donnerais pas mon secret, essaye encore !")
