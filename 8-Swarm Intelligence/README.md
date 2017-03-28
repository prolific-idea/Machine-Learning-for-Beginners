# Swarm Intelligence
Control the crowd using "swarm intelligence".

## Hackathon - Crowd Control

For this hackathon, you're tasked with using swarm intelligence approaches to solving the problem of crowd control.

Imagine a two rooms with a wall between them, some doors, and lots of people needing to get from one room to the other.

```
_________________#_________________
___________________________________
__________*______#_________________
_______*_______*_#_________________
_*_______________#_________________
_________________#_________________
___________________________________
_**______________#_________________
___*_________*___#_________________
_________**______#_________________
____*____________#_________________
___________________________________
_______*_________#_________________
____________*____#_________________
_____*___________#_________________
______*__________#_________________
```

### The Symbols
* Wall: ```#```
* Empty space: ```_```
* Individual: ```*```

You will notice that the room on the left has many individuals trying to get to the room on the right. There are 3 doors provided. 

### The Code
The crowds.py file contains a simultion of this situation. The initial map and population is generated, you may change:
* ```MAP_SIZE_X```: To adjust the width of the map.
* ```MAP_SIZE_Y```: To adjust the height of the map.
* ```NUMBER_OF_INDIVIDUALS```: To adjust the number of individuals in the simulation.
* ```DOOR_SPACING```: To change the configuration of the doors.

There are two functions to modify and improve for this optimisation problem, namely:
* ```stopping_condition()```
* ```make_smart_move()```

### The Goal
Minimise the number of moves required for all individuals to move from the left room to the right room.

### Additional Related Links
* [Artificial Life: Conway's Game of Life](https://jakevdp.github.io/blog/2013/08/07/conways-game-of-life/)
* [PSO Tutorial with Python](http://www.swarmintelligence.org/tutorials.php)
* [Ant Colony Optimisation](https://github.com/pjmattingly/ant-colony-optimization)
* [Crowd Simulation in Python](http://pub.tik.ee.ethz.ch/students/2016-FS/BA-2016-10.pdf)