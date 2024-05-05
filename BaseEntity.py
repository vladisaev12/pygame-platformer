from typing import Tuple
from pygame import color as col

class BaseEntity:
    def __init__(self, pos: Tuple[int, int], angle: float, speed: int, size: int, color: col.Color):
        self.x = pos[0]
        self.y = pos[1]
        self.angle = angle
        self.speed = speed
        self.velocity = [0, 0]
        self.size = size
        self.color = color