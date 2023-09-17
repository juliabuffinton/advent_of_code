# Imports
import sys
import os
import argparse
import re

import numpy as np
import pandas as pd
from operator import add
import time
import bisect
import math

# Parse Input
def parse_input(raw_input):
        
    pattern = "<*[x-z]="
    
    with open(raw_input) as f:
        puzzle_input = f.read().splitlines()
    puzzle_input = [x.split(", ") for x in puzzle_input]
    puzzle_input = [[re.sub(pattern, "", x) for x in l] for l in puzzle_input]
    puzzle_input = [[int(x.replace(">", "")) for x in l] for l in puzzle_input]
    puzzle_input = [np.array(x) for x in puzzle_input]
    return puzzle_input

# Helper Functions
def compare_vals(x, y):
    if x > y:
        return -1
    elif x < y:
        return 1
    elif x == y:
        return 0

def update_velocity(moon, other_moons, velocity):
    
    for axis in range(3):
        for other_moon in other_moons: 
            velocity[axis] += compare_vals(moon[axis], other_moon[axis])
    
    return velocity 

def update_moon_position(moons, velocities):
    
    new_moons = []
    new_velocities = []
    total_energy = 0
    
    # print(f"start moons: {moons}")
    # print(f"start velos: {velocities}")
    
    # For each moon 
    for i, moon in enumerate(moons):
        velo = velocities[i].copy()
        
        other_moons = moons[:i]+moons[i+1:]
    
        # Calculate the velocity
        new_velocity = update_velocity(moon,other_moons, velo)
        new_velocities.append(new_velocity)
    
        # Update position
        new_moon = moon + new_velocity
        new_moons.append(new_moon)
        
        # Calculate energy
        total_energy += calc_energy(new_moon) * calc_energy(new_velocity)
        
    # print(f"moons: {new_moons}")
    # print(f"velos: {new_velocities}")
    # print(f"total energy: {total_energy}")
    # print()
    return total_energy, new_moons, new_velocities
    
def calc_energy(coords):
    x,y,z = coords
    return abs(x) + abs(y) + abs(z)

def binary_search(L, target):
    start = 0
    end = len(L) - 1
    
    if not L:
        # handle if the list we're checking is empty
        return False

    while start <= end:
        middle = math.floor((start + end)/ 2) # Does it matter if we do ceil or floor?
        midpoint = L[middle]
        
        if midpoint > target:
            end = middle - 1
            
        elif midpoint < target:
            start = middle + 1
            
        elif midpoint == target:
            return True
    
    return False
 
# Part 1
def part1(puzzle_input,n=1000):
    
    moons = [x for x in puzzle_input]
    
    energies = []
    velocities = [np.zeros(3)] * 4
    
    for i in range(n):
        if i % 100 == 0:
            print(f"working on iteration {i}...")
        total_energy, moons, velocities = update_moon_position(moons, velocities)
                
    return total_energy

# Part 2
def part2(puzzle_input):
    
    start = time.time()

    # Keep track of everything we found previously (sorted)
    seen_orbits = set()
    # seen_orbits = []
    seen_before = False
    i = 0

    moons = [x for x in puzzle_input]
    
    velocities = [np.zeros(3)] * 4
    
    while not seen_before:
        
        if i % 100000 == 0:
            print(f"working on iteration {i}... after {round((time.time() - start) / 60, 1)} minutes...")
        _, moons, velocities = update_moon_position(moons, velocities)
        # print(moons)
        moons_flattened = "".join([str(x) for x in list(np.array(moons).flatten())])
        # print(moons_flattened)
        
        # if binary_search(seen_orbits, moons_flattened):
        if moons_flattened in seen_orbits:
            seen_before = True
        else:
            # bisect.insort(seen_orbits, moons_flattened) 
            seen_orbits.add(moons_flattened)
        
        i += 1  
    
    print(f"Total time: {round(time.time() - start, 5)}")
 
    return i

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input)
    print(f"Part 1: {part1_answer}")

    part2_answer = part2(puzzle_input)
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