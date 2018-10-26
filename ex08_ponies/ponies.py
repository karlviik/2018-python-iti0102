import codecs


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
    pass


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


print(decode('TWF1ZCBQb21tZWwgICAgICAgICBVbmljb3JuICAgICAgICAgICAgIHBpbmsgICAgICAgICAgICAgICAgZ3JlZW4gICAgICAgICA'
+ 'gICAgICBjeWFuICAgICAgICAgICAgICAgIENhc3RsZSBvZiBGcmllbmRzaGlw'))
