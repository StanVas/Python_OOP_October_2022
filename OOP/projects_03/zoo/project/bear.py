from projects_03.players_and_monsters.project import Lizard
from projects_03.players_and_monsters.project import Mammal


class Bear(Mammal):
    def __init__(self, name):
        super().__init__(name)


mammal = Mammal("Stella")
print(mammal.__class__.__bases__[0].__name__)
print(mammal.name)
lizard = Lizard("John")
print(lizard.__class__.__bases__[0].__name__)
print(lizard.name)
