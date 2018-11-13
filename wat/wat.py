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
    if -12000 <= n <= -7020:
        return int(-1000 + abs(12000 + n) / 3)
    if -7019 <= n <= -1624:
        pass  # aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
    if -1623 <= n <= -625:
        return -1345 + 2 * abs(1623 + n)
    if -624 <= n <= -15:
        return -11355 + 19 * abs(624 + n)
    if -14 <= n <= -4:
        return 0


def last_pos(n):
    """Positive wat."""
    if -3 <= n <= 102:
        return 2 * (n + 3)
    if 103 <= n <= 998:
        return int(-616 + (n - 103) * 1.5 - (int(n / 138)) * 137)
    if 999 <= n <= 1011:
        return chr((n - 999) * 2 + 98)
    if 1012 <= n <= 2002:
        return 33 + int((n - 1096) / 84)  # aaaaaaaaaaaaaaaaaaaaaaaaaaa
    if 2003 <= n <= 7981:
        return n - int(n / 1337) * 1337
    if 7982 <= n <= 12000:
        n = str(n)
        nsum = 0
        for num in n:
            nsum += int(num)
        return nsum + 1


def last(n: int):
    """Last wat."""
    if n < -3:
        return last_neg(n)
    else:
        return last_pos(n)

print(last(-9350))