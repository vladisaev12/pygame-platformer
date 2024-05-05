from multipledispatch import dispatch
from typing import List, Tuple, Dict, Callable
import sys

import pygame
from logger import log_write, DEBUG_LEVEL

class PyStorage:

    @dispatch(str)
    def __init__(self, name: str):
        self.size = (640, 480)
        self.binds: List[Tuple[int, Callable]] = []
        self.objects: Dict = {}
        self.screen, self.clock = pyInit(self.size, name)
        self.updateList: list[Callable] = []

    @dispatch(list, str)
    def __init__(self, size: Tuple, *, name: str):
        self.size = size
        self.binds: List[Tuple[int, Callable]] = []
        self.objects: Dict = {}
        self.screen, self.clock = pyInit(self.size, name)
        self.updateList: list[Callable] = []
    
    def AddUpdate(self, func: Callable) -> None:
        self.updateList.append(func)

    def AddKeyBind(self, Event: pygame.event.Event, func: Callable) -> None:
        self.binds.append((Event, func))

    def AddObject(self, name: str, value) -> None:
        self.objects[name] = value

    def runKeyBinds(self) -> None:
        key_input = pygame.key.get_pressed()
        for key, func in self.binds:
            if key_input[key]:
                func()

    def quitCheck(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    

    def runUpdates(self) -> None:
        print(self.updateList)
        if self.updateList:
            for func in self.updateList:
                func()

    def Update(self) -> None:
        self.quitCheck()
        self.runUpdates()
    
    def screenMiddle(self) -> None:
        return (self.size[0]/2, self.size[1]/2)

def giveEvents() -> list:
    return pygame.event.get()

def Quit() -> None:
    pygame.quit()
    sys.exit()



def pyInit(Size, Caption = "Pygame game") -> Tuple[pygame.surface.Surface, pygame.time.Clock]:
    pygame.init()
    log_write("Pygame Initiated", DEBUG_LEVEL.INFO)

    pygame.display.set_caption(Caption)
    Screen = pygame.display.set_mode(Size)
    log_write("Window Initiated", DEBUG_LEVEL.DEBUG)

    Clock = pygame.time.Clock()
    log_write("Clock Initiated", DEBUG_LEVEL.DEBUG)

    return Screen, Clock
