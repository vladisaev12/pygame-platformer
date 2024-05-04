import pyUtils
from pyUtils import pygame
from logger import log_write, DEBUG_LEVEL

Running = True
GameStorage: pyUtils.PyStorage = pyUtils.PyStorage("test game")

GameStorage.AddEventBind(pygame.QUIT, pyUtils.Quit)

log_write("Loop Starting", DEBUG_LEVEL.INFO)
while Running:
    GameStorage.runEventBinds()

    pygame.display.update()
    GameStorage.CLOCK.tick(60)
