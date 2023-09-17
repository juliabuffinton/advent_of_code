#######################
# Imports
#######################
# from typing import List
from enum import Enum

#######################
# Enums
#######################
class Mode(Enum):
    POSITION = 0
    IMMEDIATE = 1

#######################
# Other Helper Funcs
#######################
def get_arg_value(arg, mode, intcode_program):
    if mode == Mode.POSITION.value:
        return intcode_program[arg]
    elif mode == Mode.IMMEDIATE.value:
        return arg
    else:
        print("Got a mode we weren't expecting!")

#######################
# Operators
#######################

def add(arg1, arg2):
    """opcode of 1"""
    return arg1 + arg2

def mult(arg1, arg2):
    """opcode of 2"""
    return arg1 * arg2

def write(arg1):
    """opcode of 3"""
    return arg1

def output_value(arg1):
    """opcode of 4"""
    return arg1

def jump_if_true(arg1):
    """opcode of 5"""
    return arg1 != 0

def jump_if_false(arg1):
    """opcode of 6"""
    return arg1 == 0

def less_than(arg1, arg2):
    """opcode of 7"""
    return int(arg1 < arg2)

def equals(arg1, arg2):
    """opcode of 8"""
    return int(arg1 == arg2)

#######################
# Program
#######################

def process_program(intcode_program, input_vals = []):
    
    output = -1
    instr_pointer = 0
    write_opcodes = [1, 2, 3, 7, 8]
    
    # three_param_opcodes = [1, 2, 7, 8]
    # two_param_opcodes = [5, 6]
    # one_param_opcodes = [3, 4]
    
    while (instr_pointer < len(intcode_program)):
        if len(intcode_program) == instr_pointer + 1:
            print("we're at the last element of the intcode program...")


        # instr may be 0 - 5 digits
        instr = str(intcode_program[instr_pointer]).zfill(5)
        
        # Each argument has a mode specified by digits
        # TODO: Will there be more args?
        opcode = int(instr[-2:])
        
        if opcode == 99:
            print("we hit a 99!!! abort!!")
            break
        
        args = intcode_program[instr_pointer+1 : instr_pointer+4]
        modes = [int(x) for x in instr[:-2][::-1]] # reverse list so indexes align with args

        if opcode == 1:
            write_val = add(get_arg_value(args[0], modes[0], intcode_program), get_arg_value(args[1], modes[1], intcode_program))
            write_loc = args[2]
            instr_pointer += 4

        elif opcode == 2:
            write_val = mult(get_arg_value(args[0], modes[0], intcode_program), get_arg_value(args[1], modes[1], intcode_program))
            write_loc = args[2]
            instr_pointer += 4

        elif opcode == 3:
            write_val = input_vals.pop()
            write_loc = args[0]
            instr_pointer += 2

        elif opcode == 4:
            output = output_value(get_arg_value(args[0], modes[0], intcode_program))
            instr_pointer += 2

        elif opcode == 5:
            jump = jump_if_true(get_arg_value(args[0], modes[0], intcode_program))
            
            if jump:
                instr_pointer = get_arg_value(args[1], modes[1], intcode_program)
            else:
                instr_pointer += 3 

        elif opcode == 6:
            jump = jump_if_false(get_arg_value(args[0], modes[0], intcode_program))
            
            if jump:
                instr_pointer = get_arg_value(args[1], modes[1], intcode_program)
            else:
                instr_pointer += 3 
        
        elif opcode == 7:
            write_val = less_than(get_arg_value(args[0], modes[0], intcode_program), get_arg_value(args[1], modes[1], intcode_program))
            write_loc = args[2]
            instr_pointer += 4

        
        elif opcode == 8:
            write_val = equals(get_arg_value(args[0], modes[0], intcode_program), get_arg_value(args[1], modes[1], intcode_program))
            write_loc = args[2]
            instr_pointer += 4

        else:
            print("Got an opcode we didn't recognize!!")
            break

        # Only write for certain opcodes
        if opcode in write_opcodes:
            intcode_program[write_loc] = write_val
           
    return output, intcode_program