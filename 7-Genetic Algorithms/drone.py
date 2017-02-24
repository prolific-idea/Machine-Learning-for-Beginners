import numpy as np

class Drone:
    def __init__(self):
        self.xLocation = 0
        self.yLocation = 0
        self.items = {}
        self.distanceTraveled = 0
        
    def move(self, action):
        if action == 'N':
            self.yLocation -= 1
        elif action == 'S':
            self.yLocation += 1
        elif action == 'W':
            self.xLocation -= 1
        elif action == 'E':
            self.xLocation += 1
        self.distanceTraveled += 1
        
    def addItem(self, warehouseID, item):
        self.items[warehouseID] = item
        
        
    def removeItem(self, itemToRemove):
        for key in self.items.keys():
            if self.items[key] == itemToRemove:
                del self.items[key]
                return True
        return False