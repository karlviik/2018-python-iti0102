import codecs
import re


def decode(line: str) -> str:
    """
    Decode input base64 in unicode string into unicode string.

    :param line: given base64 in unicode string
    :return: decoded base64 in unicode
    """
    line = line.encode("utf-8")
    line = codecs.decode(line, "base64")
    line = line.decode("utf-8")
    return line


def extract_information(line: str) -> dict:
    """
    Extract pony info and put into dictionary.

    :param line: string of pony attributes
    :return: dictionary of pony attributes
    """
    regex = "[^(\\s{2,'inf'})]([a-zA-Z]|(\\s(?!\\s)))+"
    info_type_list = ["name", "kind", "coat_color", "mane_color", "eye_color", "location"]
    info_dict = {}
    for counter, match in enumerate(re.finditer(regex, line)):
        match = match.group()
        if match.find("\n") > -1:
            match = match[:-1]
        info_dict[info_type_list[counter]] = match
    return info_dict


def read(read_file: str) -> list:
    """
    Read coded lines from file, decode, extract info and put dictionaries into list.

    :param read_file: file with coded lines
    :return: list of dictionaries of pony info
    """
    try:
        with open(read_file, "r") as f:
            lines = f.readlines()
    except FileNotFoundError:
        raise Exception("File not found!")
    ponylist = []
    for count, line in enumerate(lines):
        if count > 1:
            ponylist.append(extract_information(decode(line)))
    return ponylist


def filter_by_location(ponies: list) -> list:
    """
    Filter out ponies with location set as none.

    :param ponies: list of pony dictionaries
    :return: list of filtered pony dictionaries
    """
    filteredponies = []
    for counter, ponydict in enumerate(ponies):
        if ponydict["location"] != "None":
            filteredponies.append(ponydict)
    return filteredponies


def filter_by_kind(ponies: list, kind: str) -> list:
    """
    Return dict of ponies with kind set as input string kind.

    :param ponies: pony info dictionary
    :param kind: required kind
    :return: list of pony dictionaries with kind set as input
    """
    filteredponies = []
    for counter, ponydict in enumerate(ponies):
        if ponydict["kind"] == kind:
            filteredponies.append(ponydict)
    return filteredponies


def get_points_for_color(color: str) -> int or None:
    """
    Return amount of points for that color.

    :param color: color to be evaluated
    :return: points for said color based on list
    """
    colors = [
        'magenta', 'pink', 'purple', 'orange', 'red', 'yellow', 'cyan', 'blue', 'brown', 'green'
    ]
    for counter, listcolor in enumerate(colors):
        if listcolor == color:
            points = abs(counter - 10)
            if points < 5:
                return None
            return points


def add_points(pony: dict) -> dict:
    """
    Add key "points" to the dict and return it if location is valid.

    :param pony: dict of pony info
    :return: dict of pony info plus points key
    """
    evaluation_locations = ['Town Hall', 'Theater', 'School of Friendship', 'Schoolhouse', 'Crusaders Clubhouse', 'Golden Oak Library', 'Train station', 'Castle of Friendship', 'Retirement Village']
    if pony["location"] in evaluation_locations:
        pony["points"] = None
    return pony


def evaluate_ponies(ponies: list) -> list:
    """
    Give points for pony colours and add it to key "points" and return new list with new dicts.

    :param ponies: list of pony dicts
    :return: list of pony dicts with new points key
    """
    evaluation_locations = {
        'coat_color': ['Town Hall', 'Theater', 'School of Friendship'],
        'mane_color': ['Schoolhouse', 'Crusaders Clubhouse', 'Golden Oak Library'],
        'eye_color': ['Train station', 'Castle of Friendship', 'Retirement Village']
    }
    newponies = []
    for pony in ponies:
        pony = add_points(pony)
        location = pony["location"]
        for key, locations in evaluation_locations.items():
            if location in locations:
                colortograde = pony[key]
                break
        pony["points"] = get_points_for_color(colortograde)
        newponies.append(pony)
    return newponies


def sort_by_name(ponies: list) -> list:
    """
    Sort the list of dictionaries in alphabetical order based on pony names.

    :param ponies:
    :return:
    """
    def get_name(dictionary):
        return dictionary["name"]
    return sorted(ponies, key=get_name)


def sort_by_points(ponies: list) -> list:
    """
    Sort the list of dictionaries based on pony points.

    :param ponies: list of pony dicts
    :return: list of sorted pony dicts by points
    """
    newponies = []
    for pony in ponies:
        if pony["points"] != None:
            newponies.append(pony)

    def get_points(dictionary):
        return dictionary["points"]
    return sorted(newponies, key=get_points, reverse=True)


def format_line(pony: dict, place: int) -> str:
    pass


def write(input_file: str, kind: str):
    pass



print(decode("TkFNRSAgICAgICAgICAgICAgICBLSU5EICAgICAgICAgICAgICAgIENPQVQgQ09MT1IgICAgICAgICAgTUFORSBDT0xPUiAgICAgICAgICBFWUUgQ09MT1IgICAgICAgICAgIExPQ0FUSU9O"))