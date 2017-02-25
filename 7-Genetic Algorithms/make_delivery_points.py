import numpy as np
import random as rand
from sys import exit

from delivery import Delivery        
                  
"""
Generates a random list of Delivery objects conforming to the provided parameters.
Input:  delivery_point_num_range => int array [minimum number of Delivery objects, 
                                               maximum number of Delivery objects];
        items => string array containing all of the possible delivery items;
        item_num_range => int array [minimum number of items a Delivery can have, 
                                     maximum number of items a Delivery can have];
        seed => number to seed random number generationm with (default None).
Output: Delivery object array.

e.g.    Calling make_delivery_points([5,10], ['shoe','ball','book'], [2,3]) will return 
        an array of between 5 and 10 (inclusive) Delivery objects, where each 
        Delivery can have between 2 and 3 (inclusive) items. If a seed is provided, 
        all proceeding calls to make_delivery_points with the same seed will 
        return an identical Delivery object array. 
"""  
def make_delivery_points(delivery_point_num_range, items, item_num_range, seed = None):
    if seed != None:
        rand.seed(seed)   
    num_of_items = np.size(items)        
    if num_of_items < item_num_range[1]:
        exit("For a max of " + str(item_num_range[1]) + 
             " delivery items per delivery, you need at least " + str(item_num_range[1]) + 
             " delivery items. There are currently only " + str(num_of_items) + " delivery items.")
        
    num_of_delivery_points = rand.randint(delivery_point_num_range[0], delivery_point_num_range[1])
    delivery_point_array = np.empty(num_of_delivery_points, dtype=object)  
    
    for i in xrange(num_of_delivery_points):        
        delivery_point_item_num = rand.randint(item_num_range[0], item_num_range[1])
        delivery_point_items = {} 
        
        for j in xrange(delivery_point_item_num):
            rand_int = rand.randint(0, num_of_items-1) 
            if items[rand_int] in delivery_point_items:
                delivery_point_items[items[rand_int]] += 1
            else:
                delivery_point_items[items[rand_int]] = 1
            
        delivery = Delivery(delivery_point_items)
        delivery_point_array[i] = delivery  
        
    return delivery_point_array 
    