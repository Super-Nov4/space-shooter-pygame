from pygame.image import load


class AssetManager:
    _instance = None
    _cached_bullets = {}
    _cached_enemies = {}
    _cached_player = {}

    def __new__(cls):
        if cls._instance is None:
            super(AssetManager, cls).__new__(cls)
            return cls

    def preload_all_assets(self):
        ...
