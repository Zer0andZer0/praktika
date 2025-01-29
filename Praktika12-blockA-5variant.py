def print_digits_reverse(n):
    if n == 0:
        return
    digit = n % 10
    print(digit, end=" ")
    print_digits_reverse(n // 10)


n = int(input())
print_digits_reverse(n)

