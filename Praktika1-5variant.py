def calculate_expression(n_str):
    try:
        n = float(n_str)
        result = n + n ** 2 + n ** 3 + n ** 4 + n ** 5
        return result
    except ValueError:
        print("Invalid input: Please provide a valid number string.")
        return None


number_string = "2"
result = calculate_expression(number_string)
if result is not None:
    print(f"Result of the expression for n={number_string} is: {result}")