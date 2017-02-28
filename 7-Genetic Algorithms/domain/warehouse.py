import numpy as np


class Warehouse:
    def __init__(self, ID, items):
        self.warehouseID = ID
        self.items = items
        
    def add_item(self, item):
        if item not in self.items:
            self.items = np.append(self.items, item)
        
    def remove_item(self, item):
        if item in self.items:
            self.items = np.delete(self.items, np.where(self.items == item))
