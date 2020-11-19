from src.units.EntityClass import *
from utils.utils import *
from pygame.locals import *
import pygame as pg


class PlayerClass(EntityClass):

    def __init__(self, surface):

        # Create a new entity
        self.surface = surface
        self.playerX, self.playerY = 0, 0
        self.entity = EntityClass.newEntity(surface, "Player", "Entity", ImportImage("res\Entity\Muffy\Muffy_Sprite1.png"), 0.5)
        self.velocityX, self.velocityY = 0, 0
        self.playerInMvt = False


    def draw(self):
        self.entity.draw()

    def event(self):
        keys = pg.key.get_pressed()

        if keys[K_w]:
            self.velocityY = -5
            self.playerInMvt = True

        if keys[K_s]:
            self.velocityY = 5
            self.playerInMvt = True

        if keys[K_a]:
            self.velocityX = -5
            self.playerInMvt = True

        if keys[K_d]:
            self.velocityX = 5
            self.playerInMvt = True

        if not keys[K_w] and not keys[K_s]:
            self.velocityY = 0

        if not keys[K_a] and not keys[K_d]:
            self.velocityX = 0

        if not keys[K_w] and not keys[K_s] and not keys[K_a] and not keys[K_d]:
            self.playerInMvt = False

        if not self.playerInMvt:
            self.velocityX, self.velocityY = 0, 0



    def changePos(self, posX, posY):
        self.entity.spriteObj.posX, self.entity.spriteObj.posY = posX, posY

    def addPos(self, addPosX, addPosY):
        self.entity.spriteObj.posX, self.entity.spriteObj.posY = self.entity.spriteObj.posX + addPosX, self.entity.spriteObj.posY + addPosY

    def update(self):
        self.playerX += self.velocityX
        self.playerY += self.velocityY
        self.entity.update()
