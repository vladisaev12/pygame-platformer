from typing import Tuple

from BaseEntity import BaseEntity
from pygame import color as col
from pygame import surface, draw, rect
class Player(BaseEntity):

    def __init__(self, pos: Tuple[float, float], angle: float, speed: float, color: col.Color, screen: surface.Surface, gravity: float, friction: float, scr_size: Tuple[int, int]):
        super().__init__(pos, angle, speed, 30, color)
        self.screen = screen
        self.gravity = gravity
        self.friction = friction
        self.scr_size = scr_size
    #y is inversed since pygame positioning is top-left to bottom-right

    def goLeft(self) -> None:
        self.velocity[0] -= self.speed
    def goRight(self) -> None:
        self.velocity[0] += self.speed
    def goDown(self) -> None:
        self.velocity[1] += self.speed
    def goUp(self) -> None:
        self.velocity[1] -= self.speed
    
    def MovementUpdate(self) -> None: # some junky movement
        self.y += self.gravity
        self.x += self.velocity[0]
        self.y += self.velocity[1]

        if self.velocity[0] < -10:
            self.velocity[0] = -10
        if self.velocity[0] > 10:
            self.velocity[0] = 10
        
        if self.velocity[1] < -10:
            self.velocity[1] = -10
        if self.velocity[1] < -20:
            self.velocity[1] = -20
        
        if self.velocity[0] < 0:
            self.velocity[0] += self.friction / 2
        if self.velocity[0] > 0:
            self.velocity[0] -= self.friction / 2

        


    def Update(self) -> None:
        self.MovementUpdate()
        draw.rect(self.screen, self.color, rect.Rect(self.x, self.y, self.size, self.size))