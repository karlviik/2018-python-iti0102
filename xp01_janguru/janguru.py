"""Calculates the Jangurus' meeting point."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Find the meeting point of the 2 Jangurus by using raw math and some loopy loops."""
    y1 = float(pos1)
    j1 = float(jump_distance1)
    p1 = float(sleep1)
    y2 = float(pos2)
    j2 = float(jump_distance2)
    p2 = float(sleep2)

    if y1 > y2:
        y1, y2 = y2, y1
        j1, j2 = j2, j1
        p1, p2 = p2, p1
    if y1 == y2 and j1 == j2 or y1 == j2 and y2 == j1:
        return y1 + j1
    #if ((((y2 - y1) > j1) or (j1 < j2)) and (j1 / p1 < j2 / p2)) or ((y2 - y1) % j1 != 0 and j2 % j1 == 0) or (j1 == j2 and p1 == p2 and y1 != y2):
    #    return -1
    else:
        littletemp = j2 * p1 - j1 * p2
        if littletemp == 0:
            return -1
        largetemp = (j2 * y1 * p1 - j1 * y2 * p2 + j1 * j2 * p1 - j1 * j2 * p2)
        i = 0-p1+1
        j = 0-p2+1
        minmeet = float("inf")
        while i < p1:
            while j < p2:
                if (largetemp + j1 * j2 * (j - i)) % littletemp == 0:
                    tempmeet = ((largetemp + j1 * j2 * (j - i)) / littletemp)
                    if tempmeet % 1 == 0 and tempmeet < minmeet and tempmeet >= 0 and tempmeet > y1 and tempmeet > y2 and (tempmeet - y1) % j1 == 0 and (tempmeet - y2) % j2 == 0:
                        minmeet = tempmeet
                if (largetemp + j1 * j2 * (i - j)) % littletemp == 0:
                    tempmeet = ((largetemp + j1 * j2 * (i - j)) / littletemp)
                    if tempmeet % 1 == 0 and tempmeet < minmeet and tempmeet >= 0 and tempmeet > y1 and tempmeet > y2 and (tempmeet - y1) % j1 == 0 and (tempmeet - y2) % j2 == 0:
                        minmeet = tempmeet
                j += 1
            i += 1
        if minmeet == float("inf"):
            return -1
        else:
            return int(minmeet)

print(meet_me(2, 1, 1, 2, 1, 1))
