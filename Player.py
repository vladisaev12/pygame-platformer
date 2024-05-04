from typing import Tuple

class Player:
    X: int
    Y: int
    ANGLE: float
    SPEED: int
    VELOCITY = [0, 0]

    def __init__(self, POS: Tuple[int, int], ANGLE: float, SPEED):
        self.X = POS[0]
        self.Y = POS[1]
        self.ANGLE = ANGLE
        self.SPEED = SPEED
    
    def goLeft(self):
        self.VELOCITY[0] -= self.SPEED
    def goRight(self):
        self.VELOCITY[0] += self.SPEED
    def goDown(self):
        self.VELOCITY += self.SPEED
    def goUp(self):
        self.VELOCITY -= self.SPEED