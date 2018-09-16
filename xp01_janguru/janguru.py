"""Calculates the Jangurus' meeting point."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2):
    """Find the meeting point of the 2 Jangurus by using mathematic formula based on linear functions."""
    if pos1 == pos2 and jump_distance1 == jump_distance2 or pos1 == jump_distance2 and pos2 == jump_distance1 or pos1 + jump_distance1 == pos2 + jump_distance2:  # basic if-checks for cases where meeting happens at time == 0
        return int(pos1 + jump_distance1)
    divider = (jump_distance1 * sleep2 - jump_distance2 * sleep1)  # variable for cases where divider == 0
    if divider == 0:  # changes variable to 1 to be able to get correct answer in these cases
        divider = 1
    t1 = (sleep1 * sleep2 * (pos2 - pos1 - jump_distance1)) / divider  # meeting point for 2 linear functions
    t2 = (sleep1 * sleep2 * (pos2 + jump_distance2 - pos1)) / divider  # other point
    if t1 < 0:  # these are for cases where point is negative
        t1 = 0
    if t2 < 0:
        t2 = 0
    if t2 < t1:  # orders them so that t1 is lower than t2
        t1, t2 = t2, t1
    current_time1 = t1 - t1 % sleep1  # gets lowest time in that window
    current_time2 = t1 - t1 % sleep2
    while current_time1 <= t2 or current_time2 <= t2:  # until either of the times is still in window
        if current_time1 < current_time2:
            tempmeet = current_time1 / sleep1 * jump_distance1 + jump_distance1 + pos1  # gets potential meet position
            if (current_time1 - current_time1 % sleep2)/sleep2 * jump_distance2 + jump_distance2 + pos2 == tempmeet:  # checks if it's the meet position
                return int(tempmeet)  # if it is, return it
            current_time1 += sleep1  # advances time by 1 sleep cycle
        else:  # same concept but for other time
            tempmeet = current_time2 / sleep2 * jump_distance2 + jump_distance2 + pos2
            if (current_time2 - current_time2 % sleep1) / sleep1 * jump_distance1 + jump_distance1 + pos1 == tempmeet:
                return int(tempmeet)
            current_time2 += sleep2
    return -1
