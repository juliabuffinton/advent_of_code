# Imports
import sys
import os
import argparse

from typing import List

# Is there a better way to import a module from a parent directory?
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import intcoder


# Parse Input
def parse_input(raw_input):
    with open(raw_input) as f:
        puzzle_input = f.read()
    puzzle_input = [int(x) for x in puzzle_input.split(",")]
    
    return puzzle_input

# Helper Functions
    
# Part 1
def part1(puzzle_input, input_vals):
    
    intcode_program = puzzle_input.copy()
    
    output, intcode_program = intcoder.process_program(intcode_program, input_vals)
    part1_answer = output
    return part1_answer

# Part 2
def part2(puzzle_input):
    pass

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input,[1])
    print(f"Part 1: {part1_answer}")

    part2_answer = part1(puzzle_input, [5])
    print(f"Part 2: {part2_answer}")


if __name__ == "__main__":

    # Get the location of this file, assumption that input is stored in same dir
    loc = os.path.dirname(os.path.abspath(__file__))

    parser = argparse.ArgumentParser()
    parser.add_argument('--test', '-t', 
                        action='store_true', 
                        help="indicator that this script should be run with test data")

    args = parser.parse_args()

    # Check if we got any arguments
    if args.test:
        input_file = "input_test.txt"
    else:
        input_file = "input.txt"
        
    input_loc = os.path.join(loc,input_file)
        
    main(input_loc)