import numpy as np
from domain.chromosome import Chromosome
from domain.gene import Gene
from fitness import FitnessCalculator

number_of_drones = 5
map_seed = 123
calculator = FitnessCalculator(number_of_drones, map_seed)

delivery_items = calculator.get_delivery_items()

#BEGIN EXAMPLE

genes = np.array([Gene(0, 'P', 'mug'),
                  Gene(0, 'E'),
                  Gene(0, 'E'),
                  Gene(0, 'E'),
                  Gene(0, 'D', 'mug'),
                  Gene(1, 'P', 'mug'),
                  Gene(1, 'E'),
                  Gene(1, 'E'),
                  Gene(1, 'E'),
                  Gene(1, 'S'),
                  Gene(1, 'D', 'mug'),
                  Gene(2, 'S'),
                  Gene(2, 'P', 'tablet'),
                  Gene(2, 'E'),
                  Gene(2, 'E'),
                  Gene(2, 'E'),
                  Gene(2, 'E'),
                  Gene(2, 'D', 'tablet'),
                  Gene(3, 'P', 'pen'),
                  Gene(3, 'S'),
                  Gene(3, 'P', 'dogfood'),
                  Gene(3, 'S'),
                  Gene(3, 'E'),
                  Gene(3, 'E'),
                  Gene(3, 'E'),
                  Gene(3, 'E'),
                  Gene(3, 'D', 'dogfood'),
                  Gene(3, 'D', 'pen'),
                  Gene(4, 'P', 'book'),
                  Gene(4, 'S'),
                  Gene(4, 'P', 'book'),
                  Gene(4, 'S'),
                  Gene(4, 'S'),
                  Gene(4, 'S'),
                  Gene(4, 'E'),
                  Gene(4, 'D', 'book'),
                  Gene(4, 'D', 'book'),
                  Gene(4, 'E'),
                  Gene(4, 'P', 'ball'),
                  Gene(4, 'W'),
                  Gene(4, 'D', 'ball'),
                  Gene(4, 'E'),
                  Gene(4, 'P', 'shoes'),
                  Gene(4, 'W'),
                  Gene(4, 'D', 'shoes'),
                  Gene(4, 'E'),
                  Gene(4, 'P', 'shoes'),
                  Gene(4, 'W'),
                  Gene(4, 'D', 'shoes'),
                  Gene(4, 'E'),
                  Gene(4, 'P', 'shoes'),
                  Gene(4, 'W'),
                  Gene(4, 'D', 'shoes')])

chromosome = Chromosome(genes)

calculator.print_map()

print "Chromosome Fitness [decimal percentage of items delivered, ratio of total distance traveled vs. map area]:", calculator.get_fitness(chromosome)

#END EXAMPLE