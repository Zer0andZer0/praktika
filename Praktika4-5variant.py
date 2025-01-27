def sum_of_cubes(n):
    total_sum = 0
    for i in range(1, n + 1):
        total_sum += i ** 3
    return total_sum


n1 = 5
result1 = sum_of_cubes(n1)
print(f"The sum of cubes from 1 to {n1} is: {result1}")
