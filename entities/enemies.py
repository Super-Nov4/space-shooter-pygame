from components.velocity import VelocityComponent
from components.position import PositionComponent
from components.sprite import SpriteComponent
from .entity import Entity
from pprint import pp


class BaseEnemy(Entity):
    def __init__(self):
        super().__init__()
        self.add_component("Velocity", VelocityComponent(0, 0))
        self.add_component("Position", PositionComponent(0, 0))
        self.add_component("Sprite", SpriteComponent(self.asset_manager.get_cached("ship0")))
        self.z_index = 0
