# Imports
import math
import sys
import numpy as np
from collections import Counter, defaultdict
from itertools import combinations, permutations
import time

# Parse Input
def parse_input(raw_input):
    with open(raw_input) as f:
        puzzle_input = [int(x) for x in f.read().split(",")]
    return puzzle_input

# Helper Functions
def generate_next_num(curr_num, curr_turn, last_seen):
    
    # If we've seen the number before, return the number of turns since it was last said
    if curr_num in last_seen:
        return curr_turn - last_seen[curr_num]
    
    # otherwise, if this was first time number was seen, return 0
    else:
        return 0

# Part 1
def part1(puzzle_input, n_turns):
    
    turns = 0
    next_num = puzzle_input[0]
    last_seen = {}
    
    start = time.time()
    
    while turns < n_turns:
        
        # curr_num = next_num
        curr_num = next_num

        # If we're in the input, next_num = next number in input
        # But when we're looking at the last one, we want to for real generate
        # Assumption: no duplicates in input
        if turns < len(puzzle_input) - 1:
            next_num = puzzle_input[turns+1]
        
        # else: next_num = generate the next number(..insert args..)
        else:
            next_num = generate_next_num(curr_num, turns, last_seen)
        
        # update the list of last seen (curr_num = n_turns)
        last_seen[curr_num] = turns

        # turns += 1
        turns += 1
        
    print(f"Ran in {round(time.time() - start,2)} seconds")

    return curr_num

# Part 2
def part2(puzzle_input,n):
    part2_answer = part1(puzzle_input,n)
    return part2_answer

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input,2020)
    print(f"Part 1: On the 2,020th turn, the number was {part1_answer}")

    part2_answer = part2(puzzle_input,30000000)
    print(f"Part 2: On the 30,000,000th turn, the number was {part2_answer}")


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