from os.path import join, abspath
from pygame.image import load
from pygame.mixer import Sound
from pygame.mixer import music
from pygame import Surface
from os import listdir
import sys


class AssetManager:
    _instance = None
    _cached_planets = {}
    _cached_bullets = {}
    _cached_enemies = {}
    _cached_player = {}
    _cached_music = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(AssetManager, cls).__new__(cls)
        return cls._instance

    def get_cached(self, file_name: str) -> Surface | Sound:
        """
        Returns a loaded sprite or sound stored in dictionary
        :return: Surface | Sounds
        """
        if file_name in self._cached_player:
            return self._cached_player.get(file_name)
        elif file_name in self._cached_enemies:
            return self._cached_enemies.get(file_name)
        elif file_name in self._cached_bullets:
            return self._cached_bullets.get(file_name)

    def preload_all_assets(self) -> None:
        """
        Preloading all game assets
        :return: None
        """

        # Preloading player assets
        self._cached_player["player_shoot.wav"] = Sound(self._return_file_path("player_shoot.wav"))
        self._cached_player["player_ship.png"] = load(self._return_file_path("player_ship.png"))

        # Preloading enemy assets
        self._cached_enemies["enemy_shoot.wav"] = Sound(self._return_file_path("enemy_shoot.wav"))
        self._cached_enemies["ship0.png"] = load(self._return_file_path("ship0.png"))
        self._cached_enemies["ship1.png"] = load(self._return_file_path("ship1.png"))
        self._cached_enemies["ship2.png"] = load(self._return_file_path("ship2.png"))

        # Preload planet assets
        self._cached_planets["blue_small_planet.png"] = load(self._return_file_path("black_hole.png"))
        self._cached_planets["green_planet.png"] = load(self._return_file_path("black_hole.png"))
        self._cached_planets["pink_planet.png"] = load(self._return_file_path("black_hole.png"))
        self._cached_planets["black_hole.png"] = load(self._return_file_path("black_hole.png"))

        # Preload bullet assets
        self._cached_bullets["pixel_laser_yellow.png"] = load(self._return_file_path("pixel_laser_yellow.png"))
        self._cached_bullets["pixel_laser_green.png"] = load(self._return_file_path("pixel_laser_green.png"))
        self._cached_bullets["pixel_laser_blue.png"] = load(self._return_file_path("pixel_laser_blue.png"))
        self._cached_bullets["pixel_laser_red.png"] = load(self._return_file_path("pixel_laser_red.png"))

        # Preload music assets
        self._cached_music["background_music.ogg"] = music.load("background_music.ogg")

    @staticmethod
    def _return_file_path(file_name: str) -> str:
        file_path = ""
        try:
            file_path = sys._MEIPASS
        except AttributeError:
            if file_name.endswith(".png"):
                file_path = abspath(f"assets/sprites/{file_name}")
            elif file_name.endswith(".ogg") or file_path.endswith(".ogg"):
                file_path = abspath(f"assets/sounds/{file_name}")

        return file_path
