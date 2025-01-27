from math import gcd


def subtract_fractions(a, b, c, d):
    if b == 0 or d == 0:
        raise ValueError("Denominator cannot be zero.")

    numerator = a * d - c * b
    denominator = b * d
    common_divisor = gcd(abs(numerator), abs(denominator))

    return numerator // common_divisor, denominator // common_divisor


a, b, c, d = 1, 2, 1, 4

try:
    result = subtract_fractions(a, b, c, d)
    print(f"Result of subtraction: {a}/{b} - {c}/{d} = {result[0]}/{result[1]}")
except ValueError as e:
    print(e)


def print_divisors(num):
    if num <= 0:
        print("Error: Input number should be a positive integer.")
        return None
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    print(*divisors)
