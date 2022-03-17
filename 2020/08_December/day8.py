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

    for line in puzzle_input:
        inputs = line.split(" ")
        line = (inputs[0], int(inputs[1]))
    puzzle_input = [(x[:3],int(x[4:])) for x in puzzle_input]
    return puzzle_input

# Helper Functions
def find_infinite_loop(puzzle_input):

    seen_ixs = []
    acc = 0
    curr_ix = 0

    while (curr_ix not in seen_ixs) & (curr_ix < len(puzzle_input)):
        
        seen_ixs.append(curr_ix)
        instr, amt = puzzle_input[curr_ix]

        if instr == "jmp":
            curr_ix = curr_ix + amt
            continue

        if instr == "acc":
            acc += amt

        curr_ix += 1 

    # If we've reached the end  
    # We may not see every index, so we want to just check if we saw the last one
    # Assumption: one of these options makes it to the end
    made_it_to_end = max(seen_ixs) == (len(puzzle_input) - 1)

    return acc,made_it_to_end

def swap_jmp_nop(instr):

    if instr[0] == "jmp":
        new_instr = "nop"
    else:
        new_instr = "jmp"
    return (new_instr,instr[1])

def fix_corrupt_instruction(puzzle_input):


    # Find the ixs of the jumps and nops
    jump_nop_ixs = [i for i,x in enumerate(puzzle_input) if x[0] in ['nop', 'jmp']]
    # Iterate through each one and try to swap it
    for ix in jump_nop_ixs:
        # Swap it 
        new_input = [x if i != ix else swap_jmp_nop(x) for i,x in enumerate(puzzle_input) ]

        # modify our find_infinite_loop func to indicate whether it made it to the end
        acc,made_it_to_end = find_infinite_loop(new_input)

        # break when we find one that works!
        # Assumption: we'll always find one
        if made_it_to_end:
            return acc

# Part 1
def part1(puzzle_input):
    # Since we're guaranteed to hit an infinite loop
    # Only need to access accumulator
    return find_infinite_loop(puzzle_input)[0]

# Part 2
def part2(puzzle_input):
    
    part2_answer = fix_corrupt_instruction(puzzle_input)
    return part2_answer

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input)
    print(f"Part 1: The accumulator was at {part1_answer} when we got stuck")

    part2_answer = part2(puzzle_input)
    print(f"Part 2: The accumulator was at {part2_answer} when we reached the end")


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