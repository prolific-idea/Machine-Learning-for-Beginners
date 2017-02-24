"""
Created on Fri Feb 24 16:32:29 2017

@author: jp.strydom
"""

import numpy as np
import random as rand

import warehouse as w
import drone as drone
#import delivery as d
import gene as g
import chromosome as c

items = np.array(['book', 'pen', 'laptop', 'mug', 'ball'])

warehouse_num = rand.randint(1, 10)
warehouse_array = np.empty(warehouse_num, dtype=object)

for i in xrange(warehouse_num):
    warehouse_size = rand.randint(1, 5)
    warehouse_items = np.empty(warehouse_size, dtype=object)
    for j in xrange(warehouse_size):
        rand_int = rand.randint(0, 4)
        while items[rand_int] in warehouse_items:
            rand_int = rand.randint(0, 4)
        warehouse_items[j] = items[rand_int] 
    
    warehouse = w.Warehouse(i, warehouse_items)
    warehouse_array[i] = warehouse
        
            
        

    


print warehouse_array

def make_warehouses(num, items, inventory_size):
    item_size = iy    
    
    warehouse_num = rand.randint(num[0], num[1])
    warehouse_array = np.empty(warehouse_num, dtype=object)
    
    for i in xrange(warehouse_num):
        warehouse_size = rand.randint(1, 5)
        warehouse_items = np.empty(warehouse_size, dtype=object)
        for j in xrange(warehouse_size):
            rand_int = rand.randint(0, 4)
            while items[rand_int] in warehouse_items:
                rand_int = rand.randint(0, 4)
            warehouse_items[j] = items[rand_int] 
        
        warehouse = w.Warehouse(i, warehouse_items)
        warehouse_array[i] = warehouse
    