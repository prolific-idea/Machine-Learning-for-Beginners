import numpy as np
from gene import Gene
from chromosome import Chromosome
from warehouse import Warehouse
from delivery import Delivery
from map_maker import MapMaker

test_1 = False
test_2 = True

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


if test_2:
    map_maker = MapMaker(seed = 123)
    simulation_map = map_maker.make_map()
    inv_simulation_map = np.transpose(simulation_map.simulation_map)
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

    print

    print simulation_map.get_number_of_orders()