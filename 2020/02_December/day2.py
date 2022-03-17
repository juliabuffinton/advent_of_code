# Imports
import math
import sys
from collections import Counter

# Parse Input
def parse_input(raw_input):

    with open(raw_input) as f:
        puzzle_input = f.read().splitlines()

    new_input = {}
    for line in puzzle_input:
        rule, pword = line.split(": ")
        bounds,letter = rule.split(" ")
        lower, upper = [int(x) for x in bounds.split("-")]
    
        new_input[pword] = [(lower, upper), letter]
    return new_input

# Helper Functions
def check_valid(pword,rule):
    bounds, letter = rule
    pword_chars = Counter(pword)

    return (pword_chars[letter] >= bounds[0]) & (pword_chars[letter] <= bounds[1])

# Part 1
def part1(puzzle_input):
    valid_pwords = 0

    for pword,rule in puzzle_input.items():
        if check_valid(pword,rule):
            valid_pwords += 1

    part1_answer = valid_pwords
    print(f"Part 1: {part1_answer} passwords are valid according to their policies")
    

# Part 2
def part2(puzzle_input):
    valid_pwords = 0

    for pword,rule in puzzle_input.items():
        ixs, char = rule

        if (pword[ixs[0]-1] == char) ^  (pword[ixs[1]-1] == char):
            valid_pwords += 1
    
    part2_answer = valid_pwords
    print(f"Part 2: {part2_answer} passwords are valid according to their policies")

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    # Complete Part 1
    part1(puzzle_input)

    # Complete Part 2
    # Optional: Part 2 input may be different from Part 1 input
    part2(puzzle_input)


if __name__ == "__main__":
    # Assumption: filename is of type day[num].py
    # So we can get the day number from the filename
    puzzle_num = sys.argv[0].split(".")[0][3:]

    test_flag = int(sys.argv[1])

    # Assumption: my test and final input files also follow these naming conventions
    test_input = f"day{puzzle_num}_test_input.txt"
    raw_input = f"day{puzzle_num}_input.txt"

    if test_flag:
        main(test_input)
    else:
        main(raw_input)