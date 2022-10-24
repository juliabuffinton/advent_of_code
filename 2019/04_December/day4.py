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
    puzzle_input = [int(x) for x in puzzle_input.split("-")]
    
    return puzzle_input

# Helper Functions  
    
# Part 1
def part1(puzzle_input):
    good_nums = []
    
    # TODO: Is our range inclusive or exclusive or...?
    for num in range(puzzle_input[0], puzzle_input[1]):
        # Stretch goal and do this in a while loop, 
        # skip ahead smartly if we don't find what we need

        digits = [int(x) for x in str(num)]
        diffs = [y - x for x,y in zip(digits,digits[1:])]
                
        # if at any point we're not monotonically increasing
        # we just move on to the next number
        if any([x < 0 for x in diffs]):
            continue
        # otherwise let's see if we have a pair
        elif any([x == 0 for x in diffs]):
            good_nums.append(num)
                
    return len(good_nums)
    
# Part 2
def part2(puzzle_input):
    good_nums = []
    
    # TODO: Is our range inclusive or exclusive or...?
    for num in range(puzzle_input[0], puzzle_input[1]):
        # Stretch goal and do this in a while loop, 
        # skip ahead smartly if we don't find what we need

        digits = [int(x) for x in str(num)]
        diffs = [y - x for x,y in zip(digits,digits[1:])]
        
        def check_single_adjacent(diffs):
            if (diffs[0] == 0) & (diffs[1] != 0):
                return True
            elif (diffs[-1] == 0) & (diffs[-2] != 0):
                return True
            
            for i,x in enumerate(diffs):
                # nesting these IFs so we don't check extra if not zero? 
                # does this really make a difference? 
                if (i != 0) & (i != len(diffs)-1):
                    if (diffs[i] == 0):
                        if (diffs[i-1] > 0) & (diffs[i+1] > 0):
                        # We only need to find this once to say it fits the pattern
                        # so we can return as soon as we find one
                            return True
            return False
            
        # if at any point we're not monotonically increasing
        # we just move on to the next number
        if any([x < 0 for x in diffs]):
            continue
        # otherwise let's see if we have a pair
        elif check_single_adjacent(diffs):
            good_nums.append(num)
                
    return len(good_nums)

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input)
    print(f"Part 1: {part1_answer}")

    part2_answer = part2(puzzle_input)
    print(f"Part 2: {part2_answer}")

if __name__ == "__main__":

    # Get the location of this file, assumption that input is stored in same dir
    # loc = os.path.dirname(os.path.abspath(__file__))

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
