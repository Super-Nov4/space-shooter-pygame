from components.velocity import VelocityComponent
from components.position import PositionComponent
from components.sprite import SpriteComponent
from entity import Entity


class PlayerShip(Entity):
    def __init__(self):
        super().__init__()
        self.add_component("Velocity", VelocityComponent(0, 0))
        self.add_component("Position", PositionComponent(0, 0))
        self.add_component("Sprite", SpriteComponent(self.asset_manager.get_cached("player_ship")))
