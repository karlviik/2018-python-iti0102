"""Encode and decode Caesar cipher."""

def code(message: str, shift: int, alphabet: str) -> str:
    """
    Do the actual de or encoding.

    :param message: String.
    :param shift: Shift amount.
    :param alphabet: Symbols in use.
    :return: string
    """
    message_len = len(message)
    alphabet_len = len(alphabet)
    current_pos_message = 0
    new_message = ""
    while current_pos_message < message_len:
        current_pos_alphabet = 0
        while current_pos_alphabet < alphabet_len:
            if message[current_pos_message].lower() == alphabet[current_pos_alphabet].lower():
                if message[current_pos_message] == message[current_pos_message].upper():
                    new_message += alphabet[(current_pos_alphabet + shift) % alphabet_len].upper()
                else:
                    new_message += alphabet[(current_pos_alphabet + shift) % alphabet_len].lower()
                current_pos_alphabet = alphabet_len
            elif current_pos_alphabet == alphabet_len - 1:
                new_message += message[current_pos_message]
            current_pos_alphabet += 1
        current_pos_message += 1
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


if __name__ == "__main__":
    # simple tests
    print(encode("hello", 1))  # ifmmp
    print(decode("ifmmp", 1))  # hello

    # WRITE THE REMAINING EXAMPLES YOURSELF!

    # larger shift

    # negative shift

    # shift > alphabet.length

    # case sensitivity

    # misc symbols (.,:; etc.)

    # ...