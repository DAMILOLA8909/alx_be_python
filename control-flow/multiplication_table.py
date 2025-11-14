#!/usr/bin/env python3
"""
Multiplication Table Generator
Generates and prints multiplication table for a given number from 1 to 10.
"""

def generate_multiplication_table():
    # Prompt user for a number
    number = int(input("Enter a number to see its multiplication table: "))
    
    # Generate multiplication table using for loop
    table = []
    for i in range(1, 11):
        product = number * i
        table.append(f"{number} * {i} = {product}")
    
    return table

# Call the function and print the result
table_lines = generate_multiplication_table()
for line in table_lines:
    print(line)