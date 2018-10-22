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
    assert shortest_way_back.shortest_way_back("SWEWESEEWEWWS") == "NNN"
    assert shortest_way_back.shortest_way_back("NEWWENWWWNWEEEEEW") == "SSS"
    assert shortest_way_back.shortest_way_back("ENSENSSNNESNNNSSNSS") == "WWW"
    assert shortest_way_back.shortest_way_back("SNSNWWNNNSSSNSNSNSSWNSSNN") == "EEE"


def test_four_directions_out_one_direction_in():
    assert shortest_way_back.shortest_way_back("SENWWNSWENSWEWNNWESWSEW") == "EEE"
    assert shortest_way_back.shortest_way_back("SENWWENSEWENESWEWENENWEESWSEW") == "WWW"
    assert shortest_way_back.shortest_way_back("SENWWESNSEWWENESWSWEWENWENWESESWSEW") == "NNN"
    assert shortest_way_back.shortest_way_back("SENWNWESNSEWNWENESWSWEWNNENWNENWESENSWSEW") == "SSS"


def test_two_directions():
    assert shortest_way_back.shortest_way_back("WNW") in ["SEE", "ESE", "EES"]
    assert shortest_way_back.shortest_way_back("SSE") in ["NNW", "NWN", "WNN"]


def test_three_directions():
    assert shortest_way_back.shortest_way_back("WNSNNWS") in ["SEE", "ESE", "EES"]
    assert shortest_way_back.shortest_way_back("SSNEE") in ["WWN", "WNW", "NWW"]


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
    assert shortest_way_back.shortest_way_back("SN" * 100) == ""




# TODO: add more functions
