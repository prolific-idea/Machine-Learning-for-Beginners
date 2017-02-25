"""
Created on Fri Feb 24 16:32:29 2017

@author: jp.strydom
"""

import numpy as np
import random as rand

import warehouse as w
import delivery as d                
                  
"""
Generates a random list of Warehouse objects conforming to the provided parameters.
Input:  warehouse_num_range => int array [minimum number of Warehouse objects, 
                                          maximum number of Warehouse objects];
        items => string array containing all of the possible stock items;
        inventory_size_range => int array [minimum number of stock a Warehouse can have, 
                                           maximum number of stock a Warehouse can have];
        seed => number to seed random number generationm with (default None).
Output: Warehouse object array.

e.g.    Calling make_warehouses([5,10], ['shoe','ball','book'], [2,3]) will return 
        an array of between 5 and 10 (inclusive) Warehouse objects, where each 
        Warehouse can have between 2 and 3 (inclusive) items (without duplicates).
        If a seed is provided, all proceeding calls to make_warehouses with the 
        same seed will return an identical Warehouse object array. 
"""
def make_warehouses(warehouse_num_range, items, inventory_size_range, seed = None): 
    if seed != None:
        rand.seed(seed)
    num_of_items = np.size(items)        
    if num_of_items < inventory_size_range[1]:
        print "For a max inventory size of ", inventory_size_range[1], 
        " you need space for at least ", inventory_size_range[1], " stock."
        return None        
        
    num_of_warehouses = rand.randint(warehouse_num_range[0], warehouse_num_range[1])
    warehouse_array = np.empty(num_of_warehouses, dtype=object)  
    
    for i in xrange(num_of_warehouses):        
        warehouse_size = rand.randint(inventory_size_range[0], inventory_size_range[1])
        warehouse_items = np.empty(warehouse_size, dtype=object)  
        
        for j in xrange(warehouse_size):
            rand_int = rand.randint(0, num_of_items-1)
            while items[rand_int] in warehouse_items:
                rand_int = rand.randint(0, num_of_items-1)                
            warehouse_items[j] = items[rand_int] 
            
        warehouse = w.Warehouse(i, warehouse_items)
        warehouse_array[i] = warehouse  
        
    return warehouse_array