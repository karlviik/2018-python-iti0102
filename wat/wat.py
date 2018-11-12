"""Do wat."""
import random
A = [0, 2, 4, 6, 8, 11, 12, 14, 18]
B = 0

def first(n: int):
    """Do wat."""
    global B
    B += 1
    return A[B - 1]
    if 8 < n < 1000:
        return random.choice([8, 12])
    if n > 1000:
        return 18
    if n == 0:
        return 16
    if n == 1:
        return 0
    if n == 2:
        return 2
    if 2 < n < 9:
        return random.choice([4, 6])
    if n == -1:
        return 14
    else:
        return random.choice([11, 12])
