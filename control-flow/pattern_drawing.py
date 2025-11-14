#!/usr/bin/env python3

# Prompt user for pattern size
size = int(input("Enter the size of the pattern: "))

# Use while loop for rows
row = 0
while row < size:
    # Use for loop for columns
    for col in range(size):
        print("*", end="")
    # Move to next line
    print()
    row += 1