import numpy as np
from gene import Gene
from chromosome import Chromosome
from make_warehouses import make_warehouses
from make_delivery_points import make_delivery_points
from make_map import make_map
from warehouse import Warehouse
from delivery import Delivery
from map_maker import MapMaker

test_1 = False
test_2 = False
test_3 = True

items = np.array(['book', 'pen', 'laptop', 'mug', 'ball',
                  'shoes', 'shirt', 'DVD', 'tablet', 'dogfood'])

if test_1:
    gene1 = Gene(0, 'W')
    gene2 = Gene(1, 'N')
    gene3 = Gene(2, 'S')
    gene4 = Gene(2, 'W')

    array = np.array([gene1, gene2, gene3, gene4])

    chromosome = Chromosome(array)

    while True:
        temp = chromosome.get_move()
        if not temp:
            break
        print temp.drone_ID, temp.action, temp.action_parameter

    print

    warehouse_array, total_warehouse_items = make_warehouses([1, 10], items, [1, 10])
    print "All Warehouse Items :\n", total_warehouse_items
    print "\nWarehouse Items :"
    for warehouse in warehouse_array:
        print warehouse.items

    delivery_array = make_delivery_points([1, 10], total_warehouse_items, [1, np.size(total_warehouse_items)-1])
    print "\nDelivery Point Items :"
    for delivery in delivery_array:
        print delivery.orders

    print

if test_2:
    map_x_range = [5, 10]
    map_y_range = [5, 10]
    warehouse_num_range = [1, 5]
    warehouse_inventory_size_range = [5, 10]
    delivery_point_num_range = [5, 10]
    item_num_range = [1, 5]
    seed = None

    simulation_map = make_map(map_x_range, map_y_range, items,
                 warehouse_num_range, warehouse_inventory_size_range,
                 delivery_point_num_range, item_num_range, seed)

    Inv_Map = np.transpose(simulation_map)
    for row in Inv_Map:
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
    for row in Inv_Map:
        for element in row:
            if isinstance(element, Warehouse):
                print "Warehouse no.", warehouse_count, "items:", element.items
                warehouse_count += 1
            elif isinstance(element, Delivery):
                print "Delivery point no.", delivery_count, "orders:", element.orders
                delivery_count += 1


if test_3:
    map_maker = MapMaker()
    simulation_map = map_maker.make_map()
    inv_simulation_map = np.transpose(simulation_map)
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
                print "Warehouse no.", warehouse_count, "items:", element.items
                warehouse_count += 1
            elif isinstance(element, Delivery):
                print "Delivery point no.", delivery_count, "orders:", element.orders
                delivery_count += 1