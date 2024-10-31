from .singlton_system import SingletonSystem
from random import choice
from entities import *


class EntitySystem(SingletonSystem):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self.entities: list[Entity] = []
            self.initialized = True

    def spawn_entities(self):
        self.entities = [choice([BaseEnemy()]) for _ in range(5)]

    @property
    def get_entities(self):
        return self.entities
