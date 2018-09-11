"""Polar and cartesian points converter."""
from math import cos, sin, pi, atan, degrees, radians, sqrt


def convert_polar_to_cartesian(r, phi):
    """
    Convert point from polar coordinates to cartesian coordinates.

    :param r: radius, the distance from pole to point.
    :param phi: polar angle, or azimuth in degrees.
    :return: tuple, of x- and y-coordinate of the point
    """
    x = r * cos(radians(phi))
    y = r * sin(radians(phi))
    return round(x, 2), round(y, 2)


def convert_cartesian_to_polar(x, y):
    """
    Convert point from cartesian coordinates to polar coordinates.

    Radius is equal to the length of vector from pole (0, 0) to the point (x, y).
    Calculated as in the Pythagorean theorem.

    Polar angle is the angle between positive x-axis and the ray from the pole (0, 0) to the point (x, y).
    Calculated using atan2 function, the angle is float (φ) in range −180° < φ ≤ 180°.

    :param x: x-coordinate of given point
    :param y: y-coordinate of given point
    :return: tuple, of polar radius and polar angle in degrees.
    """
    r = sqrt(x ** 2 + y ** 2)
    if x > 0:
        angle = degrees(atan(y / x))
    elif x < 0 and y >= 0:
        angle = degrees(atan(y / x) + pi)
    elif x < 0 and y < 0:
        angle = degrees(atan(y / x) - pi)
    elif x == 0 and y > 0:
        angle = degrees(pi / 2)
    elif x == 0 and y < 0:
        angle = degrees(- pi / 2)
    elif x == 0 and y == 0:
        angle = 0

    return round(r, 2), round(angle, 2)


if __name__ == '__main__':
    print("to polar")
    print(convert_cartesian_to_polar(1, 1))  # (1.41, 45.0)
    print(convert_cartesian_to_polar(0, 0))  # (0.0, 0.0)
    print(convert_cartesian_to_polar(0, 1))  # (1.0, 90.0)
    print(convert_cartesian_to_polar(-3, -4))  # (5.0, -126.87)

    print("\nto cartesian")
    print(convert_polar_to_cartesian(1, 90))  # (0.0, 1.0)
    print(convert_polar_to_cartesian(0, 0))  # (0.0, 0.0)
    print(convert_polar_to_cartesian(2, 60))  # (1.0, 1.73)
    print(convert_polar_to_cartesian(3, -40))  # (2.3, -1.93)
