"""Simulation."""
from typing import Tuple


def simulate(world_map: list, flight_plan: list) -> list:
    """
    Simulate a flying space ship fighting space pirates.

    :param world_map: A list of strings indicating rows that make up the space map.
                 The space map is always rectangular and the minimum given size is 1x1.
                 Space pirate free zone is indicated by the symbol ('-'), low presence by ('w') and high presence by ('W').
                 The ship position is indicated by the symbol ('X'). There is always one ship on the space map.
                 Asteroid fields are indicated by the symbol ('#').

    :param flight_plan: A list of moves.
                  The moves are abbreviated N - north, E - east, S - south, W - west.
                  Ignore moves that would put the ship out of bounds or crash it into an asteroid field.

    :return: A list of strings indicating rows that make up the space map. Same format as the given wmap.

    Pirates under Shippy's starting position are always eliminated ('-').
    If Shippy fights pirates in high presence area, it first turns into low presence ('w')
     and then from low presence into no presence area ('-').
    """
    maxrow, maxcol = len(world_map) - 1, len(world_map[0]) - 1
    worlddict, crow, ccol = list_to_dictionary_converter(world_map)
    worlddict[crow, ccol] = "-"
    for move in flight_plan:
        if not (crow == 0 and move == "N" or crow == maxrow and move == "S" or ccol == maxcol and move == "E" or ccol == 0 and move == "W"):
            if move == "W" and worlddict[crow, ccol - 1] != "#":
                ccol -= 1
            elif move == "E" and worlddict[crow, ccol + 1] != "#":
                ccol += 1
            elif move == "N" and worlddict[crow - 1, ccol] != "#":
                crow -= 1
            elif move == "S" and worlddict[crow + 1, ccol] != "#":
                crow += 1
        if worlddict[crow, ccol] == "W":
            worlddict[crow, ccol] = "w"
        elif worlddict[crow, ccol] == "w":
            worlddict[crow, ccol] = "-"
    worlddict[crow, ccol] = "X"
    return dictionary_to_list_converter(worlddict, maxcol + 1, maxrow + 1)


def list_to_dictionary_converter(world_map: list) -> Tuple[dict, int, int]:
    """Converts a list to dictionary using coordinates as keys."""
    mapdict = {}
    shiprow, shipcol = 0, 0
    for rowi, row in enumerate(world_map):
        for celli, cell in enumerate(row):
            if cell == "X":
                cell = "-"
                shiprow = rowi
                shipcol = celli
            mapdict[rowi, celli] = cell
    return mapdict, shiprow, shipcol


def dictionary_to_list_converter(space_map: dict, len1: int, len2: int) -> list:
    """Convert dictionary of coordinates to list of strings."""
    rowlist = []
    for rowcount in range(len2):
        temprow = ""
        for columncount in range(len1):
            temprow += space_map[(rowcount, columncount)]
        rowlist.append(temprow)
    return rowlist


if __name__ == '__main__':
    space_list1 = [
        "---",
        "-X-",
        "-W-"
    ]
    flight_plan1 = ["N", "N", "N", "N", "E", "E", "E", "E", "S", "S", "S", "S", "W", "W", "W", "W"]
    print(list_to_dictionary_converter(space_list1))
    print(simulate(space_list1, flight_plan1))
    space_list2 = [
        "WWWW",
        "-wwW",
        "X-#W",
    ]

    flight_plan2 = ["N", "N", "E", "E", "S", "W", "W", "S", "E", "E"]

"""
test_simulate_random_up_to_3x3_cut_low_high: FAILED (22.68 ms)
test_simulate_random_up_to_3x3_cut_low_high_obstacles: FAILED (14.46 ms)
test_simulate_random_up_to_20x20_cut_low_high_obstacles: FAILED (4.578 ms)
test_simulate_random_up_to_5x5_cut_low_high_obstacles_time_limit: FAILED (10.1 ms)
test_list_to_dict_2x2: FAILED (3.858 ms)
test_random_list_to_dict_easy: FAILED (2.273 ms)
test_random_list_to_dict_medium: FAILED (2.588 ms)
test_random_list_to_dict_hard: FAILED (2.276 ms)
"""

   test_simulate_random_up_to_3x3_cut_low_high: FAILED (21.53 ms)

   test_simulate_random_up_to_3x3_cut_low_high_obstacles: FAILED (20.21 ms)

   test_simulate_random_up_to_3x3_cut_low_high_obstacles_a_lot_of_moves: passed (80.82 ms)

   test_simulate_random_up_to_20x20_cut_low_high_obstacles: FAILED (4.793 ms)

   test_simulate_random_up_to_5x5_cut_low_high_obstacles_time_limit: FAILED (2.519 ms)

   test_list_to_dict_1x1_nothing: FAILED (2.089 ms)
            UnboundLocalError: local variable 'shiprow' referenced before assignment


   test_list_to_dict_2x2: FAILED (4.206 ms)
            UnboundLocalError: local variable 'shiprow' referenced before assignment

