# Imports
from http.client import IncompleteRead
import sys
import os

# Parse Input
def parse_input(raw_input):
    with open(raw_input) as f:
        puzzle_input = f.read()
    puzzle_input = [int(x) for x in puzzle_input.split(",")]
    
    return puzzle_input

# Helper Functions
def process_opcode(intcode_program, input):
    
    output = -1
    instr_pointer = 0
    write_opcodes = [1, 2, 3, 7, 8]
    
    three_param_opcodes = [1, 2, 7, 8]
    two_param_opcodes = [5, 6]
    one_param_opcodes = [3, 4]
    
    # opcode - either 1, 2, 3, or 99
    # TODO: Do we need to check if we reach the end of the list?
    while instr_pointer < len(intcode_program):

        # instr may be 0 - 5 digits
        instr = str(intcode_program[instr_pointer]).zfill(5)
        
        # Each argument has a mode specified by digits
        # TODO: Will there be more args?
        opcode = int(instr[-2:])
        
        if opcode == 99:
            break
        
        arg1_mode = int(instr[-3])
        arg2_mode = int(instr[-4])
        
        arg1 = intcode_program[instr_pointer+1]
        arg2 = intcode_program[instr_pointer+2]
        
        # TODO: Handle this more gracefully
        try:
            arg3 = intcode_program[instr_pointer+3]
        except:
            arg3 = 0
        
        # here is for all our 3-param opcodes
        if opcode in three_param_opcodes:   
        
            if opcode in [1,2]:
                if arg1_mode == 0:
                    arg1 = intcode_program[arg1]
                if arg2_mode == 0:
                    arg2 = intcode_program[arg2]
                    
                if opcode == 1:
                    write_val = arg1 + arg2
                elif opcode == 2:
                    write_val = arg1 * arg2
                
            
            # Comparison opcodes
            if opcode in [7, 8]:
                         
                if arg1_mode == 0:
                    arg1 = intcode_program[arg1]
                if arg2_mode == 0:
                    arg2 = intcode_program[arg2]
                
                if opcode == 7:
                    write_val = int(arg1 < arg2)
                    
                if opcode == 8:
                    write_val = int(arg1 == arg2)
            
            write_loc = arg3
            instr_pointer += 4
                
        # Here is for all of our 1-param opcodes
        elif opcode in one_param_opcodes:
            
            if opcode == 3:
                write_val = input
                write_loc = arg1
                
            elif opcode == 4:
                if arg1_mode == 1:
                    output = arg1
                elif arg1_mode == 0:
                    output = intcode_program[arg1]

            instr_pointer += 2
            
        # Here is for all our 2-param opcodes
        elif opcode in two_param_opcodes:
            
            if arg1_mode == 0:
                arg1 = intcode_program[arg1]
            if arg2_mode == 0:
                arg2 = intcode_program[arg2]
            
            # Jump opcodes
            if opcode == 5:
                jump = arg1 != 0 
        
            # if first param is 0, jump
            elif opcode == 6:
                jump = arg1 == 0 
            
            if jump:
                instr_pointer = arg2
            else:
                instr_pointer += 3 
                            
        # Only write for certain opcodes
        if opcode in write_opcodes:
            intcode_program[write_loc] = write_val
            
    return output, intcode_program
    
# Part 1
def part1(puzzle_input, input):
    
    intcode_program = puzzle_input.copy()
    
    output, intcode_program = process_opcode(intcode_program, input)
    part1_answer = output
    return part1_answer

# Part 2
def part2(puzzle_input):
    pass

# Put it all together
def main(raw_input):
    puzzle_input = parse_input(raw_input)
    
    part1_answer = part1(puzzle_input,1)
    print(f"Part 1: {part1_answer}")

    part2_answer = part1(puzzle_input, 5)
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