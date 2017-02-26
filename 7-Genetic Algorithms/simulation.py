from sys import exit
from drone import Drone
from delivery import Delivery
from warehouse import Warehouse


def error(gene, details=""):
    exit("Invalid gene: droneID: " + str(gene.drone_ID) +
         ", Action: " + gene.action +
         ", Action Parameter: " + str(gene.action_parameter) +
         "\n" + details)


class Simulation:
    def __init__(self, number_of_drones, simulation_map, chromosome):
        self.number_of_drones = number_of_drones
        self.simulation_map = simulation_map
        self.chromosome = chromosome
        self.drones = []
        self.possible_moves = {}
        for i in range(number_of_drones):
            self.drones.append(Drone())

    def run(self):
        self.possible_moves = {"N": self.move_north,
                               "S": self.move_south,
                               "W": self.move_west,
                               "E": self.move_east,
                               "D": self.drop_item,
                               "P": self.pickup_item}
        while True:
            gene = self.chromosome.get_move()
            if gene is False:
                break
            elif gene.drone_ID > self.number_of_drones-1:
                error(gene, "Cannot index drone that does not exist")
            try:
                self.possible_moves[gene.action](gene)
            except KeyError:
                error(gene, "Invalid action")

    def move_north(self, gene):
        if self.drones[gene.drone_ID].yLocation - 1 < 0:
            error(gene, "Map index out of range")
        self.drones[gene.drone_ID].move(0, -1)

    def move_south(self, gene):
        if self.drones[gene.drone_ID].yLocation + 1 > self.simulation_map.shape[0]:
            error(gene, "Map index out of range")
        self.drones[gene.drone_ID].move(0, 1)

    def move_west(self, gene):
        if self.drones[gene.drone_ID].xLocation - 1 < 0:
            error(gene, "Map index out of range")
        self.drones[gene.drone_ID].move(-1, 0)

    def move_east(self, gene):
        if self.drones[gene.drone_ID].xLocation + 1 > self.simulation_map.shape[1]:
            error(gene, "Map index out of range")
        self.drones[gene.drone_ID].move(1, 0)

    def drop_item(self, gene):
        if gene.action_parameter is None:
            error(gene, "No item specified to drop")
        location = self.simulation_map[self.drones[gene.drone_ID].yLocation][
                                       self.drones[gene.drone_ID].xLocation]
        if not isinstance(location, Delivery):
            error(gene, "Invalid drop-off location")
        elif not self.drones[gene.drone_ID].is_carrying_item(gene.action_parameter):
            error(gene, "Target drone is not carrying that item")
        elif not location.deliver_item(gene.action_parameter):
            error(gene, "Target delivery is not expecting that item")
        self.drones[gene.drone_ID].remove_item(gene.action_parameter)

    def pickup_item(self, gene):
        if gene.action_parameter is None:
            error(gene, "No item specified to pick-up")
        location = self.simulation_map[self.drones[gene.drone_ID].yLocation][
                                       self.drones[gene.drone_ID].xLocation]
        if not isinstance(location, Warehouse):
            error(gene, "Invalid pick-up location")
        elif gene.action_parameter not in location.items:
            error(gene, "Target warehouse doesnt stock that item")
        self.drones[gene.drone_ID].add_item(location.warehouseID, gene.action_parameter)
