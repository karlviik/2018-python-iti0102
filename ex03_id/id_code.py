"""Check if given ID code is valid."""

import math


def check_your_id(id_code: str):
    """
    Check if given ID code is valid and return the result.

    :param id_code: str
    :return: boolean
    """
    if len(id_code) == 11 and id_code.isdigit():
        if check_gender_number(int(id_code[0])) == 1:
            if check_day_number(int(id_code[1:3]), int(id_code[3:5]), int(id_code[5:7])) == 1:
                if check_born_order(int(id_code[7:10])) == 1:
                    if check_control_number(id_code) == 1:
                        return True
    return False


def check_gender_number(gender_number: int):
    """
    Check if given value is correct for gender number in ID code.

    :param gender_number: int
    :return: boolean
    """
    if 1 <= gender_number <= 6:
        return True
    return False


def check_year_number_two_digits(year_number: int):
    """
    Check if given value is correct for year number in ID code.

    :param year_number: int
    :return: boolean
    """
    if 0 <= year_number <= 99:
        return True
    return False


def check_month_number(month_number: int):
    """
    Check if given value is correct for month number in ID code.

    :param month_number: int
    :return: boolean
    """
    if 1 <= month_number <= 12:
        return True
    return False


def check_day_number(year_number: int, month_number: int, day_number: int):
    """
    Check if given value is correct for day number in ID code.

    Also, consider leap year and which month has 30 or 31 days.

    :param year_number: int
    :param month_number: int
    :param day_number: int
    :return: boolean
    """
    if check_month_number(month_number) == 1 and check_year_number_two_digits(year_number) == 1:
        if (month_number <= 7 and month_number % 2 == 1 or month_number > 7 and month_number % 2 == 0) and 0 < day_number <= 31:
            return True
        if (3 < month_number < 7 and month_number % 2 == 0 or month_number > 7 and month_number % 2 == 1) and 0 < day_number <= 30:
            return True
        if month_number == 2 and (check_leap_year(year_number) == 1 and day_number == 28 or check_leap_year(year_number) == 0 and 0 < day_number <= 29):
            return True
    return False


def check_leap_year(year_number: int):
    """
    Check if given year is a leap year.

    :param year_number: int
    :return: boolean
    """
    if year_number % 4 != 0 or year_number % 400 != 0 and year_number % 100 == 0:
        return False
    return True


def check_born_order(born_order: int):
    """
    Check if given value is correct for born order number in ID code.

    :param born_order: int
    :return: boolean
    """
    if 0 <= born_order <= 999:
        return True
    return False


def check_control_number(id_code: str):
    """
    Check if given value is correct for control number in ID code.

    Use algorithm made for creating this number.

    :param id_code: string
    :return: boolean
    """
    control = int(id_code[10])
    loop_counter = 0
    multiplier = 1
    while loop_counter < 2:
        number_counter = 0
        checksum = 0
        while number_counter < 10:
            checksum = checksum + int(id_code[number_counter]) * multiplier
            number_counter += 1
            multiplier = multiplier % 9 + 1
        if checksum % 11 < 10:
            if checksum % 11 == control:
                return True
            return False
        loop_counter += 1
        multiplier += 1
    if checksum % 11 == 10 and control == 0:
        return True
    return False


def get_data_from_id(id_code: str):
    """
    Get possible information about the person.

    Use given ID code and return a short message.
    Follow the template - This is a (gender) born on (DD.MM.YYYY).
    :param id_code: str
    :return: str
    """
    if check_your_id(id_code) == 0:
        return "Given invalid ID code!"
    return "This is a " + get_gender(int(id_code[0])) + " born on " + str(id_code[5:7]) + "." + str(id_code[3:5]) + "." + str(get_full_year(int(id_code[0]), int(id_code[1:3])))


def get_gender(gender_number: int):
    """
    Define the gender according to the number from ID code.

    :param gender_number: int
    :return: str
    """
    if gender_number % 2 == 0:
        return "female"
    return "male"


def get_full_year(gender_number: int, year: int):
    """
    Define the 4-digit year when given person was born.

    Person gender and year numbers from ID code must help.
    Given year has only two last digits.

    :param gender_number: int
    :param year: int
    :return: int
    """
    century_add = math.ceil(gender_number / 2)
    return 1700 + 100 * century_add + year


if __name__ == '__main__':
    print("Overall ID check::")
    print(check_your_id("49808270244"))  # -> True
    personal_id = input()  # type your own id in command prompt
    print(check_your_id(personal_id))    # -> True
    print(check_your_id("12345678901"))  # -> False
    print("\nGender number:")
    for i in range(9):
        print(f"{i} {check_gender_number(i)}")
        # 0 -> False
        # 1...6 -> True
        # 7...8 -> False
    print("\nYear number:")
    print(check_year_number_two_digits(100))  # -> False
    print(check_year_number_two_digits(50))   # -> true
    print("\nMonth number:")
    print(check_month_number(2))   # -> True
    print(check_month_number(15))  # -> False
    print("\nDay number:")
    print(check_day_number(5, 12, 25))  # -> True
    print(check_day_number(10, 8, 32))  # -> False
    print(check_leap_year(1804))  # -> True
    print(check_leap_year(1800))  # -> False
    print("\nFebruary check:")
    print(check_day_number(96, 2, 30))  # -> False (February cannot contain more than 29 days in any circumstances)
    print(check_day_number(99, 2, 29))  # -> False (February contains 29 days only during leap year)
    print(check_day_number(8, 2, 29))   # -> True
    print("\nMonth contains 30 or 31 days check:")
    print(check_day_number(22, 4, 31))   # -> False (April contains max 30 days)
    print(check_day_number(18, 10, 31))  # -> True
    print(check_day_number(15, 9, 31))   # -> False (September contains max 30 days)
    print("\nBorn order number:")
    print(check_born_order(0))    # -> False
    print(check_born_order(850))  # -> True
    print("\nControl number:")
    print(check_control_number("49808270244"))  # -> True
    print(check_control_number("60109200187"))  # -> False, it must be 6


if __name__ == '__main__':
    print("\nFull message:")
    print(get_data_from_id("49808270244"))  # -> "This is a female born on 27.08.1998"
    print(get_data_from_id("60109200187"))  # -> "Given invalid ID code!"
    print(get_full_year(1, 28))  # -> 1828
    print(get_full_year(4, 85))  # -> 1985
    print(get_full_year(5, 1))   # -> 2001
    print(get_gender(2))  # -> "female"
    print(get_gender(5))  # -> "male"
