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
        puzzle_input = f.read().splitlines()
    puzzle_input = [x.split(")") for x in puzzle_input]
    # Orbiter is key; orbitee is value
    puzzle_input = {k:v for v,k in puzzle_input}
    
    return puzzle_input

# Helper Functions
def get_orbit(object, orbit_dict, counter):
    
    # get the object that this object orbits
    next_object = orbit_dict.get(object)
    
    # if we it isn't a key, we've reached the end
    if not next_object:
        return counter
    else:
        counter += 1
        return get_orbit(next_object, orbit_dict, counter)

    
# Part 1
def part1(puzzle_input):
    
    total_orbits = 0
    
    for object in puzzle_input:
        orbits = get_orbit(object, puzzle_input, 0)
        print(f"object {object} has {orbits} orbits")

        total_orbits += orbits
        
    return total_orbits

# Part 2
def part2(puzzle_input):
    
    visited = []
    
    pass

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input)
    print(f"Part 1: {part1_answer}")

    # part2_answer = part1(puzzle_input, [5])
    # print(f"Part 2: {part2_answer}")


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