# Machine Learning - Genetic Algorithms
## Introduction
In computer science and operations research, a genetic algorithm (GA) is a metaheuristic inspired by the process of natural selection that belongs to the larger class of evolutionary algorithms (EA). Genetic algorithms are commonly used to generate high-quality solutions to optimization and search problems by relying on bio-inspired operators such as mutation, crossover and selection. [[1]](https://en.wikipedia.org/wiki/Genetic_algorithm)
## Getting Started
The following software is required:
+ [Python](http://www.python.org)
+ [Numpy](http://www.numpy.org)

##Hackathon - Drone Delivery System
For this hackathon we will be using genetic algorithms to optimize a drone delivery system by modelling an instruction as a gene and a collection of instructions as a chromosome.

A two-dimensional array will be used to represent a geographical map. Such a map will contain empty cells, warehouses, and delivery points. A predetermined amount of drones will initially reside at the top-left most corner-cell on the map. Your goal is to generate movement and action commands for these drones to complete as many possible deliveries in as few as possible moves.

Below is an example of a map array (this map is used in the *example.py* file). In this example a '**.**' represents an empty cell, a '**W**' represents a warehouse, and a '**D**' represents a delivery point.
```
W . . D .
W . . D D
. . . . D
. . . . .
. D W . .
```
The restrictions imposed on the drones are as follows:

   + Drones(D) deliver items
   + Items reside at warehouses(W)
   + Drones start at 0, 0
   + Drones may only pick up one item per warehouse
   + Drones may carry unlimited items as long as each are from a different warehouse
   + Drones cannot pick up from a delivery point or empty cell
   + Drones cannot drop to a warehouse
  
The restrictions on warehouse and deliveries:

   + Warehouses can contain an unlimited supply of one or many items.
   + Deliveries may require one or many items that reside at one or many warehouses.

Each drone can perform any of the following moves:
   + '**N**' - Move North
   + '**S**' - Move South
   + '**W**' - Move West
   + '**E**' - Move East
   + '**P**' - Pick up | This requires an additional string parameter of what to pick up.
   + '**D**' - Drop | This requires an additional string parameter of what to drop.

Invalid moves will cause the chromosome to be evaluated with the worst possible fitness. Invalid moves include:
   + Moving out of the bounds of the map.
   + Attempting to pick up from a cell that isn't a warehouse.
   + Attempting to pick up an item a warehouse does'nt stock.
   + Attempting to drop an item where there is no delivery point.
   + Attempting to drop an item at a delivery point that does'nt want that item.    
   + Attempting to drop an item that the drone isn't carrying.


In the above map, going from left to right and top to bottom, the following information can be gathered about the respective entities and their delivery/stock items:


```
Warehouse no. 0 Items: ['mug' 'ball' 'dogfood' 'book' 'pen']
Delivery Point no. 0 Orders: {'mug': 1}
Warehouse no. 1 Items: ['dogfood' 'book' 'shoes' 'mug' 'tablet']
Delivery Point no. 1 Orders: {'mug': 1}
Delivery Point no. 2 Orders: {'tablet': 1}
Delivery Point no. 3 Orders: {'dogfood': 1, 'pen': 1}
Delivery Point no. 4 Orders: {'book': 2, 'ball': 1, 'shoes': 3}
Warehouse no. 2 Items: ['mug' 'laptop' 'book' 'ball' 'shoes']
```
All the items present in warehouses on the map can be seen under '**Collective Warehouse Items**', all the items needed for deliveries on the map can be seen under '**Collective Delivery Items**', and '**Collective Delivery Quantity**' shows how many orders there are on the map in total.
```
Collective Warehouse Items: ['dogfood' 'book' 'shoes' 'mug' 'tablet' 'laptop' 'ball' 'pen'] 
 
Collective Delivery Items: ['mug' 'pen' 'dogfood' 'shoes' 'ball' 'book' 'tablet'] 
 
Collective Delivery Quantity: 11 
```

##Fitness Calculator
The fitness calculator will estimate how well a choromosome performs. Based on this performance, you can choose which chormosomes to use for your GA's next generation, and which to discard. The fitness calculator takes in a chromosome and returns and array of fitness measures.

```
[Decimal percentage of items delivered, Ratio of total distance traveled vs. map area]
```

####Using the fitness calculator

Before you can use the fitness calculator however, you need to construct genes and chromosomes.
To generate genes, use the drone ID, the move string (as described above), and, where applicable, the string array called *delivery_items* (this is the same array as Collective Delivery Items described above) to construct gene objects:
```Python
gene = Gene(drone_ID, move_str, item_str) # where move_str = 'P' or 'D'; item_str = delivery_items[index] or
gene = Gene(drone_ID, move_str) # where move_str = 'N', 'S', 'W', or 'E'
```

Use a gene array to construct chromosomes:
```Python
genes = np.array([gene1, gene2, ...])
chromosome = Chromosome(genes)
```

Calculate the chromosome's fitness:
```Python
fitness = calculator.get_fitness(chromosome)
```

Use the returned fitness to judge chromosomes best suited for the next generation. 

*Note: The *example.py* file contains a detailed example on how to use the fitness calculator, 
including how to structure a gene and a chromosome.

##References
   1. [Wikipedia - Genetic Algorithms](https://en.wikipedia.org/wiki/Genetic_algorithm)
