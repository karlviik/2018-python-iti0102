"""Do wat."""
FIRST_LIST = [0, 2, 4, 6, 8, 11, 12, 14, 16, 18]
FIRST_COUNTER = 0


def first(n: int):
    """Do wat."""
    global FIRST_COUNTER
    FIRST_COUNTER += 1
    return FIRST_LIST[FIRST_COUNTER - 1]


def last(n: int):
    pass
