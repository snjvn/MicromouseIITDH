import numpy as np

class cell:
    def __init__(self, x, y):
        
        self.x = x
        self.y = y

        self.north = 0
        self.south = 0
        self.east = 0
        self.west = 0

    def block_north(self):
        self.north = 1

    def block_south(self):
        self.south = 1

    def block_east(self):
        self.east = 1

    def block_west(self):
        self.west = 1
