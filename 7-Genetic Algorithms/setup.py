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
        
            
        

    


print warehouse_array[0].items

def make_warehouses(num, items, inventory_size):    
    warehouse_num = rand.randint(num[0], num[1])
    warehouse_array = np.empty(warehouse_num, dtype=object)
    
    for i in xrange(warehouse_num):
        warehouse_size = rand.randint(inventory_size[0], inventory_size[1])
        warehouse_items = np.empty(warehouse_size, dtype=object)
        for j in xrange(warehouse_size):
            rand_int = rand.randint(0, np.size(items)-1)
            while items[rand_int] in warehouse_items:
                rand_int = rand.randint(0, np.size(items)-1)
            warehouse_items[j] = items[rand_int] 
        
        warehouse = w.Warehouse(i, warehouse_items)
        warehouse_array[i] = warehouse
    return warehouse_array

warehouse_array_2 = make_warehouses([1, 10], items, [1, 5])

print warehouse_array_2[0].items
    