from simulation import Simulation, InvalidMoveException
from map_maker import *
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
