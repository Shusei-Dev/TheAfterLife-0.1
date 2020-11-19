import pygame as pg
import sys, time, random, os

from pygame.locals import *

from src.settings import *
from src.menu import *
from utils.utils import *

from src.units.PlayerClass import *
from src.units.TileClass import *

from src.CameraClass import *


class MainClass:
    def __init__(self):
        pg.init()
        pg.mixer.init()
        pg.font.init()

        infoMsg("Pygame as been init, the game start to init all methods", "INFO")

        ds_info = pg.display.Info()
        x_pos_screen = 0
        y_pos_screen = 0
        os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (x_pos_screen, y_pos_screen)

        self.m_width = ds_info.current_w
        self.m_height = ds_info.current_h
        self.screen = pg.display.set_mode((self.m_width, self.m_height), settings.full_screen)



        pg.display.set_caption(settings.name + " v" + settings.version)
        self.clock = pg.time.Clock()
        self.running = True

        infoMsg("All basic elements have been init", "INFO")


    def init(self):
        infoMsg("All elements of the game start to init", "INFO")
        self.errorInit = False
        self.init_menu()
        self.init_sprite()
        self.init_camera()
        self.init_world()
        if not self.errorInit:
            infoMsg("Everythings has been init correctly, the game start with no error", "INFO")
        else:
            infoMsg("Please check the game content, if you modifed the game please re-install him correctly", "ERROR")


    def init_menu(self):
        self.main_menu = MainMenu()
        infoMsg("Menu as been init", "INFO")


    def init_world(self):
        self.worldMap = [["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
                         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"],
                         ["0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]]

        self.worldSize = (len(self.worldMap[0]), len(self.worldMap))
        self.worldPos = (124, 126)

        self.tileSize = 32

        grassTileImg = ImportImage("res\Tiles\grassTile.png")
        dirtTileImg = ImportImage("res\Tiles\dirtTile.png")

        tileNmb = 0
        worldPosX, worldPosY = self.worldPos[0] - self.tileSize, self.worldPos[1] - self.tileSize

        for y in range(self.worldSize[1]):
            worldPosY += self.tileSize
            if tileNmb != 0:
                worldPosX = self.worldPos[0] - self.tileSize
            for x in range(self.worldSize[0]):
                worldPosX += self.tileSize

                tileElement = self.worldMap[y][x]
                tileNmb += 1
                if tileElement == str(1):
                    self.tileClass.newTile(self.screen, "Grass " + str(tileNmb), "Fg", grassTileImg, worldPosX, worldPosY)
                if tileElement == str(0):
                    self.tileClass.newTile(self.screen, "Dirt " + str(tileNmb), "Fg", dirtTileImg, worldPosX, worldPosY)

                tileList = self.tileClass.getTileList()

    def init_sprite(self):
        self.objDict = {}
        # Create the tile class
        self.tileClass = TileClass()
        self.objDict["tileClass"] = self.tileClass
        # Create the player class
        self.playerClass = PlayerClass(self.screen)
        self.objDict["playerClass"] = self.playerClass


    def init_camera(self):
        self.camera = Camera(self.objDict, self.playerClass)




    def main_loop(self):
        self.playing = True
        while self.playing:
            self.clock.tick(settings.fps)
            self.event()
            self.draw()
            self.update()


    def event(self):
        self.fullscreen = settings.full_screen

        for event in pg.event.get():
            if event.type == QUIT:
                if self.playing:
                    self.playing = False
                self.running = False

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    self.running = False


        self.playerClass.event()


    def draw(self):
        self.screen.fill((0,0,0))
        self.playerClass.draw()
        self.tileClass.draw()


    def update(self):
        self.playerClass.update()
        self.camera.update()
        self.tileClass.update()
        pg.display.update()




if __name__ == "__main__":
	main = MainClass()
else:
	pass
	sys.exit()



while main.running:
    main.init()
    main.main_loop()

pg.quit()
sys.exit()
