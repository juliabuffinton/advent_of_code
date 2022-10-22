# Imports
import sys
import os
import argparse

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
def repl_vals_1_and_2(intcode_program, val1, val2):
    intcode_program[1] = val1
    intcode_program[2] = val2
    
    return intcode_program
    
# Part 1
def part1(puzzle_input):
    
    intcode_program = puzzle_input.copy()
    intcode_program = repl_vals_1_and_2(intcode_program, 12, 2)
    
    intcode_program = intcoder.process_program(intcode_program)
    part1_answer = intcode_program[1][0]
    return part1_answer

# Part 2
def part2(puzzle_input):
    
    target_output = 19690720
    
    for noun in range(0,100):
        for verb in range(0,100):
            
            # Make sure to copy the input otherwise you won't start fresh!
            intcode_program = puzzle_input.copy()
            
            intcode_program = repl_vals_1_and_2(intcode_program, noun, verb)
            intcode_program = intcoder.process_program(intcode_program)
            output = intcode_program[1][0]
            
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
        
    input_loc = os.path.join(current_dir,input_file)
        
    main(input_loc)