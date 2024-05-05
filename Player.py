from typing import Tuple

from BaseEntity import BaseEntity
from pygame import color as col
from pygame import surface, draw, rect
class Player(BaseEntity):

    def __init__(self, pos: Tuple[int], angle: float, speed: int, color: col.Color, screen: surface.Surface):
        super().__init__(pos, angle, speed, 30, color)
        self.screen = screen

    def goLeft(self) -> None:
        self.velocity[0] -= self.speed
    def goRight(self) -> None:
        self.velocity[0] += self.speed
    def goDown(self) -> None:
        self.velocity[1] += self.speed
    def goUp(self) -> None:
        self.velocity[1] -= self.speed
    
    def Update(self) -> None:
        self.x += self.velocity[0]
        self.y += self.velocity[1]
        draw.rect(self.screen, self.color, rect.Rect(self.x, self.y, self.size, self.size))