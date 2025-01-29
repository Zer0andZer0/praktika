def find_max_digit():
    numbers = input("Enter natural numbers ending in zero: ")
    max_digit = -1

    for char in numbers:
        if char.isdigit():
            digit = int(char)
            if digit > max_digit:
                max_digit = digit

    return max_digit


max_digit = find_max_digit()
print("The largest number:", max_digit)
