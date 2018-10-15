"""Find the shortest way back in a taxicab geometry."""
import re


def shortest_way_back(path: str) -> str:
    """
    Find the shortest way back in a taxicab geometry.

    :param path: string of moves, where moves are encoded as follows:.
    N - north -  (1, 0)
    S - south -  (-1, 0)
    E - east  -  (0, 1)
    W - west  -  (0, -1)
    (first coordinate indicates steps towards north,
    second coordinate indicates steps towards east)

    :return: the shortest way back encoded the same way as :param path:.
    """
    west_or_east = len(re.findall("W", path)) - len(re.findall("E", path))
    north_or_south = len(re.findall("N", path)) - len(re.findall("S", path))
    if west_or_east > 0:
        we = "E"
    else:
        we = "W"
    if north_or_south > 0:
        ne = "S"
    else:
        ne = "N"
    return we * abs(west_or_east) + ne * abs(north_or_south)
