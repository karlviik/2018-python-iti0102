"""Calculates the Jangurus' meeting point."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Find the meeting point of the 2 Jangurus by using raw math and some loopy loops."""
    y1 = float(pos1)
    j1 = float(jump_distance1)
    p1 = float(sleep1)
    y2 = float(pos2)
    j2 = float(jump_distance2)
    p2 = float(sleep2)

    if y1 == y2 and j1 == j2 or y1 == j2 and y2 == j1:
        return int(y1 + j1)
    if (j1 * p2 - j2 * p1) == 0:
        return -1
    t1 = (p1 * p2 * (y2 - y1 - j1)) / (j1 * p2 - j2 * p1)
    t2 = (p1 * p2 * (y1 - y2 - j2)) / (j1 * p2 - j2 * p1)
    if t1 < 0:
        t1 = 0
    if t2 < 0:
        t2 = 0
    if t2 < t1:
        t1, t2 = t2, t1
    print(t1)
    print(t2)
    t11 = t1 - t1 % p1 + p1
    t22 = t1 - t1 % p2 + p2
    print(t11)
    print(t22)
    while t11 <= t2 and t22 <= t2:
        if t11 < t22:
            tempmeet = t11 / p1 * j1 + j1 + y1
            if (t11 - t11 % p2)/p2 * j2 + j2 + y2 == tempmeet:
                return int(tempmeet)
            t11 += p1
        else:
            tempmeet = t22 / p2 * j2 + j2 + y2
            if (t22 - t22 % p1) / p1 * j1 + j1 + y1 == tempmeet:
                return int(tempmeet)
            t22 += p2
    return -1

    pass
    if y1 > y2:
        y1, y2 = y2, y1
        j1, j2 = j2, j1
        p1, p2 = p2, p1
    if y1 == y2 and j1 == j2 or y1 == j2 and y2 == j1:
        return int(y1 + j1)
    if ((((y2 - y1) > j1) or (j1 < j2)) and (j1 / p1 < j2 / p2)) or ((y2 - y1) % j1 != 0 and j2 % j1 == 0) or (j1 == j2 and p1 == p2 and y1 != y2):
        return -1
    aah = p1 * p2 * (y2 + j2 - y1 - j1)
    eeh = p2 * j1 - p1 * j2
    if eeh == 0:
        return -1
    i = 0
    j = 0
    minmeet = float("inf")
    while i < p1:
        while j < p2:
            tempmeet = (aah+p2*j1*i-p1*j2*j)/eeh
            tempmeet = tempmeet/p1 * j1 + j1 + y1
            if tempmeet % 1 == 0 and tempmeet < minmeet and tempmeet >= 0 and tempmeet > y1 and tempmeet > y2 and (tempmeet - y1) % j1 == 0 and (tempmeet - y2) % j2 == 0:
                minmeet = tempmeet
            tempmeet = (aah + p2 * j1 * j - p1 * j2 * i) / eeh
            tempmeet = tempmeet/p1 * j1 + j1 + y1
            if tempmeet % 1 == 0 and tempmeet < minmeet and tempmeet >= 0 and tempmeet > y1 and tempmeet > y2 and ( tempmeet - y1) % j1 == 0 and (tempmeet - y2) % j2 == 0:
                minmeet = tempmeet
            j += 1
        i += 1
    if 1 == 2:
        return int(minmeet)
    else:
        littletemp = j2 * p1 - j1 * p2
        if littletemp == 0:
            return -1
        largetemp = (j2 * y1 * p1 - j1 * y2 * p2 + j1 * j2 * p1 - j1 * j2 * p2)
        i = 0
        j = 0
        #minmeet = float("inf")
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

#print(meet_me(2, 1, 1, 2, 1, 1))

#print(meet_me(1, 2, 3, 4, 5, 5))

#print(meet_me(10, 7, 7, 5, 8, 6))

#print(meet_me(100, 7, 4, 300, 8, 6))

#print(meet_me(1, 7, 1, 15, 5, 1))

#print(meet_me(0, 1, 1, 1, 1, 1))

