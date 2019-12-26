import random


def printas(name: str, text: str):
    print("[" + name.upper() + "] : " + text)


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
