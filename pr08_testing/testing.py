import pytest
import shortest_way_back
import random


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
    assert shortest_way_back.shortest_way_back("WENSSNEW") == ""


def test_three_directions_out_one_direction_in():
    assert shortest_way_back.shortest_way_back("SWEWES") == "NN"
    assert shortest_way_back.shortest_way_back("NEWWEN") == "SS"
    assert shortest_way_back.shortest_way_back("ENSENS") == "WW"
    assert shortest_way_back.shortest_way_back("SNSNWW") == "EE"


def test_two_directions():
    assert shortest_way_back.shortest_way_back("WNW") in ["SEE", "ESE", "EES"]
    assert shortest_way_back.shortest_way_back("SSE") in ["NNW", "NWN", "WNN"]

# TODO: add more functions
