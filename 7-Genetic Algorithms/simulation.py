import drone as d


class Simulation:

    def __init__(self, number_of_drones, simulation_map, chromosome):
        self.number_of_drones = number_of_drones
        self.simulation_map = simulation_map
        self.chromosome = chromosome
        self.drones = []
        for i in range(number_of_drones):
            self.drones.append(d.Drone())

    def check_validity(self):
        while True:
            gene = self.chromosome.get_move()
            if gene is False:
                break
            elif gene.action == 'N':
                if self.drones[gene.drone_ID].y - 1 < 0:
                    return False
                self.drones[gene.drone_ID].move(None, -1)
            elif gene.action == 'S':
                if self.drones[gene.drone_ID].y + 1 > self.simulation_map.shape[0]:
                    return False
                self.drones[gene.drone_ID].move(None, 1)
            elif gene.action == 'W':
                if self.drones[gene.drone_ID].x - 1 < 0:
                    return False
                self.drones[gene.drone_ID].move(-1)
            elif gene.action == 'E':
                if self.drones[gene.drone_ID].x + 1 > self.simulation_map.shape[1]:
                    return False
                self.drones[gene.drone_ID].move(1)
