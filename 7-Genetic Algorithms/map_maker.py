import numpy as np
import random as rand
from sys import exit

from warehouse import Warehouse
from delivery import Delivery
from simulation_map import SimulationMap

class MapMaker:
    def __init__(self,
                 map_x_range = [5, 10],
                 map_y_range = [5, 10],
                 items = np.array(['book','pen','laptop','mug','ball','shoes','shirt','DVD','tablet','dogfood']),
                 warehouse_num_range = [1, 5],
                 warehouse_inventory_size_range = [5, 10],
                 delivery_point_num_range = [5, 10],
                 delivery_point_item_num_range = [1, 10],
                 seed = None):
         self.map_x_range = map_y_range
         self.map_y_range = map_y_range
         self.warehouse_items = items
         self.warehouse_num_range = warehouse_num_range
         self.warehouse_inventory_size_range = warehouse_inventory_size_range
         self.delivery_point_num_range = delivery_point_num_range
         self.delivery_point_item_num_range = delivery_point_item_num_range
         self.seed = seed


    def make_warehouses(self):
        if self.seed is None:
            rand.seed(self.seed)
        num_of_items = np.size(self.warehouse_items)
        if num_of_items < self.warehouse_inventory_size_range[1]:
            exit("For a max inventory size of " + str(self.warehouse_inventory_size_range[1]) +
                 " you need at least " + str(self.warehouse_inventory_size_range[1]) + " stock items." +
                 "There are currently only " + str(num_of_items) + " stock items.")

        num_of_warehouses = rand.randint(self.warehouse_num_range[0], self.warehouse_num_range[1])
        warehouse_array = np.empty(num_of_warehouses, dtype=object)
        total_warehouse_items = np.empty(0, dtype=object)

        for i in xrange(num_of_warehouses):
            warehouse_size = rand.randint(self.warehouse_inventory_size_range[0], self.warehouse_inventory_size_range[1])
            warehouse_items = np.empty(warehouse_size, dtype=object)

            for j in xrange(warehouse_size):
                rand_int = rand.randint(0, num_of_items-1)
                while self.warehouse_items[rand_int] in warehouse_items:
                    rand_int = rand.randint(0, num_of_items-1)
                warehouse_items[j] = self.warehouse_items[rand_int]

                if self.warehouse_items[rand_int] not in total_warehouse_items:
                    total_warehouse_items = np.append(total_warehouse_items, self.warehouse_items[rand_int])

            warehouse = Warehouse(i, warehouse_items)
            warehouse_array[i] = warehouse

        return warehouse_array, total_warehouse_items


    def make_delivery_points(self, delivery_items):
        if self.seed != None:
            rand.seed(self.seed)
        num_of_items = np.size(delivery_items)
        num_of_delivery_points = rand.randint(self.delivery_point_num_range[0], self.delivery_point_num_range[1])
        delivery_point_array = np.empty(num_of_delivery_points, dtype = object)

        for i in xrange(num_of_delivery_points):
            delivery_point_item_num = rand.randint(self.delivery_point_item_num_range[0], self.delivery_point_item_num_range[1])
            delivery_point_items = {}

            for j in xrange(delivery_point_item_num):
                rand_int = rand.randint(0, num_of_items-1)
                if delivery_items[rand_int] in delivery_point_items:
                    delivery_point_items[delivery_items[rand_int]] += 1
                else:
                    delivery_point_items[delivery_items[rand_int]] = 1

            delivery = Delivery(delivery_point_items)
            delivery_point_array[i] = delivery

        return delivery_point_array


    def make_map(self):
        if self.seed != None:
            rand.seed(self.seed)
        map_x = rand.randint(self.map_x_range[0], self.map_x_range[1])
        map_y = rand.randint(self.map_y_range[0], self.map_y_range[1])
        simulation_map = np.empty([map_x, map_y], dtype = object)

        warehouses_array, warehouse_items = self.make_warehouses()
        delivery_points_array = self.make_delivery_points(delivery_items = warehouse_items)

        for warehouse in warehouses_array:
            warehouse_x = rand.randint(0, map_x - 1)
            warehouse_y = rand.randint(0, map_y - 1)
            while simulation_map[warehouse_x, warehouse_y] != None:
                warehouse_x = rand.randint(0, map_x - 1)
                warehouse_y = rand.randint(0, map_y - 1)
            simulation_map[warehouse_x, warehouse_y] = warehouse

        for delivery_point in delivery_points_array:
            delivery_point_x = rand.randint(0, map_x - 1)
            delivery_point_y = rand.randint(0, map_y - 1)
            while simulation_map[delivery_point_x, delivery_point_y] != None:
                delivery_point_x = rand.randint(0, map_x - 1)
                delivery_point_y = rand.randint(0, map_y - 1)
            simulation_map[delivery_point_x, delivery_point_y] = delivery_point

        return SimulationMap(simulation_map, warehouse_items)
