import platform
import sys
import os
from random import randint

MAP_SIZE_X = 16
MAP_SIZE_Y = 35
NUMBER_OF_INDIVIDUALS = 25
DOOR_SPACING = 5

BLOCK_EMPTY = "_"
BLOCK_WALL = "#"
BLOCK_INDIVIDUAL = "*"

map = [[BLOCK_EMPTY for a in range(MAP_SIZE_Y)] for b in range(MAP_SIZE_X)]
next_map = [[BLOCK_EMPTY for a in range(MAP_SIZE_Y)] for b in range(MAP_SIZE_X)]


def update_map():
    for x in range(MAP_SIZE_X):
        for y in range(MAP_SIZE_Y):
            map[x][y] = next_map[x][y]


def move_individual(x, y, tx, ty):
    if map[x][y] == BLOCK_INDIVIDUAL:
        if MAP_SIZE_X > x >= 0 and MAP_SIZE_Y > y >= 0 and MAP_SIZE_X > tx >= 0 and MAP_SIZE_Y > ty >= 0:
            if next_map[tx][ty] != BLOCK_WALL and next_map[tx][ty] != BLOCK_INDIVIDUAL:
                next_map[tx][ty] = BLOCK_INDIVIDUAL
                next_map[x][y] = BLOCK_EMPTY
    elif map[x][y] == BLOCK_WALL:
        next_map[x][y] = map[x][y]


def move_individual_north(x, y):
    move_individual(x, y, x - 1, y)


def move_individual_south(x, y):
    move_individual(x, y, x + 1, y)


def move_individual_east(x, y):
    move_individual(x, y, x, y + 1)


def move_individual_west(x, y):
    move_individual(x, y, x, y - 1)


def move_individual_north_west(x, y):
    move_individual(x, y, x - 1, y - 1)


def move_individual_south_west(x, y):
    move_individual(x, y, x + 1, y - 1)


def move_individual_north_east(x, y):
    move_individual(x, y, x - 1, y + 1)


def move_individual_south_east(x, y):
    move_individual(x, y, x + 1, y + 1)


def print_map():

    for x in range(MAP_SIZE_X):
        for y in range(MAP_SIZE_Y):
            sys.stdout.write(map[x][y])
        sys.stdout.write("\n")


def init_map(door_spacing, number_of_individuals):

    individual_count = 0

    for y in range(MAP_SIZE_Y):
        for x in range(MAP_SIZE_X):
            if individual_count < number_of_individuals:
                map[x][y] = BLOCK_INDIVIDUAL
                individual_count += 1
            else:
                map[x][y] = BLOCK_EMPTY

    for i in range(MAP_SIZE_X):
        if i % door_spacing != 1:
            map[i][MAP_SIZE_Y / 2] = next_map[i][MAP_SIZE_Y / 2] = BLOCK_WALL


def simulate():
    generation_count = 0
    while stopping_condition() == 1:
        os.system("cls") if platform.system() == "Windows" else os.system("clear")
        print "Ctrl+C to stop for now..."
        print_map()
        generation_count += 1
        print "Generation: %d" % generation_count
        for x in range(MAP_SIZE_X):
            for y in range(MAP_SIZE_Y):
                make_smart_move(x, y)
        update_map()


# Your smart stopping condition goes here
def stopping_condition():
    return 1


# Your smart crowd code goes here
def make_smart_move(x, y):
    random_move(randint(1, 8), x, y)


def random_move(r, x, y):
    if r == 1:
        return move_individual_north(x, y)
    if r == 2:
        return move_individual_south(x, y)
    if r == 3:
        return move_individual_east(x, y)
    if r == 4:
        return move_individual_west(x, y)
    if r == 5:
        return move_individual_north_east(x, y)
    if r == 6:
        return move_individual_north_west(x, y)
    if r == 7:
        return move_individual_south_east(x, y)
    if r == 8:
        return move_individual_south_west(x, y)

init_map(DOOR_SPACING, NUMBER_OF_INDIVIDUALS)
simulate()
