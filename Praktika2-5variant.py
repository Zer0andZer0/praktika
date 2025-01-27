import math as m


def calculate_s(x, y, z):
    try:
        if y <= 0:
            return None

        y_pow = y ** (-m.sqrt(abs(x)))

        log_term = m.log(y_pow)

        first_term = log_term * (x - y / 2)

        arctan_z = m.atan(z)

        second_term = m.sin(arctan_z) ** 2

        s = first_term + second_term

        return s


    except ValueError:
        print("Math Error: Please check your input values.")
        return None
