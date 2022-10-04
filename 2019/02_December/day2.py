# Imports
import math
import sys
import numpy as np
from collections import Counter, defaultdict
from itertools import combinations, permutations
import time
import os

# Parse Input
def parse_input(raw_input):
    with open(raw_input) as f:
        puzzle_input = f.read()
    puzzle_input = [int(x) for x in puzzle_input.split(",")]
    
    return puzzle_input

# Helper Functions
def process_opcode(intcode_program):
    
    instr_pointer = 0

    opcode = intcode_program[0]
    
    # opcode - either 1, 2, or 99
    while opcode != 99:

        arg1_loc = intcode_program[instr_pointer+1]
        arg2_loc = intcode_program[instr_pointer+2]
        output_loc = intcode_program[instr_pointer+3]
        
        if opcode == 1:
            output = intcode_program[arg1_loc] + intcode_program[arg2_loc]
        elif opcode == 2:
            output = intcode_program[arg1_loc] * intcode_program[arg2_loc]

        intcode_program[output_loc] = output
        
        instr_pointer += 4
        opcode = intcode_program[instr_pointer]
    
    return intcode_program
    
def repl_vals_1_and_2(intcode_program, val1, val2):
    intcode_program[1] = val1
    intcode_program[2] = val2
    
    return intcode_program
    
# Part 1
def part1(puzzle_input):
    
    intcode_program = puzzle_input.copy()
    intcode_program = repl_vals_1_and_2(intcode_program, 12, 2)
    
    intcode_program = process_opcode(intcode_program)
    part1_answer = intcode_program[0]
    return part1_answer

# Part 2
def part2(puzzle_input):
    
    target_output = 19690720
    
    for noun in range(0,100):
        for verb in range(0,100):
            
            # Make sure to copy the input otherwise you won't start fresh!
            intcode_program = puzzle_input.copy()
            
            intcode_program = repl_vals_1_and_2(intcode_program, noun, verb)
            intcode_program = process_opcode(intcode_program)
            output = intcode_program[0]
            
            if output == target_output:
                part2_answer = 100 * noun + verb
                return part2_answer

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input)
    print(f"Part 1: {part1_answer}")

    part2_answer = part2(puzzle_input)
    print(f"Part 2: {part2_answer}")


if __name__ == "__main__":

    # Get the location of this file, assumption that input stored in same dir
    loc = sys.argv[0].rsplit("/",1)[0]

    # TODO: if no flag, treat as not test
    test_flag = int(sys.argv[1]) # 1 = test

    if test_flag:
        main(os.path.join(loc,"input_test.txt"))
    else:
        main(os.path.join(loc,"input.txt"))