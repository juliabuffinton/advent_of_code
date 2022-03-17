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
    return puzzle_input

# Helper Functions


# Part 1
def part1(puzzle_input):
    part1_answer = ""
    return part1_answer

# Part 2
def part2(puzzle_input):
    part2_answer = ""
    return part2_answer

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input)
    print(f"Part 1: {part1_answer}")

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