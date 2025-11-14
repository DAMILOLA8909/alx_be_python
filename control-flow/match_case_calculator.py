#!/usr/bin/env python3
"""
Simple Calculator using Match Case
Performs basic arithmetic operations based on user input.
"""

def calculate():
    # Prompt user for two numbers
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    # Prompt user for operation
    operation = input("Choose the operation (+, -, *, /): ").strip()
    
    # Perform calculation using match case
    match operation:
        case "+":
            return num1 + num2
        case "-":
            return num1 - num2
        case "*":
            return num1 * num2
        case "/":
            if num2 == 0:
                return "Cannot divide by zero."
            else:
                return num1 / num2
        case _:
            return "Invalid operation. Please choose from +, -, *, or /."

# Call the function and print the result
result = calculate()
print(f"The result is {result}" if isinstance(result, (int, float)) else result)