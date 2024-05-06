from multipledispatch import dispatch
from typing import List, Tuple, Dict, Callable
import sys

import pygame
from logger import Logger

class PyGStorage:

    @dispatch(str)
    def __init__(self, name: str):
        self.logger = Logger(Logger.DEBUG_LEVEL.INFO)
        self.size = (640, 480)
        self.binds: List[Tuple[int, Callable]] = []
        self.objects: Dict = {}
        self.updateList: list[Callable] = []
        self.screen, self.clock = pyInit(self.logger, self.size, name)
        self.logger.log_write("PyGStorage Intilizated", Logger.DEBUG_LEVEL.DEBUG)

    @dispatch(list, str)
    def __init__(self, size: Tuple, *, name: str):
        self.logger = Logger(Logger.DEBUG_LEVEL.INFO)
        self.size = size
        self.binds: List[Tuple[int, Callable]] = []
        self.objects: Dict = {}
        self.updateList: list[Callable] = []
        self.screen, self.clock = pyInit(self.logger, self.size, name)
        Logger.log_write("PyGStorage Intilizated", Logger.DEBUG_LEVEL.DEBUG)
    
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
        if self.updateList:
            for func in self.updateList:
                func()

    def Update(self) -> None:
        self.screen.fill((0, 0, 0))
        self.quitCheck()
        self.runKeyBinds()
        self.runUpdates()
        pygame.display.update()
        self.clock.tick(60)
    
    def screenMiddle(self) -> Tuple[int, int]:
        return (self.size[0]/2, self.size[1]/2)
    def screenMiddleFloat(self) -> Tuple[float, float]:
        return (float(self.size[0]/2), float(self.size[1]/2))

def giveEvents() -> list:
    return pygame.event.get()

def Quit() -> None:
    pygame.quit()
    sys.exit()



def pyInit(logger: Logger, Size, Caption = "Pygame game") -> Tuple[pygame.surface.Surface, pygame.time.Clock]:
    pygame.init()
    logger.log_write("Pygame Initiated", Logger.DEBUG_LEVEL.INFO)

    pygame.display.set_caption(Caption)
    Screen = pygame.display.set_mode(Size)
    logger.log_write("Window Initiated", Logger.DEBUG_LEVEL.DEBUG)

    Clock = pygame.time.Clock()
    logger.log_write("Clock Initiated", Logger.DEBUG_LEVEL.DEBUG)

    return Screen, Clock
