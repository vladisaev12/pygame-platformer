from typing import Tuple
from os import getcwd

from BaseEntity import BaseEntity
from pygame import color as col
from pygame import surface, draw, rect, image
class Player(BaseEntity):

    def __init__(self, pos: Tuple[float, float], angle: float, speed: float, color: col.Color, screen: surface.Surface, scr_size: Tuple[int, int]):
        super().__init__(pos, angle, speed, 32, color)
        self.screen = screen
        self.scr_size = scr_size
        self.minspd = self.speed * 0.15 # 15% of speed is minimal
        self.aPK = {} # (A)lready (P)ressed (K)eys
        self.idle_anim = []
        for i in range(1, 13):
            self.idle_anim.append(image.load(getcwd() + f"/animations/player/idle{i}.png"))
        self.cur_anim = "idle"
        self.cur_frame = 0
    #y is inversed since pygame positioning is top-left to bottom-right

    def goLeft(self) -> None:
        self.velocity[0] -= self.speed
        self.aPK["left"] = True
    def goRight(self) -> None:
        self.velocity[0] += self.speed
        self.aPK["right"] = True
    def goDown(self) -> None:
        self.velocity[1] += self.speed
        self.aPK["down"] = True
    def goUp(self) -> None:
        self.velocity[1] -= self.speed
        self.aPK["up"] = True
    
    def MovementUpdate(self) -> None: # probably the junkiest shit that you'll ever see
        friction = 0.05 # TODO: FIX: a small patch, will get changed when new surfaces will be added
        # X axis friction
        if self.velocity[0] > 0 and self.aPK["right"] == False:
            self.velocity[0] += -friction
            if self.velocity[0] < self.minspd:
                self.velocity[0] = 0
        elif self.velocity[0] < 0 and self.aPK["left"] == False:
                self.velocity[0] += friction
                if self.velocity[0] > -self.minspd:
                    self.velocity[0] = 0
        # Y axis friction
        if self.velocity[1] > 0 and self.aPK["down"] == False:
            self.velocity[1] += -friction
            if self.velocity[1] < self.minspd:
                self.velocity[1] = 0
        elif self.velocity[1] < 0 and self.aPK["up"] == False:
            self.velocity[1] += friction
            if self.velocity[1] > -self.minspd:
                self.velocity[1] = 0

        # print("X:" ,self.velocity[0], "Y:", self.velocity[1]) # debug for velecity
        if self.velocity[0]: # same as: if self.velosity[0] != 0
            self.x += self.velocity[0]
        if self.velocity[1]: # same as: if self.velosity[1] != 1
            self.y += self.velocity[1]



    def Update(self) -> None:
        self.MovementUpdate()
        for key in self.aPK.keys():
            self.aPK[key] = False
        # draw.rect(self.screen, self.color, rect.Rect(self.x, self.y, self.size, self.size))
        if self.cur_anim == "idle":
            if self.cur_frame < 11:
                self.cur_frame += 1
            else:
                self.cur_frame = 0
            self.screen.blit(self.idle_anim[self.cur_frame], rect.Rect(self.x, self.y, self.size * 2, self.size * 2))