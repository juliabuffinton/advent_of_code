# Imports
import math
import sys
import numpy as np
from collections import Counter, defaultdict
from itertools import combinations, permutations
import time
import os
from pathlib import Path
import pandas as pd

# Parse Input
def parse_input(raw_input):
    with open(raw_input) as f:
        puzzle_input = f.read().splitlines()
    
    guards = []
    asleep = []
    awake = []
    date = []
    
    # Handle first line
    curr_guard, curr_status, curr_time, curr_date = parse_line(puzzle_input[0], 0)
    # guards.append(curr_guard)
    # awake.append(curr_time)
    # date.append(curr_date)
    
    for line in puzzle_input[1:]:
        # prev_guard = curr_guard
        curr_guard, curr_status, curr_time, curr_date = parse_line(line, curr_guard)
        
        if curr_status == "awake":
            
            # Assumption: Guards end their shift awake
            if curr_time < asleep[-1]:
                continue
            # guards.append(curr_guard)
            else:
                awake.append(curr_time)
            # date.append(curr_date)

        else:
            asleep.append(curr_time)
            guards.append(curr_guard)
            date.append(curr_date)
    # asleep.append(59)    
    
    puzzle_input = pd.DataFrame({"guard":guards, "asleep":asleep, "awake":awake, "date": date})
    return puzzle_input

# Helper Functions
def parse_line(line, curr_guard):
    date = line[1:11]
    time = int(line[15:17])

    if line[19] == "f":
        status = "asleep"
    else:
        if line[19] == "G":
            curr_guard = int(line[19:].split(' ')[1][1:])
            time = 0
        status = "awake"
    
    return curr_guard, status, time, date
        
def sleepiest_guard(df):
    df["mins_asleep"] = df.awake - df.asleep

    df = df.groupby("guard").agg({"mins_asleep":"sum"}).reset_index()
    df[df.mins_asleep == df.mins_asleep.max()].guard
    return ()
    
# Part 1
def part1(puzzle_input):
    df = puzzle_input
        
    part1_answer = f"The sleepiest guard is {sleepiest_guard(df)}"
    return part1_answer

# Part 2
def part2(puzzle_input):
    part2_answer = ""
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
    path = os.path.dirname(__file__)
    # TODO: if no flag, treat as not test
    test_flag = int(sys.argv[1]) # 1= test

    # Assumption: my test and final input files also follow these naming conventions
    test_input = Path(path)/"input_test.txt"
    raw_input = Path(path)/"input.txt"

    if test_flag:
        main(test_input)
    else:
        main(raw_input)