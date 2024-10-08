from pygame import Surface


class SpriteComponent:
    def __init__(self, sprite: Surface):
        self.sprite = sprite
        self.rect = self.sprite.get_rect()
        self.width = self.sprite.get_width()
        self.height = self.sprite.get_height()
