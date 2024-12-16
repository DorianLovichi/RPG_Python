import random
from Avatar import Avatar
from Stat import Stat


class Mobs(Avatar):
    def __init__(self, targs):
        super().__init__(targs)
        self._type = targs["type"]
        self._initial_life = targs.get("life", 100) 
        self._life = self._initial_life  

    @property
    def life(self):
        return self._life

    @life.setter
    def life(self, value):
        self._life = value

    def reset(self):
        self._life = self._initial_life  

    def __str__(self):
        return f"Mobs {self._type} {self._nom}, PV: {self._life}"
