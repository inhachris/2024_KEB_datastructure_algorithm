# Assignment 2.2

def print_poly(x_):
    poly_str = "P(x) = "

    for i in range(len(x_[0])):
        term = x_[0][i]
        coef = x[1][i]

        if (coef >= 0):
            poly_str += "+"
        poly_str += str(coef) + "x^" + str(term) + " "

    return poly_str


def calc_poly(x_val, x_):
    ret_value = 0

    for i in range(len(x_[0])):
        term = x_[0][i]
        coef = x_[1][i]
        ret_value += coef * x_value ** term

    return ret_value

x = [[300, 20, 0],
     [7, -4, 5]]

if __name__ == "__main__":
    p_str = print_poly(x)
    print(p_str)

    x_value = int(input("X 값-->"))

    px_value = calc_poly(x_value, x)
    print(px_value)
