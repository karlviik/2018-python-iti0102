import pytest
import shortest_way_back
import random
import re


def test_no_movement():
    assert shortest_way_back.shortest_way_back("") == ""


def test_one_movement():
    assert shortest_way_back.shortest_way_back("W") == "E"
    assert shortest_way_back.shortest_way_back("E") == "W"
    assert shortest_way_back.shortest_way_back("S") == "N"
    assert shortest_way_back.shortest_way_back("N") == "S"


def test_back_to_beginning_two_directions():
    assert shortest_way_back.shortest_way_back("WE") == ""
    assert shortest_way_back.shortest_way_back("WEWE") == ""
    assert shortest_way_back.shortest_way_back("WWEE") == ""
    assert shortest_way_back.shortest_way_back("SN") == ""
    assert shortest_way_back.shortest_way_back("SNSN") == ""
    assert shortest_way_back.shortest_way_back("SSNN") == ""


def test_back_to_beginning_four_directions():
    assert shortest_way_back.shortest_way_back("WENS") == ""
    assert shortest_way_back.shortest_way_back("WENSSENW") == ""


def test_three_directions_out_one_direction_in():
    assert shortest_way_back.shortest_way_back("SWEWESEEWEWWS") == "NNN"
    assert shortest_way_back.shortest_way_back("NEWWENWWWNWEEEEEW") == "SSS"
    assert shortest_way_back.shortest_way_back("ENSENSSNNESNNNSSNSS") == "WWW"
    assert shortest_way_back.shortest_way_back("SNSNWWNNNSSSNSNSNSSWNSSNN") == "EEE"


def test_four_directions_out_one_direction_in():
    assert shortest_way_back.shortest_way_back("SENWWNSSWENSWENEWNNWEWSWSEW") == "EEE"
    assert shortest_way_back.shortest_way_back("SENWWENSEWENESWEWENENWEESWSEW") == "WWW"
    assert shortest_way_back.shortest_way_back("SENWWESNSEWWENESWSWEWENWENWESESWSEW") == "NNN"
    assert shortest_way_back.shortest_way_back("SENWNWESNSEWNWENESWSWEWNNENWNENWESENSWSEW") == "SSS"


def test_two_directions():
    assert shortest_way_back.shortest_way_back("WNW") in ["SEE", "ESE", "EES"]
    assert shortest_way_back.shortest_way_back("SSE") in ["NNW", "NWN", "WNN"]
    assert shortest_way_back.shortest_way_back("ENN") in ["SSW", "WSS", "SWS"]
    assert shortest_way_back.shortest_way_back("WWS") in ["NEE", "ENE", "EEN"]


def test_three_directions():
    assert shortest_way_back.shortest_way_back("WNSNNWS") in ["SEE", "ESE", "EES"]
    assert shortest_way_back.shortest_way_back("SSNENES") in ["WWN", "WNW", "NWW"]


def test_four_directions():
    assert shortest_way_back.shortest_way_back("WNSNENWS") in ["SE", "ES"]
    assert shortest_way_back.shortest_way_back("SSEWENSN") in ["NW", "WN"]


def test_long_one_way():
    assert shortest_way_back.shortest_way_back("W" * 100) == "E" * 100
    assert shortest_way_back.shortest_way_back("E" * 100) == "W" * 100
    assert shortest_way_back.shortest_way_back("N" * 100) == "S" * 100
    assert shortest_way_back.shortest_way_back("S" * 100) == "N" * 100


def test_long_two_cancelling_ways():
    assert shortest_way_back.shortest_way_back("W" * 50 + "E" * 50) == ""
    assert shortest_way_back.shortest_way_back("SSNN" * 100) == ""


def test_long_two_almost_cancelling_ways():
    assert shortest_way_back.shortest_way_back("W" * 50 + "E" * 51) == "W"
    assert shortest_way_back.shortest_way_back("W" * 50 + "E" * 49) == "E"
    assert shortest_way_back.shortest_way_back("N" * 50 + "S" * 51) == "N"
    assert shortest_way_back.shortest_way_back("N" * 50 + "S" * 49) == "S"


def test_random():
    def generate_random(length):
        directions = ["W", "E", "N", "S"]
        movement = ""
        for _ in range(length):
            movement += random.choice(directions)
        return movement

    def check(path, multiplier):
        we = len(re.findall("W", path)) - len(re.findall("E", path))
        ns = len(re.findall("N", path)) - len(re.findall("S", path))
        return we * multiplier, ns * multiplier

    for i in range(5):
        movement = generate_random(20 + i)
        assert check(shortest_way_back.shortest_way_back(movement), 1) == check(movement, -1)


"""
test_testing_basic[result_has_only_other1-False]: FAILED (70.9 ms)

   test_testing_basic[result_has_only_other2-False]: passed (392.6 ms)

   test_testing_basic[result_has_only_other3-False]: FAILED (72.6 ms)

   test_testing_basic[result_has_only_other4-False]: passed (451.8 ms)

   test_uses_random: FAILED (363.7 ms)"""





# TODO: add more functions
