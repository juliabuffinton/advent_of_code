# Imports
import sys
import os
import argparse

import numpy as np
import pandas as pd

# Is there a better way to import a module from a parent directory?
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)
import intcoder


# Parse Input
def parse_input(raw_input):
    with open(raw_input) as f:
        puzzle_input = f.read().strip()
    # puzzle_input = [int(x) for x in [*puzzle_input.strip()]]
    return puzzle_input

# Helper Functions
    
# Part 1
def part1(puzzle_input, width, height):
    
    chunk_size = width * height
    
    # Shamelessly stolen: https://pythonexamples.org/python-split-string-into-specific-length-chunks/
    chunks = [puzzle_input[i:i+chunk_size] for i in range(0, len(puzzle_input), chunk_size)]
    
    # find number of zeros in each layer
    zero_counts = [s.count('0') for s in chunks]
    
    fewest_zeros_loc = zero_counts.index(min(zero_counts))
    
    fewest_zeros = chunks[fewest_zeros_loc]
    
    ones = fewest_zeros.count("1")
    twos = fewest_zeros.count("2")
        
    return ones * twos

# Part 2
def part2(puzzle_input, width, height):
    
    chunk_size = width * height
    
    # Shamelessly stolen: https://pythonexamples.org/python-split-string-into-specific-length-chunks/
    layers = [puzzle_input[i:i+chunk_size] for i in range(0, len(puzzle_input), chunk_size)]
    
    final_output = []
    
    for i in range(chunk_size):
        # get the corresponding pixels from all layers
        pixels = [x[i] for x in layers]
    
        # find the first non-2
        for pixel in pixels:
            if pixel != '2':
                if pixel == '0':
                    pixel = '' # makes it easier to see the ouptut
                final_output.append(pixel)
                break 
    
    # Arrange pixels
    reshaped = np.array(final_output).reshape(height, width)
    
    # Easier to see in a DF
    return pd.DataFrame(reshaped)

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input, 25, 6)
    print(f"Part 1: {part1_answer}")

    part2_answer = part2(puzzle_input, 25, 6)
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