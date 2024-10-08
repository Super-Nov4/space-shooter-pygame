from components.velocity import VelocityComponent
from components.position import PositionComponent
from components.sprite import SpriteComponent
from utils.asset_manager import AssetManager
from entity import Entity


class PlayerShip(Entity):
    def __init__(self):
        super().__init__()
        asset_manager = AssetManager()
        self.add_component("Velocity", VelocityComponent(0, 0))
        self.add_component("Position", PositionComponent(0, 0))
        self.add_component("Sprite", SpriteComponent(asset_manager.get_cached("player_ship")))

        """Здесь должна быть реализована стрельба, движение игрока?"""
