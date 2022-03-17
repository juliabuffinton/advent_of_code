# Imports
import math
import sys
import numpy as np
from collections import Counter
from itertools import combinations, permutations
import time as t

# Parse Input
def parse_input(raw_input):
    with open(raw_input) as f:
        puzzle_input = f.read().splitlines()

    puzzle_input = [int(x) for x in puzzle_input]
    return puzzle_input

# Helper Functions


# Part 1
def part1(puzzle_input, n):
    pairs = list(combinations(puzzle_input,n))

    for pair in pairs:
        if sum(pair) == 2020:
            return np.product(pair)

# Part 2
def part2(puzzle_input, n):
    part2_answer = part1(puzzle_input, 3)
    return part2_answer

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input, 2)
    print(f"Part 1: {part1_answer}")
    part2_answer = part2(puzzle_input, 3)
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