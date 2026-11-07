
# CSC 223 Binary Expression Tree Project

## Project Description
This Python program builds a binary expression tree from a postfix expression using a stack.

The program supports addition, subtraction, multiplication, and division. It can display fully parenthesized infix expressions, generate postfix expressions, and recursively evaluate the tree.

## Project Files
- stack.py - Stack implementation reused from the previous project.
- binary_expression_tree.py - Binary expression tree implementation.
- main.py - Driver program that processes sample expressions.
- test_binary_expression_tree.py - Unit tests.

## How to Run the Program
Open the terminal and enter:

python main.py

## How to Run the Tests
Enter:

python -m unittest test_binary_expression_tree.py -v

## Example
Input: 5 3 8 * +

Infix: (5 + (3 * 8))

Postfix: 5 3 8 * +

Result: 29.0

## Error Handling
The program handles invalid expressions, missing or extra operands, unsupported tokens, empty input, and division by zero.
