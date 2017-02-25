import numpy as np
from gene import Gene
from chromosome import Chromosome
from make_warehouses import make_warehouses
from make_delivery_points import make_delivery_points


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
    
items = np.array(['book', 'pen', 'laptop', 'mug', 'ball', 
                  'shoes', 'shirt', 'DVD', 'tablet', 'dogfood'])
                  
warehouse_array, total_warehouse_items = make_warehouses([1, 10], items, [1, 10])
if warehouse_array is not None:
    print "All Warehouse Items :\n", total_warehouse_items        
    print "\nWarehouse Items :"
    for warehouse in warehouse_array:
        print warehouse.items
                          
delivery_array = make_delivery_points([1, 10], total_warehouse_items, [1, np.size(total_warehouse_items)-1])
if delivery_array is not None:
    print "\nDelivery Point Items :"
    for delivery in delivery_array:
        print delivery.orders
