#!/usr/bin/env python3
"""
Multiplication Table Generator
"""

# Prompt user for a number
number = int(input("Enter a number to see its multiplication table: "))

# Generate and print multiplication table using for loop
for i in range(1, 11):
    print(f"{number} * {i} = {number * i}")