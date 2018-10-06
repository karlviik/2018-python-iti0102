"""Normalize and solve linear and square functions."""
import re
import math

# regex_a = "(((\\-\s)|(?<=\\+\s))?\d*)x2([^0-9]|$)"
# regex_b = "(((-\s)|(?<=\\+\s))?\d*)x([^02-9]|$)(?![0-9])"
# regex_c = "(?<![x(x2)(x1)])(((-\s)|(?<=\\+\s))?\d+((?!(x|[0-9]))|$))"

regex_a = "(((-\s)|(?<=+\s))?\d*)x2([^0-9]|$)"
regex_b = "(((-\s)|(?<=+\s))?\d*)x([^02-9]|$)(?![0-9])"
regex_c = "(?<![x(x2)(x1)])(((-\s)|(?<=+\s))?\d+((?!(x|[0-9]))|$))"


def multiplier_sum(side, regex):
    """
    Get the sum of one type of multiplier in one side of equation.

    :param side: one side of equation
    :param regex: type of regex to use
    :return: sum of multiplier
    """
    mult_sum = 0
    for match in re.finditer(regex, side):
        number = match.group(1)
        if number == "":
            number = "1"
        elif number == "- ":
            number = "- 1"
        if number.find("-") == -1:
            mult_sum += int(number)
        else:
            mult_sum -= int(number[2:])  # deals with negative numbers
    return mult_sum


def get_multiplier_sums(equation):
    """
    Get sum of all multipliers in whole equation.

    :param equation: whole equation in form of string
    :return: a, b and c, respective multipliers
    """
    equation = equation.split("=")
    a = 0
    b = 0
    c = 0
    forcount = 1  # used for adding up both sides' multipliers correctly
    for side in equation:
        if forcount == 2:
            forcount = -1
        a += multiplier_sum(side, regex_a) * forcount
        b += multiplier_sum(side, regex_b) * forcount
        c += multiplier_sum(side, regex_c) * forcount
        forcount += 1
    return a, b, c


def number_to_string(numb, plusadd):
    """
    Add space and plus or minus to number and return as string.

    :param numb: number as int
    :param plusadd: if to add plus and space or not
    :return: number as string with +/- and space
    """
    if numb > 0 and plusadd:
        return "+ " + str(numb)
    if numb > 0:
        return str(numb)
    if numb < 0:
        return "- " + str(abs(numb))
    return str(numb)


def normalize_equation(equation):
    """
    Create normalized equation from fed string.

    :param equation: fed equation as string
    :return: normalized equation as string
    """
    a, b, c = get_multiplier_sums(equation)
    if a < 0 or a == 0 and b < 0 or a == b == 0 and c < 0:
        a = a * -1
        b = b * -1
        c = c * -1
    normeq = ""
    started = 0  # if the equation has been started
    if a != 0:
        if a == 1:
            normeq += "x2 "
        else:
            normeq += number_to_string(a, 0) + "x2 "
        started = 1
    if b != 0:
        if b == 1 and started:
            normeq += "+ x "
        elif b == 1:
            normeq += "x "
        elif b == -1:
            normeq += "- x "
        else:
            normeq += number_to_string(b, started) + "x "
        started = 1
    if c != 0:
        normeq += number_to_string(c, started) + " "
    return normeq + "= 0"


def solve_equation(equation):
    """
    Solve equation and return answers.

    :param equation: equation as string
    :return: answers as string
    """
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
