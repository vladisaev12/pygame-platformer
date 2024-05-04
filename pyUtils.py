from multipledispatch import dispatch
from typing import List, Tuple
import sys

import pygame
from logger import log_write, DEBUG_LEVEL

class PyStorage:
    SIZE = [640, 480]
    SCREEN: pygame.surface
    CLOCK: pygame.time.Clock
    EVENTS: List[Tuple[pygame.event.Event, function]]

    @dispatch(str)
    def __init__(self, name: str):
        self.SCREEN, self.CLOCK = pyInit(self.SIZE, name)


    @dispatch(list, str)
    def __init__(self, size: list = SIZE, *, name: str):
        self.SIZE = size
        
        self.SCREEN, self.CLOCK = pyInit(self.SIZE, name)
    
    def AddEventBind(self, Event: pygame.event.Event, func: function):
        self.EVENTS.append(Tuple(Event, func))
    
    def runEventBinds(self):
        events = giveEvents()
        for Binds in self.EVENTS:
            for Event, func in Binds:
                if Event in events:
                    func()

def giveEvents() -> list:
    return pygame.event.get()

def Quit():
    pygame.quit()
    sys.quit()

def pyInit(Size, Caption = "Pygame game"):
    pygame.init()
    log_write("Pygame Initiated", DEBUG_LEVEL.INFO)

    pygame.display.set_caption(Caption)
    Screen = pygame.display.set_mode(Size)
    log_write("Window Initiated", DEBUG_LEVEL.DEBUG)

    Clock = pygame.time.Clock()
    log_write("Clock Initiated", DEBUG_LEVEL.DEBUG)

    return Screen, Clock
