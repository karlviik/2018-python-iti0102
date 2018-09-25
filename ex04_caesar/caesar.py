"""Encode and decode Caesar cipher."""


def code(message: str, shift: int, alphabet: str) -> str:
    """
    Do the actual de or encoding.

    :param message: String.
    :param shift: Shift amount.
    :param alphabet: Symbols in use.
    :return: string
    """
    len_mes = len(message)
    len_al = len(alphabet)
    cpos_mes = 0

    new_message = ""

    while cpos_mes < len_mes:

        cpos_al = 0     # resets alphabet counter
        while cpos_al < len_al:

            if message[cpos_mes].lower() == alphabet[cpos_al].lower():  # if message's character is part of alphabet
                if message[cpos_mes] == message[cpos_mes].upper():      # if char is capitalized
                    new_message += alphabet[(cpos_al + shift) % len_al].upper()
                else:                                                   # if char is not capitalized
                    new_message += alphabet[(cpos_al + shift) % len_al].lower()
                cpos_al = len_al

            elif cpos_al == len_al - 1:         # adds the char to message if it's not in alphabet
                new_message += message[cpos_mes]

            cpos_al += 1
        cpos_mes += 1

    if new_message == "":   # deals with empty alphabet
        new_message = message

    return new_message


def encode(message: str, shift: int, alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Encode the given message using the Caesar cipher principle.

    :param message: The string to be encoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Encoded string.
    """
    return code(message, shift, alphabet)


def decode(message: str, shift: int, alphabet: str = "abcdefghijklmnopqrstuvwxyz") -> str:
    """
    Decode the given message already encoded with the caesar cipher principle.

    :param message: The string to be decoded.
    :param shift: Determines the amount of symbols to be shifted by.
    :param alphabet: Determines the symbols in use. Defaults to the standard latin alphabet.
    :return: Decoded string.
    """
    return code(message, -shift, alphabet)
