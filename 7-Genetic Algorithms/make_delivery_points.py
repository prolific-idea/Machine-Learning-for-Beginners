"""
Created on Sat Feb 25 12:31:41 2017

@author: jp.strydom
"""

import numpy as np
import random as rand

import delivery as d   

def make_delivery_points(delivery_point_num_range, items, item_num_range, seed = None):
    if seed != None:
        rand.seed(seed)   
    num_of_items = np.size(items)        
    if num_of_items < item_num_range[1]:
        print "For a max of", item_num_range[1], 
        print "delivery items per delivery, you need at least", item_num_range[1], 
        print "delivery items. There are currently only", num_of_items, "delivery items."
        return None        
        
    num_of_delivery_points = rand.randint(delivery_point_num_range[0], delivery_point_num_range[1])
    delivery_point_array = np.empty(num_of_delivery_points, dtype=object)  
    
    for i in xrange(num_of_delivery_points):        
        delivery_point_item_num = rand.randint(item_num_range[0], item_num_range[1])
        delivery_point_items = np.empty(delivery_point_item_num, dtype=object)  
        
        for j in xrange(delivery_point_item_num):
            rand_int = rand.randint(0, num_of_items-1)
            while items[rand_int] in delivery_point_items:
                rand_int = rand.randint(0, num_of_items-1)                
            delivery_point_items[j] = items[rand_int] 
            
        delivery = d.Delivery(delivery_point_items)
        delivery_point_array[i] = delivery  
        
    return delivery_point_array 
    