# Imports
from gettext import find
import sys
import os
import pandas as pd

# Parse Input
def parse_input(raw_input):
    
    with open(raw_input) as f:
        # Two lines, one for each wire
        puzzle_input = f.read().splitlines()
    puzzle_input = [x.split(",") for x in puzzle_input]
    
    return puzzle_input

# Helper Functions          

def find_points_on_path(path):
    
    x,y = 0,0
    all_points = []
    step = 1
    
    # for each instruction, get the points from start to end
    for instr in path:
        
        dir = instr[0]
        dist = int(instr[1:])
        sign = 1
                
        if dir in ["R", "L"]:
            if dir == "L":
                sign = -1
            # 1 because we don't need to include current point
            for incr in range(1, dist+1):
                x += 1 * sign
                all_points.append((step,(x,y)))
                step += 1

        elif dir in ["U", "D"]:
            if dir == "D":
                sign = -1
            # 1 because we don't need to include current point
            for incr in range(1, dist+1):
                y += 1 * sign
                all_points.append((step,(x,y)))
                step += 1
                   
    return pd.DataFrame(all_points, columns=["step", "point"])
    
def get_all_shared_points(paths):
    path1 = find_points_on_path(paths[0])
    path2 = find_points_on_path(paths[1])
    
    # Find the intersection between each set of points
    shared_points = path1.merge(path2, on="point", how="inner", suffixes=("_1", "_2"))

    return shared_points

def calc_manhattan_dist_between_points(point1, point2):
    
    x_dist = abs(point1[0] - point2[0])
    y_dist = abs(point1[1] - point2[1])
    
    return x_dist + y_dist
    
# Part 1
def part1(puzzle_input):

    shared_points = get_all_shared_points(puzzle_input)
    
    shared_points["manhattan_distance"] = shared_points.apply(lambda row: calc_manhattan_dist_between_points((0,0),row.point), axis=1)
    return shared_points.manhattan_distance.min()

# Part 2
def part2(puzzle_input):
    
    shared_points = get_all_shared_points(puzzle_input)

    shared_points["total_steps"] = shared_points.step_1 + shared_points.step_2
    return shared_points.total_steps.min()

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

    # TODO: if no flag, treat as normal mode
    test_flag = int(sys.argv[1]) # 1 = test; 0 = normal mode

    if test_flag:
        input_file = "input_test.txt"
    else:
        input_file = "input.txt"
        
    input_loc = os.path.join(loc,input_file)
        
    main(input_loc)