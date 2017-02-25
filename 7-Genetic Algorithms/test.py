# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:05:19 2017

@author: jp.strydom
"""

import numpy as np
import gene as g
import chromosome as c
import make_warehouses as MW

gene1 = g.Gene(0, 'W')
gene2 = g.Gene(1, 'N')
gene3 = g.Gene(2, 'S')
gene4 = g.Gene(2, 'W')

array = np.array([gene1, gene2, gene3, gene4])

chromosome = c.Chromosome(array)

while True:
    temp = chromosome.get_move()
    if not temp:
        break
    print temp.drone_ID, temp.action, temp.action_parameter
    
    
items = np.array(['book', 'pen', 'laptop', 'mug', 'ball', 
                  'shoes', 'shirt', 'DVD', 'tablet', 'dogfood'])
                  
warehouse_array = MW.make_warehouses([1, 10], items, [1, 5])

for warehouse in warehouse_array:
    print warehouse.items
    