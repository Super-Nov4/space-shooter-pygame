from pygame.math import Vector2


class PositionComponent:
    def __init__(self, x: float, y: float):
        self.position = Vector2(x, y)
