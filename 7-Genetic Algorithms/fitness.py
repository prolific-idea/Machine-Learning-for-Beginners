from simulation import Simulation, InvalidMoveException
from make_map import *


class FitnessCalculator:
    def __init__(self,
                 number_of_drones,
                 x_range,
                 y_range,
                 warehouse_range,
                 warehouse_inventory_range,
                 delivery_point_range,
                 item_range,
                 seed):
        items = np.array(['book', 'pen', 'laptop', 'mug', 'ball',
                          'shoes', 'shirt', 'DVD', 'tablet', 'dogfood'])
        simulation_map = make_map(x_range,
                                  y_range,
                                  items,
                                  warehouse_range,
                                  warehouse_inventory_range,
                                  delivery_point_range,
                                  item_range,
                                  seed)
        self.simulation = Simulation(number_of_drones, simulation_map)

    def get_fitness(self, chromosome):
        try:
            self.simulation.run(chromosome)
        except InvalidMoveException:
            return [0, np.inf]

