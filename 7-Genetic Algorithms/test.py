# -*- coding: utf-8 -*-
"""
Created on Fri Feb 24 16:05:19 2017

@author: jp.strydom
"""

import numpy as np
import gene as g
import chromosome as c

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