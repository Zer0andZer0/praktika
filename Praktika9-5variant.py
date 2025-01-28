def print_sorted_matrix(matrix):  # Task 1
    for row in sorted(matrix, key=lambda r: sorted(r)):
        print(sorted(row))


matrix = [
    [3, 1, 4, 2],
    [6, 8, 5, 7],
    [9, 10, 12, 11]
]

print("\nOriginal Matrix:")
print(matrix)

print("\nMatrix with rows sorted:")
print_sorted_matrix(matrix)


def replace_min_elements(matrix):  # Task 2
    new_matrix = []
    for row in matrix:
        min_val = min(row)
        min_index = row.index(min_val)
        new_row = row[:]
        new_row[min_index] = 0 if min_val % 2 == 0 else 1
        new_matrix.append(new_row)
    return new_matrix


def print_matrix(matrix):
    for row in matrix:
        print(row)


# Example
matrix_with_real_numbers = [
    [3.2, 2.0, 4.1, 2.7],
    [6.8, 8.9, 5.3, 7.1],
    [8.0, 10.4, 12.6, 11.5]
]

modified_matrix = replace_min_elements(matrix_with_real_numbers)

print("Original Matrix:")
print_matrix(matrix_with_real_numbers)

print("\nModified Matrix:")
print_matrix(modified_matrix)
