def find_smallest(num1, num2, num3):
    smallest = num1
    if num2 < smallest:
        smallest = num2
    if num3 < smallest:
        smallest = num3
    print(f"The smallest number is: {smallest}")
