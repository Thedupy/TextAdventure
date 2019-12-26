class Character:
    def __init__(self, _name: str, _damage: int, _life: int):
        self.name = _name
        self.damage = _damage
        self.life = self.maxLife = _life

    def status(self):
        print("[" + self.name + "] | Vie : " + str(self.life) + " \\ " + str(self.maxLife))
