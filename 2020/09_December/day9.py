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

    puzzle_input = [int(x) for x in puzzle_input]
    return puzzle_input

# Helper Functions
def valid_num(prev_25,curr_num):
    '''
    Determine whether the current number is valid
    Valid = is the sum of 2 numbers that occur in the 
    25 previous numbers.
    '''
    pairs = list(combinations(prev_25,2))
    for pair in pairs:
        if sum(pair) == curr_num:
            return True
    return False
    
def find_invaid_num(nums):
    '''
    Find first number that is NOT valid and return it
    '''
    nums = nums.copy()
    
    is_valid = True
    
    while is_valid:
        curr_num = nums[25]
        is_valid = valid_num(nums[:25],curr_num)
        nums.pop(0)
    
    return curr_num

def find_contiguous(nums, target_num):
    '''
    Find a series of contiguous numbers that 
    ..........
    '''

    for i,num in enumerate(nums):
        total = 0
        
        j = i
        
        while total <= target_num:
            if total == target_num:
                return nums[i:j]
            else:
                total += nums[j]
                j+=1


# Part 1
def part1(puzzle_input):
    part1_answer = find_invaid_num(puzzle_input)
    return part1_answer

# Part 2
def part2(puzzle_input):
    invalid_num = find_invaid_num(puzzle_input)
    
    contiguous = find_contiguous(puzzle_input,invalid_num)

    part2_answer = max(contiguous) + min(contiguous)
    return part2_answer

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input)
    print(f"Part 1: {part1_answer}")

    part2_answer = part2(puzzle_input)
    print(f"Part 2: {part2_answer}")


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