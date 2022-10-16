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

#######################
# Program
#######################

def process_program(intcode_program, input_vals = []):
    # print(intcode_program)
    
    output = -1
    instr_pointer = 0
    write_opcodes = [1, 2, 3, 7, 8]
    
    three_param_opcodes = [1, 2, 7, 8]
    two_param_opcodes = [5, 6]
    one_param_opcodes = [3, 4]
    
    # opcode - either 1, 2, 3, or 99
    # TODO: Do we need to check if we reach the end of the list?
    while (instr_pointer < len(intcode_program)):

        # instr may be 0 - 5 digits
        instr = str(intcode_program[instr_pointer]).zfill(5)
        
        # Each argument has a mode specified by digits
        # TODO: Will there be more args?
        opcode = int(instr[-2:])
        # print(opcode)
        
        if opcode == 99:
            break
        
        args = intcode_program[instr_pointer+1 : instr_pointer+4]
        # print(args)
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
            write_val == input_vals.pop()
            # write_loc = 
            instr_pointer += 2

        elif opcode == 4:
            output = output_value(get_arg_value(args[0], modes[0], intcode_program))
            instr_pointer += 2
            # if arg1_mode == Mode.IMMEDIATE:
            #     output = arg1
            # elif arg1_mode == Mode.POSITION:
            #     output = intcode_program[arg1]            
            
        # here is for all our 3-param opcodes
        '''
        if opcode in three_param_opcodes:   
            
            # Comparison opcodes
            if opcode in [7, 8]:
                
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
                if arg1_mode == Mode.IMMEDIATE:
                    output = arg1
                elif arg1_mode == Mode.POSITION:
                    output = intcode_program[arg1]

            instr_pointer += 2
            
        # Here is for all our 2-param opcodes
        elif opcode in two_param_opcodes:
            
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
        '''

        # Only write for certain opcodes
        if opcode in write_opcodes:
            intcode_program[write_loc] = write_val
           
    return output, intcode_program