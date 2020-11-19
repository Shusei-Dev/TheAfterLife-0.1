from src.units.SpriteClass import *


class EntityClass(SpriteClass):

    global entityList
    entityList = []

    class newEntity:

        def __init__(self, surface, name, type, img, gravity):

            if type == "Entity":
                self.spriteObj = SpriteClass.newSprite(surface, name, type, img)
                entityList.append(self.spriteObj)
            else:
                return

            self.gravity = gravity

        def draw(self):
            self.spriteObj.draw()

        def update(self):

            self.spriteObj.update()
