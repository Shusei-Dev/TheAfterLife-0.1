import pygame as pg

from src.units.SpriteClass import *


class TileClass(SpriteClass):
    global tileList
    tileList = []

    class newTile():

        def __init__(self, surface, name, type, img, posX, posY):
            self.typeList = ["Bg", "Fg"]

            self.posX, self.posY = posX, posY

            if type in self.typeList:
                type = "Tile"
                self.sprObj = SpriteClass.newSprite(surface, name, type, img, posX, posY)
                tileList.append(self.sprObj)
            else:
                return


        def draw(self):
            self.sprObj.draw()


        def update(self):
            self.sprObj.update()

    def draw(self):
        for elements in tileList:
            if elements.state == "displayed":
                elements.draw()

    def update(self):
        for tiles in tileList:
            tiles.update()

    def getTileList(self):
        return tileList
