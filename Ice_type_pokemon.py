"""Discussion: Pokemon by Ian Rowe"""
class Pokemon:
    basic_attack = 'tackle'
    damage = 40

    def __init__(self, name, trainer):
        self.name = name
        self.trainer = trainer
        self.level = 1
        self.hp = 50
        self.paralyzed = False

    def speak(self):
        print(self.name + '!')

    def attack(self, other):
        if not self.paralyzed:
            self.speak()
            print(self.name, ' used ', self.basic_attack, '!')
            other.receive_damage(self.damage)

    def receive_damage(self, damage):
        self.hp = max(0, self.hp - damage)
        if self.hp == 0:
            print(self.name, ' fainted!')


class IceType(Pokemon):

    basic_attack = "Freeze Shock"
    prob = .3

    def __init__(self, name, trainer, hp=None):
        super().__init__(name, trainer)
        if hp is not None:
            self.hp = hp

    def __str__(self):
        ice_str = "Pokemon name: {}\t Trainer: {}\n" \
                  "Level: {}\tHP: {}".format(self.name, self.trainer, self.level, self.hp)
        return ice_str

    def attack(self, other):
        if isinstance(other, FireType) or isinstance(other, WaterType) or isinstance(other, IceType):
            self.damage = Pokemon.damage / 2
        elif isinstance(other, FlyingType) or isinstance(other, GrassType) or isinstance(other, DragonType):
            self.damage = Pokemon.damage * 2
        super().attack(other)
        if random() < self.prob and type(other) != IceType:
            other.paralyzed = True
            print(other.name, "is paralyzed!")
