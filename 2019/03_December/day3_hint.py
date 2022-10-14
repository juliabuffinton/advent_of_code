# Imports
import sys
import os

# Parse Input
def parse_input(raw_input):
    
    with open(raw_input) as f:
        puzzle_input = f.read().splitlines()
    puzzle_input = [x.split(",") for x in puzzle_input]
    
    return puzzle_input

# Helper Functions          

def find_points_on_path(path):
    '''
    Generate all points encountered by a single wire
    when following path from instructions
    '''
    # Start at the "origin" and keep track of each point encountered
    x,y = 0,0
    all_points = []
    
    # for each instruction, get the points from start to end
    for instr in path:
                        
        if dir in ["R", "L"]:
            # move according to directions, add all points encountered
            # TODO!
            pass
        elif dir in ["U", "D"]:
            # move according to directions, add all points encountered
            # TODO!
            pass
        else:
            print("We got an instruction we didn't expect!")
                   
    return all_points
    
def find_all_shared_points(paths):
    '''
    Given two paths, find all the points that appear on both paths
    '''
    
    # TODO! 
    pass

def calc_manhattan_dist_between_points(point1 , point2):
    '''
    Take in two points as tuple and return manhattan distance
    '''
    x_dist = abs(point1[0] - point2[0])
    y_dist = abs(point1[1] - point2[1])
    
    return x_dist + y_dist
    
# Part 1
def part1(puzzle_input):

    # Get all points for each wire
    
    # Find the shared points
    
    # Calculate Manhattan distance for shared points 

    # Return the point that has the lowest Manhattan distance
    return 

# Part 2
def part2(puzzle_input):
    
    # Get all points for each wire + how many steps it takes to get to them
    
    # Find the shared points
    
    # Calculate total steps (steps for wire 1 + steps for wire 2)

    # Return the point that has the lowest total steps
    return 

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

    input_file = "input.txt"
        
    input_loc = os.path.join(loc,input_file)
        
    main(input_loc)