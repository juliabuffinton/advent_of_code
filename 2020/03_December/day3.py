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
    
    puzzle_input = np.array([list(x) for x in puzzle_input])
    return puzzle_input

# Helper Functions
def get_tree_count(puzzle_input, x_slope=3, y_slope=1):
    x,y = (0,0)
    right_bound, bottom_bound = len(puzzle_input[0]), len(puzzle_input)
    tree_count = 0

    # While we haven't hit the end of our forest
    while y < (bottom_bound - 1):
        x,y = x + x_slope, y + y_slope

        if puzzle_input[y][(x % right_bound)] == "#":
            tree_count += 1

    return tree_count

# Part 1
def part1(puzzle_input):

    part1_answer = get_tree_count(puzzle_input)
    print(f"Part 1: I encountered {part1_answer} trees")

# Part 2
def part2(puzzle_input):

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    tree_count = []

    for slope in slopes:
        tree_count.append(get_tree_count(puzzle_input, slope[0], slope[1]))
    part2_answer = np.prod(tree_count)
    print(f"Part 2: I get {part2_answer} when multiplying the number of trees encountered")

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1(puzzle_input)
    part2(puzzle_input)


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