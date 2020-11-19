

class Camera:

    def __init__(self, objDict, entity):

        self.cameraPosX, self.cameraPosY = 0, 0
        self.centerOn = entity

        self.objDict = objDict


    def update(self):
        self.playerObj = self.objDict.get("playerClass")
        self.tileObj = self.objDict.get("tileClass")

        self.tileList = self.tileObj.getTileList()

        if self.playerObj.playerInMvt:
            if self.playerObj.velocityX == -5:
                for tiles in self.tileList:
                    tiles.posX += 5

            if self.playerObj.velocityX == 5:
                for tiles in self.tileList:
                    tiles.posX -= 5

            if self.playerObj.velocityY == -5:
                for tiles in self.tileList:
                    tiles.posY += 5

            if self.playerObj.velocityY == 5:
                for tiles in self.tileList:
                    tiles.posY -= 5
