# Script for formatting a list of equations to an arithmetic format string
# Replit link: https://replit.com/@dylanprole/boilerplate-arithmetic-formatter

def custom_eval(split_equation):
    # Addition
    if split_equation[1] == '+':
        return str(int(split_equation[0]) + int(split_equation[2]))
    # Subtraction
    elif split_equation[1] == '-':
        return str(int(split_equation[0]) - int(split_equation[2]))
    else:
        return None

def arithmetic_arranger(problems=["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], include_answer=False):
    # Check to see if there are too many problems
    if len(problems) > 5:
        return 'Error: Too many problems.'

    #Create dictionary object to store all information
    problems_list = list()

    # Loop through the problems and store each problem in the problems
    # dictionary
    for i in range(len(problems)):
        # Use string split to seperate the problem
        problem_split = problems[i].split()

        # Check to see if each character in the digits are numerical only
        for c in problem_split[0] + problem_split[2]:
            if c not in ['1','2','3','4','5','6','7','8','9','0']:
                return 'Error: Numbers must only contain digits.'
        
        # Check to see if the arithmetic operator is valid
        if problem_split[1] not in ['+','-']:
            return "Error: Operator must be '+' or '-'."

        # Add each attribute into the problems dictionary
        problems_list.append({
            # Set original problem as key
            problems[i]:{
            # First number
            'number_1': problem_split[0],
            # Second number
            'number_2': problem_split[2],
            # '+' or '-' sign
            'arithmetic_sign': problem_split[1],
            # the length of the largest digit in the problem
            'max_digit_len': max([len(number) for number in problem_split]),
            # Custom function for calculatig the answer to the problem
            'answer': custom_eval(problem_split)
            }
        })

        # Check to see if the maximum digit length is 4 or less
        if problems_list[i][problems[i]]['max_digit_len'] > 4:
            # Remove if too large
            problems_list.pop(i)
            return 'Error: Numbers cannot be more than four digits.'

    arranged_problems = ''

    # Create a list for each line to print
    lines = ['number_1', 'number_2', 'dash']

    # If answers are required, append it as a line in the list
    if include_answer == True:
        lines.append('answer')

    # Loop through each line
    for line in lines:
        # Nested loop over each problem
        for i in range(len(problems_list)):
            # Print out lines for the first integer
            if line == 'number_1':
                arranged_problems += str(' '*(problems_list[i][problems[i]]['max_digit_len'] -
                                        len(problems_list[i][problems[i]][line]) + 2) +
                                        problems_list[i][problems[i]][line])
                if i != len(problems_list) - 1:
                    arranged_problems += '    '
                
            # Print out lines for the second integer
            elif line == 'number_2':
                arranged_problems += str(problems_list[i][problems[i]]['arithmetic_sign'] +
                                        ' '*(problems_list[i][problems[i]]['max_digit_len'] -
                                            len(problems_list[i][problems[i]][line]) + 1) +
                                            problems_list[i][problems[i]][line])
                if i != len(problems_list) - 1:
                    arranged_problems += '    '
                
            # Print out line for the dashes
            elif line == 'dash':
                arranged_problems += str('-'*(problems_list[i][problems[i]]['max_digit_len'] + 2))
                if i != len(problems_list) - 1:
                    arranged_problems += '    '
                
            # Print out line for the answers if included
            elif line == 'answer':
                arranged_problems += str(' '*(problems_list[i][problems[i]]['max_digit_len'] -
                                            len(problems_list[i][problems[i]][line]) + 2) +
                                            problems_list[i][problems[i]][line])
                if i != len(problems_list) - 1:
                    arranged_problems += '    '
                
        # Print new line
        if line != lines[-1]:
            arranged_problems += str('\n')

    return arranged_problems

print(arithmetic_arranger())



