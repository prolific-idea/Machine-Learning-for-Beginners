import numpy as np
import random as rand
from make_warehouses import make_warehouses
from make_delivery_points import make_delivery_points


"""
Generates a random map containing Warehouse and Delivery objects conforming to the
provided parameters.
Input:  map_x_range => int array [minimum map x-axis size, maximum map x-axis size];
        map_y_range => int array [minimum map y-axis size, maximum map y-axis size];
        items => string array containing all of the possible items;
        warehouse_num_range => int array [minimum number of Warehouse objects,
                                          maximum number of Warehouse objects];
        inventory_size_range => int array [minimum number of stock a Warehouse can have,
                                           maximum number of stock a Warehouse can have];
        delivery_point_num_range => int array [minimum number of Delivery objects,
                                               maximum number of Delivery objects];
        item_num_range => int array [minimum number of items a Delivery can have,
                                     maximum number of items a Delivery can have];
        seed => number to seed random number generationm with (default None).
Output: Map => 2D array containing Warehouse and Delivery objects.
"""
def make_map(map_x_range, map_y_range, items,
             warehouse_num_range, warehouse_inventory_size_range,
             delivery_point_num_range, item_num_range, seed = None):
    if seed != None:
        rand.seed(seed)
    map_x = rand.randint(map_x_range[0], map_x_range[1])
    map_y = rand.randint(map_y_range[0], map_y_range[1])
    Map = np.empty([map_x, map_y], dtype=object)

    warehouses_array, warehouse_items = make_warehouses(warehouse_num_range, items, warehouse_inventory_size_range, seed)
    delivery_points_array = make_delivery_points(delivery_point_num_range, warehouse_items, item_num_range, seed)

    for warehouse in warehouses_array:
        warehouse_x = rand.randint(0, map_x - 1)
        warehouse_y = rand.randint(0, map_y - 1)
        while Map[warehouse_x, warehouse_y] != None:
            warehouse_x = rand.randint(0, map_x - 1)
            warehouse_y = rand.randint(0, map_y - 1)
        Map[warehouse_x, warehouse_y] = warehouse

    for delivery_point in delivery_points_array:
        delivery_point_x = rand.randint(0, map_x - 1)
        delivery_point_y = rand.randint(0, map_y - 1)
        while Map[delivery_point_x, delivery_point_y] != None:
            delivery_point_x = rand.randint(0, map_x - 1)
            delivery_point_y = rand.randint(0, map_y - 1)
        Map[delivery_point_x, delivery_point_y] = delivery_point

    return Map