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
        cpos_al = 0
        while cpos_al < len_al:
            if message[cpos_mes].lower() == alphabet[cpos_al].lower():
                if message[cpos_mes] == message[cpos_mes].upper():
                    new_message += alphabet[(cpos_al + shift) % len_al].upper()
                else:
                    new_message += alphabet[(cpos_al + shift) % len_al].lower()
                cpos_al = len_al
            elif cpos_al == len_al - 1:
                new_message += message[cpos_mes]
            cpos_al += 1
        cpos_mes += 1
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


#if __name__ == "__main__":
    # simple tests
    #print(encode(";:;:;;::;:;:", 1, ";:"))  # ifmmp
    #print(decode("ifmmp", 1))  # hello

    # WRITE THE REMAINING EXAMPLES YOURSELF!

    # larger shift

    # negative shift

    # shift > alphabet.length

    # case sensitivity

    # misc symbols (.,:; etc.)

    # ...