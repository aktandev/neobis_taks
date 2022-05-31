class PokeScan:
    def __init__(self, name, level, pkmntype):
        self.name = name
        self.level = level
        self.pkmntype = pkmntype

    @property
    def element(self):
        return {'water': 'wet', 'fire': 'fiery', 'grass': 'grassy'}.get(self.pkmntype)

    @property
    def strength(self):
        return 'strong' if self.level > 50 else 'fair' if self.level > 20 else 'weak'

    def info(self):
        return f'{self.name}, a {self.element} and {self.strength} Pokemon.'



print(PokeScan('Squirtle', 100, 'water').info(),)
print(PokeScan('Charmander', 0, 'fire').info())
print(PokeScan('Bulbasaur', 0, 'grass').info())