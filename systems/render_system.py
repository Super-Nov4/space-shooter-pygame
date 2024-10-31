from .singlton_system import SingletonSystem
from abc import ABC, abstractmethod
from pygame.surface import Surface
from pygame import draw


class BaseRenderer(ABC):
    @abstractmethod
    def render(self, _surface, _obj):
        """Абстрактный метод для отрисовки объекта. Должен быть переопределен в подклассах."""


class RectRenderer(BaseRenderer):
    def render(self, _surface: Surface, _obj):
        draw.rect(_surface, 'white', _obj.rect)


class SpriteRenderer(BaseRenderer):
    def render(self, _surface: Surface, _obj):
        _surface.blit(_obj.components['Sprite'].sprite, _obj.components['Sprite'].rect)


class RenderSystem(SingletonSystem, SpriteRenderer, RectRenderer):
    def __init__(self):
        if not hasattr(self, 'initialized'):
            self._render_queue = []
            self.initialized = True

    def set_render_objects(self, objects) -> None:
        """
        Инициализирует очередь отрисовки, сортируя объекты по z_index.
        :return: None
        """
        self._render_queue = objects
        # self._initialize_render_queue()

    def render_objects(self, _surface: Surface) -> None:
        """
        Отрисовывает объекты на экране в порядке z_index
        :return: None
        """
        for entity in self._render_queue:
            if entity.get_component('Sprite'):
                self.render(_surface, entity)

    def _initialize_render_queue(self) -> None:
        """
        Инициализирует очередь отрисовки, сортируя объекты по z_index.
        :return: None
        """
        self._render_queue.sort(key=lambda obj: obj.z_index)
