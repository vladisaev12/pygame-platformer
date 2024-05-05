import pyGUtils
from pyGUtils import pygame
from logger import log_write, DEBUG_LEVEL

from Player import Player

#create the Storage
GameStorage: pyGUtils.PyStorage = pyGUtils.PyStorage("test game")

#add exit keybind
GameStorage.AddKeyBind(pygame.QUIT, pyGUtils.Quit)

#add the player to the GameStorage Object
GameStorage.AddObject("Player",Player(GameStorage.screenMiddle(), 0, 3, pygame.Color(0, 255, 255), GameStorage.screen))

#player movement
GameStorage.AddKeyBind(pygame.K_a, GameStorage.objects["Player"].goLeft)
GameStorage.AddKeyBind(pygame.K_d, GameStorage.objects["Player"].goRight)
GameStorage.AddKeyBind(pygame.K_s, GameStorage.objects["Player"].goDown)
GameStorage.AddKeyBind(pygame.K_w, GameStorage.objects["Player"].goUp)

GameStorage.AddUpdate(GameStorage.objects["Player"].Update)

log_write("Loop Starting", DEBUG_LEVEL.INFO)
while True:
    GameStorage.Update()