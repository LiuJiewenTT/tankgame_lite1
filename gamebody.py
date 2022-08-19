import cv2.cv2 as cv
import numpy as np

class GameBody:
    # Indev
    # This is the body of game.
    # main.py should create an instance of it to run the game.
    plate = None
    scale = None    # [width, height]
    background = None
    background_path = None

    def __init__(self):
        pass

    def setBackground(self, img):
        self.background = img
        self.background_path = None

    def setBackground_path(self, path):
        self.background_path = path
        self.background = None

    def setBackgroundFromFile(self, filepath):
        self.background_path = filepath
        self.background = cv.imread(filepath, cv.IMREAD_COLOR)

    def showBackground(self):
        # Should apply multi-thread tech.
        cv.namedWindow('showBackground', cv.WINDOW_AUTOSIZE)
        cv.imshow('showBackground', self.background)
        cv.waitKey(0)