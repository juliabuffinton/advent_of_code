# Imports
import sys
import os
import argparse

# Is there a better way to import a module from a parent directory?
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
# import intcoder

# Parse Input
def parse_input(raw_input):
    with open(raw_input) as f:
        puzzle_input = f.read().splitlines()
    
    puzzle_input = [x.split(" ") for x in puzzle_input]
    
    return puzzle_input

# Helper Functions  
    
# Part 1
def part1(puzzle_input):
    
    valid_passphrases = 0 
    
    for passphrase in puzzle_input:
        
        if len(set(passphrase)) == len(passphrase):
            valid_passphrases += 1
             
    return valid_passphrases

# Part 2
def part2(puzzle_input):
    
    valid_passphrases = 0 
    
    for passphrase in puzzle_input: 
        passphrase = [''.join(sorted(x)) for x in passphrase]
        
        if len(set(passphrase)) == len(passphrase):
            valid_passphrases += 1
    
    return valid_passphrases

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