from pygame import Surface


class RenderSystem:

    def __init__(self):
        self._render_queue = []

    def _set_render_objects(self, objects) -> None:
        """
        Инициализирует очередь отрисовки, сортируя объекты по z_index.
        :return: None
        """
        self._render_queue = objects
        self._initialize_render_queue()

    def _render_objects(self, _surface: Surface) -> None:
        """
        Отрисовывает объекты на экране в порядке z_index
        :return: None
        """
        ...

    def _initialize_render_queue(self) -> None:
        """
        Инициализирует очередь отрисовки, сортируя объекты по z_index.
        :return: None
        """
        self._render_queue.sort(key=lambda obj: obj.z_index)
