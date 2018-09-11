"""Circle info."""
import math


def find_circle_info(d, x, y):
    """Function which finds perimeter, area and placement of the point."""
    r = d / 2
    r_point = math.sqrt(x ** 2 + y ** 2)
    if r_point < r:
        place = "inside"
    elif r_point == r:
        place = "perimeter"
    elif r_point > r:
        place = "outside"
    perimeter = 2 * math.pi * r
    area = math.pi * r ** 2
    print(f"Circle with perimeter of {perimeter} units and area of {area} units has point ({x}, {y}) on its {place}")


if __name__ == "__main__":  # <- This line is needed for automatic testing
    find_circle_info(10, 9, 8)
