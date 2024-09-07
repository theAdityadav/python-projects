import pandas as pd
import numpy as nm
#Taking input for the number of rows and columns
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initializing an empty matrix
matrix = []

# Taking input for each row
for i in range(rows):
    # Initializing an empty row
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position [{i}][{j}]: "))
        row.append(element)
    # Adding the row to the matrix
    matrix.append(row)

# Printing the matrix
print("The matrix is:")
for row in matrix:
    print(row)

#Adding a function to calculate the sum of diagonal elements
def calculate_diagonal_sum(matrix):
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    return diagonal_sum
diagonal_sum = calculate_diagonal_sum(matrix)
print(f"Diagonal Sum: {diagonal_sum}")
