"""Collect story parts from a messy text."""
import re


def read_file(file) -> str:
    """
    Read the text from given file into string.

    :param file: file path
    :return: string
    """
    with open(file) as txt:
        return get_clean_text(txt.read())


def get_clean_text(messy_text: str) -> str:
    """
    Process given text, remove unneeded symbols and retrieve a story.

    :param messy_text: string
    :return: clean string
    """
    regex = "[a-zA-Z:\\.*?!/\\s'-]"
    clean_string = ""
    big = 1
    quotes = 0
    symbfrom = r"*?/!"
    symbto = r'"!,?'
    for match in re.finditer(regex, messy_text):
        temp = match.group()
        if temp in symbfrom:
            a = symbfrom.find(temp)
            temp = symbto[a]
            big = a % 2
            if not a:
                quotes += 1
                if quotes % 2:
                    big = 1
        elif temp == ".":
            big = 1
        elif big and temp.lower() in "abcdefghijklmnopqrstuvwxzy":
            temp = temp.upper()
            big = 0
        clean_string += temp
    return clean_string
