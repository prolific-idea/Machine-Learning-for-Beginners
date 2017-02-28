import numpy as np

from domain.chromosome import Chromosome
from domain.gene import Gene
from services.fitness import FitnessCalculator

number_of_drones = 5
map_seed = 123
calculator = FitnessCalculator(number_of_drones, map_seed)

delivery_items = calculator.get_delivery_items()

#BEGIN EXAMPLE

genes = np.array([Gene(0, 'P', delivery_items[0]),
                  Gene(0, 'E'),
                  Gene(0, 'E'),
                  Gene(0, 'E'),
                  Gene(0, 'D', delivery_items[0]),
                  Gene(1, 'P', delivery_items[0]),
                  Gene(1, 'E'),
                  Gene(1, 'E'),
                  Gene(1, 'E'),
                  Gene(1, 'S'),
                  Gene(1, 'D', delivery_items[0]),
                  Gene(2, 'S'),
                  Gene(2, 'P', delivery_items[6]),
                  Gene(2, 'E'),
                  Gene(2, 'E'),
                  Gene(2, 'E'),
                  Gene(2, 'E'),
                  Gene(2, 'D', delivery_items[6]),
                  Gene(3, 'P', delivery_items[1]),
                  Gene(3, 'S'),
                  Gene(3, 'P', delivery_items[2]),
                  Gene(3, 'S'),
                  Gene(3, 'E'),
                  Gene(3, 'E'),
                  Gene(3, 'E'),
                  Gene(3, 'E'),
                  Gene(3, 'D', delivery_items[2]),
                  Gene(3, 'D', delivery_items[1]),
                  Gene(4, 'P', delivery_items[5]),
                  Gene(4, 'S'),
                  Gene(4, 'P', delivery_items[5]),
                  Gene(4, 'S'),
                  Gene(4, 'S'),
                  Gene(4, 'S'),
                  Gene(4, 'E'),
                  Gene(4, 'D', delivery_items[5]),
                  Gene(4, 'D', delivery_items[5]),
                  Gene(4, 'E'),
                  Gene(4, 'P', delivery_items[4]),
                  Gene(4, 'W'),
                  Gene(4, 'D', delivery_items[4]),
                  Gene(4, 'E'),
                  Gene(4, 'P', delivery_items[3]),
                  Gene(4, 'W'),
                  Gene(4, 'D', delivery_items[3]),
                  Gene(4, 'E'),
                  Gene(4, 'P', delivery_items[3]),
                  Gene(4, 'W'),
                  Gene(4, 'D', delivery_items[3]),
                  Gene(4, 'E'),
                  Gene(4, 'P', delivery_items[3]),
                  Gene(4, 'W'),
                  Gene(4, 'D', delivery_items[3])])

chromosome = Chromosome(genes)

calculator.print_map()

print "Chromosome Fitness [decimal percentage of items delivered, ratio of total distance traveled vs. map area]:", calculator.get_fitness(chromosome)

#END EXAMPLE