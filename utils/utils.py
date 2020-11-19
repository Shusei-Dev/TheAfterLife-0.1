import time
import pygame as pg

def infoMsg(message, type):
    print("[" + type + ": " + getTime() + "] " + message)

def getTime():
    actualtime = time.strftime("%I:%M:%S")
    return actualtime


def ImportImage(path):
    image = pg.image.load(path).convert()
    return image
