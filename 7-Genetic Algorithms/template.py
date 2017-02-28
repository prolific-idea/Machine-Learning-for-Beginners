import numpy as np
from domain.chromosome import Chromosome
from domain.gene import Gene
from fitness import FitnessCalculator

number_of_drones = 5
map_seed = 123
calculator = FitnessCalculator(number_of_drones, map_seed)

delivery_items = calculator.get_delivery_items()

"""
TODO:
    Generate genes and use delivery_items to construct gene objects (where applicable):
        e.g. gene = Gene(drone_ID, move_str, item_str) {where move_str = 'P' or 'D'; item_str = delivery_items[index]} or
             gene = Gene(drone_ID, move_str) {where move_str = 'N', 'S', 'W', or 'E'}

    Use gene array to construct chromosmes:
        e.g. genes = np.array([gene1, gene2,...])
             chromosome = Chromosome(genes)

    Calculate chromosome fittness:
        e.g. fitness = calculator.get_fitness(chromosome)
             fitness array contains [decimal percentage of items delivered, ratio of total distance traveled vs. map area]

    Use fitness to generate next generation

    Repeat untill a satisfactory delivery solution has been found
"""