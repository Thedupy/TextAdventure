def printas(name: str, text: str):
    print("[" + name.upper() + "] : " + text)


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
        "Bonjour, je suis Julien, et j'ai trouvé un moyen très simple de se faire de l'argent facilement depuis chez soi !")
