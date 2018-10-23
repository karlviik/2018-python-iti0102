"""Test pr07 shortest_way_back code."""
import shortest_way_back
import random
import re


def test_no_movement():
    """Test case with no movement."""
    assert shortest_way_back.shortest_way_back("") == ""


def test_one_movement():
    """Test cases with only one movement step."""
    assert shortest_way_back.shortest_way_back("W") == "E"
    assert shortest_way_back.shortest_way_back("E") == "W"
    assert shortest_way_back.shortest_way_back("S") == "N"
    assert shortest_way_back.shortest_way_back("N") == "S"


def test_back_to_beginning_two_directions():
    """Test cases with movement in two directions that cancel out."""
    assert shortest_way_back.shortest_way_back("WE") == ""
    assert shortest_way_back.shortest_way_back("WEWE") == ""
    assert shortest_way_back.shortest_way_back("WWEE") == ""
    assert shortest_way_back.shortest_way_back("SN") == ""
    assert shortest_way_back.shortest_way_back("SNSN") == ""
    assert shortest_way_back.shortest_way_back("SSNN") == ""


def test_back_to_beginning_four_directions():
    """Test cases with movement in 4 directions that all cancel out."""
    assert shortest_way_back.shortest_way_back("WENS") == ""
    assert shortest_way_back.shortest_way_back("WENSSENW") == ""


def test_three_directions_out_one_direction_in():
    """Test cases where movement is in 3 directions but 2 directions cancel out."""
    assert shortest_way_back.shortest_way_back("SWEWESEEWEWWS") == "NNN"
    assert shortest_way_back.shortest_way_back("NEWWENWWWNWEEEEEW") == "SSS"
    assert shortest_way_back.shortest_way_back("ENSENSSNNESNNNSSNSS") == "WWW"
    assert shortest_way_back.shortest_way_back("SNSNWWNNNSSSNSNSNSSWNSSNN") == "EEE"


def test_four_directions_out_one_direction_in():
    """Test cases with movement in 4 directions but shortest way back in one direction."""
    assert shortest_way_back.shortest_way_back("SENWWNSSWENSWENEWNNWEWSWSEW") == "EEE"
    assert shortest_way_back.shortest_way_back("SENWWENSEWENESWEWENENWEESWSEW") == "WWW"
    assert shortest_way_back.shortest_way_back("SENWWESNSEWWENESWSWEWENWENWESESWSEW") == "NNN"
    assert shortest_way_back.shortest_way_back("SENWNWESNSEWNWENESWSWEWNNENWNENWESENSWSEW") == "SSS"


def test_two_directions():
    """Test cases with movement in 2 directions, no canceling out."""
    assert shortest_way_back.shortest_way_back("WNW") in ["SEE", "ESE", "EES"]
    assert shortest_way_back.shortest_way_back("SSE") in ["NNW", "NWN", "WNN"]
    assert shortest_way_back.shortest_way_back("ENN") in ["SSW", "WSS", "SWS"]
    assert shortest_way_back.shortest_way_back("WWS") in ["NEE", "ENE", "EEN"]


def test_three_directions():
    """Test movement in 3 directions, movement back in 2 directions."""
    assert shortest_way_back.shortest_way_back("WNSNNWS") in ["SEE", "ESE", "EES"]
    assert shortest_way_back.shortest_way_back("SSNENES") in ["WWN", "WNW", "NWW"]


def test_four_directions():
    """Test movement in 4 directions with movement back in 2 directions."""
    assert shortest_way_back.shortest_way_back("WNSNENWS") in ["SE", "ES"]
    assert shortest_way_back.shortest_way_back("SSEWENSN") in ["NW", "WN"]


def test_random():
    """Test 5 random cases."""
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
