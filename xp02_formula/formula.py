import re
import math

regex_a = "(((\\-\s)|(?<=\\+\s))?\d*)x2([^0-9]|$)"
regex_b = "(((-\s)|(?<=\\+\s))?\d*)x([^02-9]|$)" #([^0-9]|$)"
regex_c = "(?<![x(x2)(x1)])(((-\s)|(?<=\\+\s))?\d+((?!(x|[0-9]))|$))"


def sum_of_multipliers(side, regex):
    intsum = 0
    for match in re.finditer(regex, side):
        number = match.group(1)
        print(number)
        if number == "":
            number = "1"
        elif number == "- ":
            number = "- 1"
        if number.find("-") == -1:
            intsum += int(number)
        else:
            intsum -= int(number[2:])
    return intsum


def get_multiplier_sums(equation):
    equation = equation.split("=")
    a = 0
    b = 0
    c = 0
    forcount = 1
    for side in equation:
        if forcount == 2:
            forcount = -1
        a += sum_of_multipliers(side, regex_a) * forcount
        b += sum_of_multipliers(side, regex_b) * forcount
        c += sum_of_multipliers(side, regex_c) * forcount
        forcount += 1
    return a, b, c


def add_space(numb, plusadd):
    if numb > 0 and plusadd:
        return "+ " + str(numb)
    if numb > 0:
        return str(numb)
    if numb < 0:
        return "- " + str(abs(numb))
    return str(numb)


def create_normeq(a, b, c):
    normeq = ""
    started = 0
    if a != 0:
        if a == 1:
            normeq += "x2 "
        else:
            normeq += add_space(a, 0) + "x2 "
        started = 1
    if b != 0:
        if b == 1 and started:
            normeq += "+ x "
        elif b == 1:
            normeq += "x "
        elif b == -1:
            normeq += "- x "
        else:
            normeq += add_space(b, started) + "x "
        started = 1
    if c != 0:
        normeq += add_space(c, started) + " "
    if normeq == "":
        normeq += "0 "
    return normeq + "= 0"


def normalize_equation(equation):
    a, b, c = get_multiplier_sums(equation)
    if a < 0:
        a = a * -1
        b = b * -1
        c = c * -1
    elif a == 0 and b < 0:
        b = b * -1
        c = c * -1
    elif a == b == 0 and c < 0:
        c = c * -1
    return create_normeq(a, b, c)


def solve_equation(equation):
    a, b, c = get_multiplier_sums(equation)
    if a == b == c == 0:
        return None
    if a == 0:
        return "x = " + str(round(- c / b, 2))
    else:
        d = b ** 2 - 4 * a * c
        if d < 0:
            return None
        if d == 0:
            return "x = " + str(round((- b + math.sqrt(d)) / (2 * a), 2))
        x1 = (- b + math.sqrt(d)) / (2 * a)
        x2 = (- b - math.sqrt(d)) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        return "x1 = " + str(round(x1, 2)) + ", x2 = " + str(round(x2, 2))


if __name__ == '__main__':

    f = "x2 - 4x + 1x2"
    #print(solve_equation("2x2 + 2 = 0"))
    print(normalize_equation("- 1x - 2x = 0"))
    #print(normalize_equation(f))
    #print_regex_results(regex_a, f)  # 3
    #print_regex_results(regex_b, f)  # - 4
    #print_regex_results(regex_c, f)  # 1

    #f2 = "3x2 + 4x + 5 - 2x2 - 7x + 4"

    #print("x2")
    #print_regex_results(regex_a, f2)  # 3, - 2
    #print("x")
    #print_regex_results(regex_b, f2)  # 4, - 7
    #print("c")
    #print_regex_results(regex_c, f2)  # 5, 4


    #f = "1 - x2 + 48587x"
    #print_regex_results(regex_b, f)

    print("end")
