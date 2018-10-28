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
    pass


def filter_by_location(ponies: list) -> list:
    pass


def filter_by_kind(ponies: list, kind: str) -> list:
    pass


def get_points_for_color(color: str) -> int:
    pass


def add_points(pony: dict) -> dict:
    pass


def evaluate_ponies(ponies: list) -> list:
    pass


def sort_by_name(ponies: list) -> list:
    pass


def sort_by_points(ponies: list) -> list:
    pass


def format_line(pony: dict, place: int) -> str:
    pass


def write(input_file: str, kind: str):
    pass


assert extract_information(' MaudPommel       Unicorn       pink  green     cyan   Castle of Friendship\n') == {'name': 'MaudPommel', 'kind': 'Unicorn', 'coat_color': 'pink', 'mane_color': 'green', 'eye_color': 'cyan', 'location': 'Castle of Friendship'}

