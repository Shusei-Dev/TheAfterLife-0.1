import pygame as pg


class SpriteClass(pg.sprite.Sprite):

    global spriteList
    spriteList = []

    class newSprite():
        def __init__(self, surface, name, type, img, posX=None, posY=None):
            pg.sprite.Sprite.__init__(self)

            self.typeList = ["Entity", "Object", "Tile"]

            self.surface = surface
            self.name = name

            self.collapse = True

            if type in self.typeList:
                self.type = type
            else:
                print("This sprite type don't seems to exist !")
                return

            self.state = "displayed"

            if posX != None and posY != None:
                self.posX, self.posY = posX, posY
            else:
                self.posX, self.posY = 0, 0

            self.image = img
            self.rect = self.image.get_rect()
            self.rect.topleft = (self.posX, self.posY)

            spriteList.append(self)

        def draw(self):
            if self.state == "displayed":
                self.surface.blit(self.image, self.rect)
            else:
                pass

        def update(self):
            self.rect.topleft = (self.posX, self.posY)

    def getSpriteType(self, spriteObj):
        return spriteObj.type

    def getSpriteList(self):
        return spriteList
