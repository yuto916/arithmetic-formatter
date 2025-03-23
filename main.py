def arithmetic_arranger(problems, show_answers=False):
    # Constants
    MAX_NUM_OF_PROBLEMS = 5
    MAX_NUM_OF_DIGITS = 4
    SUPPORTED_OPERATORS = ["+", "-"]
    NUM_OF_SPACES_TOP_EXCL_OPERAND_SPACE = 2
    NUM_OF_SPACES_BOTTOM_EXCL_OPERAND_SPACE = 1
    NUM_OF_SPACES_BETWEEN_PROBLEMS = 4
    SEPARATING_SYMBOL = "-"
    

    # Variables
    num_of_problems = 0
    list_of_operand1 = []
    list_of_operand2 = []
    list_of_problem_operators = []
    list_of_highest_num_of_digits = []
    formatted_string_top = ""
    formatted_string_bottom = ""
    formatted_string_answer = ""
    formatted_string_separator = ""


    # Error Messages
    TOO_MANY_PROBLEMS = f"ERROR: Too many problems. You can add maximum of {MAX_NUM_OF_PROBLEMS} problems."
    INVALID_OPERATOR = "ERROR: Operator must be '+' or '-'."
    NON_NUMERIC_OPERAND = "ERROR: Numbers must only contain digits."
    EXCEEDING_DIGIT_LIMIT = f"ERROR: Numbers cannot be more than {MAX_NUM_OF_DIGITS} digits."
    

    # Determine # of problems
    num_of_problems = len(problems)
    # For each problem in the list of problems:
    for problem in problems:
        # Separate the components of each problem (e.g. 1 + 1 -> ['1', '+', '1'])
        components = problem.split(" ")
        # Assign the problem's operands and operator to the appropriate variable
        list_of_operand1.append(components[0])
        list_of_operand2.append(components[2])
        list_of_problem_operators.append(components[1])


    # ------------------------- Validation -------------------------
    # Input Validation: # of problems
    if len(problems) > MAX_NUM_OF_PROBLEMS:
        return TOO_MANY_PROBLEMS
    
    # Input Validation: operator
    for operator in list_of_problem_operators:
        if operator not in SUPPORTED_OPERATORS:
            return INVALID_OPERATOR
        
    # Input Validation: non-numeric operand & exceeding number of digits
    for operand in list_of_operand1:
        if not operand.isnumeric():
            return NON_NUMERIC_OPERAND
        elif len(operand) > MAX_NUM_OF_DIGITS:
            return EXCEEDING_DIGIT_LIMIT
    for operand in list_of_operand2:
        if not operand.isnumeric():
            return NON_NUMERIC_OPERAND
        elif len(operand) > MAX_NUM_OF_DIGITS:
            return EXCEEDING_DIGIT_LIMIT
    # -------------------------------------------------------------

   
    for i in range(num_of_problems):
        # Determine the length of larger operand in each problem
        length_of_bigger_operand = (max([len(list_of_operand1[i]), len(list_of_operand2[i])]))
        # Append the length
        list_of_highest_num_of_digits.append(length_of_bigger_operand)
        # Determine how many spaces are needed for formatting from the left
        num_of_spaces_top = (list_of_highest_num_of_digits[i] - len(list_of_operand1[i])) + NUM_OF_SPACES_TOP_EXCL_OPERAND_SPACE
        num_of_spaces_bottom = (list_of_highest_num_of_digits[i] - len(list_of_operand2[i])) + NUM_OF_SPACES_BOTTOM_EXCL_OPERAND_SPACE
        # Format each line
        formatted_string_top += (f"{" " * num_of_spaces_top}{list_of_operand1[i]}{" " * NUM_OF_SPACES_BETWEEN_PROBLEMS}")
        formatted_string_bottom += (f"{list_of_problem_operators[i]}{" " * num_of_spaces_bottom}{list_of_operand2[i]}{" " * NUM_OF_SPACES_BETWEEN_PROBLEMS}")
        formatted_string_separator += (f"{SEPARATING_SYMBOL * (list_of_highest_num_of_digits[i] + NUM_OF_SPACES_TOP_EXCL_OPERAND_SPACE)}{" " * (NUM_OF_SPACES_BETWEEN_PROBLEMS)}")


    # Return the formatted problems
    return(f"{formatted_string_top}\n{formatted_string_bottom}\n{formatted_string_separator}")

  
    


print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49", "45 + 43"]))

