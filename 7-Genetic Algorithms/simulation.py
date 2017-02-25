import drone as d


class Simulation:

    def __init__(self, number_of_drones, simulation_map, chromosome):
        self.number_of_drones = number_of_drones
        self.simulation_map = simulation_map
        self.chromosome = chromosome
        self.drones = []
        self.possible_moves = {}
        for i in range(number_of_drones):
            self.drones.append(d.Drone())

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
            elif gene.drone_ID > self.number_of_drones:
                self.error(gene, "Cannot index drone that does not exist")
            try:
                self.possible_moves[gene.action](gene)
            except KeyError:
                self.error(gene, "Invalid action")

    def move_north(self, gene):
        if self.drones[gene.drone_ID - 1].yLocation - 1 < 0:
            self.error(gene, "Map index out of range")
        self.drones[gene.drone_ID - 1].move(0, -1)

    def move_south(self, gene):
        if self.drones[gene.drone_ID - 1].yLocation + 1 > self.simulation_map.shape[0]:
            self.error(gene, "Map index out of range")
        self.drones[gene.drone_ID - 1].move(0, 1)

    def move_west(self, gene):
        if self.drones[gene.drone_ID - 1].xLocation - 1 < 0:
            self.error(gene, "Map index out of range")
        self.drones[gene.drone_ID - 1].move(-1)

    def move_east(self, gene):
        if self.drones[gene.drone_ID - 1].xLocation + 1 > self.simulation_map.shape[1]:
            self.error(gene, "Map index out of range")
        self.drones[gene.drone_ID - 1].move(1)

    def drop_item(self, gene):
        if gene.action_parameter is None:
            self.error(gene, "No item specified to drop")

    def pickup_item(self, gene):
        if gene.action_parameter is None:
            self.error(gene, "No item specified to pick-up")

    def error(self, gene, details=""):
        exit("Invalid gene: droneID: " + str(gene.drone_ID) +
             ", Action: " + gene.action +
             ", Action Parameter: " + str(gene.action_parameter) +
             "\n" + details)
