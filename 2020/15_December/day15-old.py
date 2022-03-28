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
def gen_next_num(seen, prev):

    most_recent = seen[prev]
    
    # If that was the first time the number has been spoken, the current player says 0.
    if len(most_recent) == 1:
        return 0
    else: 
        # how many turns apart the number is from when it was previously spoken.
        return most_recent[0] - most_recent[1]


# Part 1
def part1(puzzle_input,n):

    start = time.time()

    seen = defaultdict(list)

    for i,starter in enumerate(puzzle_input):
        seen[starter].append(i)
        prev_num = starter
    
    for num_seen in range(len(puzzle_input),n):

        # Prev_num is now the next number spoken
        prev_num = gen_next_num(seen, prev_num)
        
        if prev_num in seen.keys():
            # keep track of current index and the most recent
            seen[prev_num] = [num_seen, seen[prev_num][0]]
        else:
            # Otherwise need to start the list
            seen[prev_num] = [num_seen]

    part1_answer = prev_num
    print(f"Ran in {round(time.time() - start,2)} seconds")
    return part1_answer

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