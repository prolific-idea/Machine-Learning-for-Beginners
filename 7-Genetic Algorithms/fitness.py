from services.simulation import Simulation, InvalidMoveException
from services.map_maker import *
import numpy as np


class FitnessCalculator:
    def __init__(self,
                 number_of_drones,
                 seed):
        self.seed = seed
        map_maker = MapMaker(seed=self.seed)
        self.simulation_map = map_maker.make_map()
        self.total_orders = float(self.simulation_map.get_number_of_orders())
        self.simulation = Simulation(number_of_drones, self.simulation_map)

    def get_fitness(self, chromosome):
        try:
            self.simulation.run(chromosome)
        except InvalidMoveException:
            return [0, np.inf]
        total_distance = 0
        total_remaining_orders = self.simulation_map.get_number_of_orders()
        for drone in self.simulation.drones:
            total_distance += drone.distanceTraveled
        return [(self.total_orders - total_remaining_orders)/self.total_orders,
                total_distance/float((self.simulation_map.simulation_map.shape[0] *
                                      self.simulation_map.simulation_map.shape[1]))]

    def get_delivery_items(self):
        return np.copy(self.simulation_map.delivery_items)

    def print_map(self):
        inv_simulation_map = np.transpose(self.simulation_map.simulation_map)
        for row in inv_simulation_map:
            for element in row:
                if element == None:
                    print ".",
                elif isinstance(element, Warehouse):
                    print "W",
                elif isinstance(element, Delivery):
                    print "D",
            print
        print

        warehouse_count = 0
        delivery_count = 0
        for row in inv_simulation_map:
            for element in row:
                if isinstance(element, Warehouse):
                    print "Warehouse no.", warehouse_count, "Items:", element.items
                    warehouse_count += 1
                elif isinstance(element, Delivery):
                    print "Delivery Point no.", delivery_count, "Orders:", element.orders
                    delivery_count += 1

        print "\nCollective Warehouse Items:", self.simulation_map.warehouse_items, "\n"

        print "Collective Delivery Items:", self.simulation_map.delivery_items, "\n"

        print "Collective Delivery Quantity:", self.simulation_map.get_number_of_orders(), "\n"
