"""Do wat."""
FIRST_LIST = [0, 2, 4, 6, 8, 11, 12, 14, 16, 18]

first_counter = 0


def first(n: int):
    """First wat."""
    global first_counter
    first_counter += 1
    return FIRST_LIST[first_counter - 1]


def last_neg(n):
    """Negative wat."""
    if n > -15:
        return 0
    if n > -625:
        pass
    if n > -1624:
        pass
    if n > -7020:
        pass


def last_pos(n):
    """Positive wat."""
    if n < 103:
        pass
    elif n < 999:
        pass
    elif n < 1012:
        pass
    elif n < 2003:
        pass
    elif n < 7982:
        pass
    else:
        pass


def last(n: int):
    """Last wat."""
    if n >= -3:
        return last_pos(n)
    else:
        return last_neg(n)
