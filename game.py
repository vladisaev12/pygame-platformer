import pyGUtils
from pyGUtils import pygame
from logger import Logger

from Player import Player

#create the Storage
GameStorage: pyGUtils.PyGStorage = pyGUtils.PyGStorage("test game")

#add exit keybind
GameStorage.AddKeyBind(pygame.QUIT, pyGUtils.Quit)

#add the player to the GameStorage Object
GameStorage.AddObject("Player",Player(GameStorage.screenMiddleFloat(), 0, 1, pygame.Color(0, 255, 255), GameStorage.screen, 2.0, 5.0, GameStorage.screenMiddle()))

#player movement
GameStorage.AddKeyBind(pygame.K_a, GameStorage.objects["Player"].goLeft)
GameStorage.AddKeyBind(pygame.K_d, GameStorage.objects["Player"].goRight)
GameStorage.AddKeyBind(pygame.K_s, GameStorage.objects["Player"].goDown)
GameStorage.AddKeyBind(pygame.K_w, GameStorage.objects["Player"].goUp)

GameStorage.AddUpdate(GameStorage.objects["Player"].Update)

GameStorage.logger.log_write("Loop Starting", Logger.DEBUG_LEVEL.DEBUG)
while True:
    GameStorage.Update()