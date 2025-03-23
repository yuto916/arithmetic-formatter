def arithmetic_arranger(problems, show_answers=False):
    # Constants
    MAX_NUM_OF_PROBLEMS = 5
    MAX_NUM_OF_DIGITS = 4
    OPERATORS_SUPPORTED = ["+", "-"]
    
    # Variables
    list_of_operand1 = []
    list_of_operand2 = []
    list_of_problem_operators = []
    list_of_num_of_digits = []

    # Error Messages
    TOO_MANY_PROBLEMS = f"ERROR: Too many problems. You can add maximum of {MAX_NUM_OF_PROBLEMS} problems."
    INVALID_OPERATOR = "ERROR: Operator must be '+' or '-'."
    NON_NUMERIC_OPERAND = "ERROR: Numbers must only contain digits."
    EXCEEDING_DIGIT_LIMIT = f"ERROR: Numbers cannot be more than {MAX_NUM_OF_DIGITS} digits."
    
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
        if operator != "+" and operator != "-":
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
   
    
    




   
 


print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49", "45 + 43"]))

