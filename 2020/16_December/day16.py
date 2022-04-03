# Imports
import math
import sys
import numpy as np
from collections import Counter, defaultdict
from itertools import combinations, permutations
import time

# Parse Input
def parse_input(raw_input):
    with open("day16_input.txt") as f:
        puzzle_input = f.read().split("\n\n")

    valid_fields = clean_fields(puzzle_input[0].split("\n"))
    my_ticket = parse_tickets(puzzle_input[1])[0]
    other_tickets = parse_tickets(puzzle_input[2])
    
    return valid_fields, my_ticket, other_tickets

# Helper Functions
def parse_tickets(ticket_list):
    tickets = ticket_list.split("\n")[1:]
    tickets = [ticket.split(",") for ticket in tickets]
    tickets = [[int(x) for x in ticket] for ticket in tickets]
    return tickets

def clean_fields(fields):
    fields_dict = {}
    
    for field in fields:
        field_name, vals = field.split(": ")
        ranges = [[int(x) for x in rng.split("-")] for rng in vals.split(" or ")]

        fields_dict[field_name] = ranges
    return fields_dict

def get_overall_ranges(valid_field_values):
    
    rng1_min = min([rng1[0] for rng1,rng2 in valid_field_values])
    rng1_max = max([rng1[1] for rng1,rng2 in valid_field_values])
    
    rng2_min = min([rng2[0] for rng1,rng2 in valid_field_values])
    rng2_max = max([rng2[1] for rng1,rng2 in valid_field_values])

    # If they overlap - I could have hard coded this but I didn't
    if rng2_min < rng1_max:
        return [(rng1_min, rng2_max)]
    else:
        return [(rng1_min, rng1_max), (rng2_min, rng2_max)]

def check_valid_tickets(tickets, rng):
    
    invalid_nums = []
    for ticket in tickets:
        invalid_nums.extend([x for x in ticket if not check_valid_num(x,rng)])
    return invalid_nums

def check_valid_num(num, rng):
    lower,upper = rng[0]
    # we know there is only one range - this I did hard code :(
    return (num >= lower) & (num <= upper)

def num_in_ranges(num, rng1, rng2):
    
    num_in_rng1 = rng1[0] <= num <= rng1[1]
    num_in_rng2 = rng2[0] <= num <= rng2[1]
    
    return num_in_rng1 | num_in_rng2

def map_fields_to_cols(potential_fields):
    
    actual_fields = {}
    n = 1
    used = []
    
    while len(potential_fields) > 0:        
        # Assumption that one column can only be assigned to one field
        # Find the one. This is sketchy.
        field, columns = [(k,v) for (k,v) in potential_fields.items() if len(v) == n][0]
        
        # Assumption we should be narrowing to 1
        confirmed_column = [x for x in columns if x not in used][0]
        
        # Add to actual fields. 
        actual_fields[field] = confirmed_column
                
        # pop this key from the dictionary
        potential_fields.pop(field)
        
        n += 1
        used.append(confirmed_column)
        
    return actual_fields 

# Part 1
def part1(valid_fields, my_ticket, other_tickets):

    overall_valid_range = get_overall_ranges(valid_fields.values())
    
    invalid_values =  check_valid_tickets(other_tickets, overall_valid_range)

    part1_answer = sum(invalid_values)
    return part1_answer

# Part 2
def part2(valid_fields, my_ticket, other_tickets):
    
    # Get the list of tickets that are actually valid
    overall_valid_range = get_overall_ranges(valid_fields.values())

    valid_tickets = [ticket for ticket in other_tickets if all([check_valid_num(num, overall_valid_range) for num in ticket])]
    
    potential_fields = {key: [] for key in valid_fields}
    
    # Find all the 'columns' that could work for each field
    for field_name, rngs in valid_fields.items():
        rng1, rng2 = rngs
        
        # get a list of all ticket locs            
        potential_locs = [column for column in range(len(valid_fields)) if all([num_in_ranges(x, rng1, rng2) for x in [ticket[column] for ticket in valid_tickets]])]        
        potential_fields[field_name] = potential_locs
    
    # Process of elimination: one col will only be valid for one field, then cross them off from there
    actual_fields = map_fields_to_cols(potential_fields)
    
    # Finally, get the departure values and multiple them together
    departure_cols = [field[1] for field in actual_fields.items() if "departure" in field[0]]
    departure_values = [value for (i, value) in enumerate(my_ticket) if i in departure_cols]
         
    part2_answer = np.prod(departure_values)
    return part2_answer

# Put it all together
def main(raw_input):
    valid_fields, my_ticket, other_tickets = parse_input(raw_input)
    
    part1_answer = part1(valid_fields, my_ticket, other_tickets)
    print(f"Part 1: My ticket scanning error rate is {part1_answer}")

    part2_answer = part2(valid_fields, my_ticket, other_tickets)
    print(f"Part 2: Multiplying the departure field values on my ticket produces {part2_answer}")


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