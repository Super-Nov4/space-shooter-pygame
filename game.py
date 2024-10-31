from systems.entity_system import EntitySystem
from systems.render_system import RenderSystem
from utils.asset_manager import AssetManager
from os import system
from sys import exit
import pygame.event


class Game:
    def __init__(self):
        self.fps = 60
        self.width = 600
        self.height = 750
        self.entities = []
        self.clock = pygame.time.Clock()
        self.asset_manager = AssetManager()
        self._render_system = RenderSystem()
        self._entity_system = EntitySystem()
        self.window = pygame.display.set_mode((self.width, self.height))

    def _restart(self):
        ...

    def start(self):
        while True:
            self.event_loop()
            self.window.fill("black")

            self.asset_manager.preload_all_assets()

            self._entity_system.spawn_entities()
            self._render_system.set_render_objects(self._entity_system.get_entities)
            self._render_system.render_objects(self.window)

            pygame.display.flip()
            self.clock.tick(self.fps)

    @staticmethod
    def event_loop():
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_ESCAPE]:
                pygame.quit()
                system("cls")
                exit()


if __name__ == "__main__":
    pygame.mixer.init()
    pygame.init()
    g = Game()
    g.start()
