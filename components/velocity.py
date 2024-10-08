from pygame.math import Vector2


class VelocityComponent:
    def __init__(self, x: float, y: float):
        self.velocity = Vector2(x, y)

