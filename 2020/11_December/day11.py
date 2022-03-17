# Imports
import math
import sys
import numpy as np
from collections import Counter
from itertools import combinations, permutations

# Parse Input
def parse_input(raw_input):
    with open(raw_input) as f:
        puzzle_input = f.read().splitlines()

    # print(f"Length of input = {len(puzzle_input)}")
    
    puzzle_input = np.array([np.array(list(x)) for x in puzzle_input])
    return puzzle_input

# Helper Functions  
def get_all_neighbors(horiz_length, vert_length, start_point):
    x,y = start_point
    # print()
    print(f"starting at {start_point}")
    neighbors = []

    for new_x in range(x-1, x+2):
        if (new_x >= horiz_length) | (new_x < 0):
            continue
        for new_y in range(y-1, y+2):
            if (new_y >= vert_length) | (new_y < 0):
                continue
            neighbors.append((new_x, new_y))

    neighbors.remove(start_point)
    # print(f"Found neighbors: {neighbors}")
    return neighbors

def get_num_occupied_neighbors(seat_map, seat_x, seat_y):
    num_occupied = 0
    vert_length, horiz_length = seat_map.shape
    # print(f"Shape: {horiz_length} (x) by {vert_length} (y)")

    neighbors = get_all_neighbors(horiz_length, vert_length, (seat_x,seat_y))
    for neighbor_x, neighbor_y in neighbors:
        if seat_map[neighbor_y][neighbor_x] == '#':
            num_occupied += 1
    return num_occupied

def update_seat(num_occupied_neighbors, seat_status):
    '''
    The following rules are applied to every seat simultaneously:
    - empty seats become occupied if no adjacent seats are occupied
    - occupied seats become empty if 4+ adjacent seats are occupied
    - otherwise, the seat's state does not change.
    '''
    if (seat_status == 'L') & (num_occupied_neighbors == 0):
        return '#'
    elif (seat_status == '#') & (num_occupied_neighbors >= 4):
        return 'L'
    else:
        return seat_status

def move_seats(curr_seat_map):

    new_seat_map = curr_seat_map.copy()

    vert_length, horiz_length = curr_seat_map.shape

    for y in range(vert_length):
        for x in range(horiz_length):
            num_occupied_neighbors = get_num_occupied_neighbors(curr_seat_map, x, y)
            seat_status = curr_seat_map[y][x]
            new_seat_map[y][x] = update_seat(num_occupied_neighbors, seat_status)
    return new_seat_map

# Part 1
def part1(puzzle_input):

    curr_seat_map = puzzle_input
    seats_changed = True
    
    # While movement did happen move again
    while seats_changed:
        new_seat_map = move_seats(curr_seat_map)

        if (new_seat_map == curr_seat_map).all():
            seats_changed = False
        else:
            curr_seat_map = new_seat_map

    # Return the final number of occupied seats once things settle
    
    # TODO: Figure out how to count all the '#' in our numpy array
    part1_answer = (curr_seat_map == '#').sum()
    return part1_answer

# Part 2
def part2(puzzle_input):
    part2_answer = ""
    return part2_answer

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    # print(puzzle_input)
    
    part1_answer = part1(puzzle_input)
    print(f"Part 1: {part1_answer} seats are occupied when the seats stop changing")

    part2_answer = part2(puzzle_input)
    print(f"Part 2: {part2_answer}")


if __name__ == "__main__":
    # Assumption: filename is of type day[num].py
    # So we can get the day number from the filename
    puzzle_num = sys.argv[0].split(".")[0][3:]

    # TODO: if no flag, treat as not test
    test_flag = int(sys.argv[1]) # 1= test

    # Assumption: my test and final input files also follow these naming conventions
    test_input = f"day{puzzle_num}_test_input.txt"
    raw_input = f"day{puzzle_num}_input.txt"

    if test_flag:
        main(test_input)
    else:
        main(raw_input)