# Arithmetic Formatter


## Description
This program formats a set of arithmetic problems into a structured output. It ensures the input follows specific rules and returns meaningful error messages when the formatting is incorrect.


## Formatting Rules
If the problems are formatted correctly, the function arranges them as follows:
- Problems are **right-aligned**.
- The operator is on the same line as the second operand, with **one space** between the operator and the longest operand.
- Each problem is separated by **four spaces**.
- A row of dashes (-) runs beneath each problem.


## Error Handling
The function returns errors in the following cases:
- **Too many problems**: The limit is five. More than five problems return:
    ```
    Error: Too many problems.
    ```

- **Invalid operator**: Only **+** and **-** are allowed. Other operators return:
    ```
    Error: Operator must be '+' or '-'.
    ```

- **Non-numeric input**: Operands must contain only digits. Otherwise, it returns:
    ```
    Error: Numbers must only contain digits.
    ```

- **Exceeding digit limit**: Each operand must be at most four digits. Otherwise, it returns:
    ```
    Error: Numbers cannot be more than four digits.
    ```


## Example Output
Input:
  ```
  arithmetic_arranger(["35 + 730", "3801 - 5", "45 + 87", "123 + 51"])
  ```
Output:
  ```
     35      3801      45      123
  + 730    -    5    + 87    +  51
  -----    ------    ----    -----
  ```
