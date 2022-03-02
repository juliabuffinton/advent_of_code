# Imports
import math
import sys

# Parse Input
def parse_input(raw_input):
    with open(raw_input) as f:
        puzzle_input = f.read().splitlines()
    return puzzle_input

# Helper Functions
def partition(boarding_pass, upper):
    '''
    For a group of characters in a boarding pass, 
    Return the new range of potential seats based on
    the character.
    '''
    lower = 0
    
    for loc in boarding_pass:
        rng = upper - lower

        if loc == 'B':
            lower = lower + math.ceil(rng/2)
        else:
            upper = lower + math.floor(rng/2)
        
    return lower

def find_seat_id(boarding_pass):
    '''
    Find the ID of the seat by partitioning the potential seats 
    based on the characters in the boarding pass. The first seven characters
    indicate Front-Back partitioning (128 rows on plane) and the last three
    characters indicate Right-Left (8 seats across).
    '''
    boarding_pass = boarding_pass.replace("R","B").replace("L","F")
    
    row = partition(boarding_pass[:7],128)
    col = partition(boarding_pass[7:],8)
    
    return row * 8 + col

# Part 1
def part1(puzzle_input):
    all_seat_ids = [find_seat_id(x) for x in puzzle_input]
    print(f"Part 1: The highest seat ID on a boarding pass is {max(all_seat_ids)}")
    return all_seat_ids

# Part 2
def part2(all_seat_ids):
    potential_seats = range(min(all_seat_ids),max(all_seat_ids)+1)
    my_seat = set(potential_seats) - set(all_seat_ids)
    print(f"Part 2: The ID of my seat is {my_seat}")

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    all_seat_ids = part1(puzzle_input)
    part2(all_seat_ids)


if __name__ == "__main__":
    raw_input = sys.argv[1]
    main(raw_input)