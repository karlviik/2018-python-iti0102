def recursive_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using recursion.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    numbersum = 0
    if numbers[0] % 2 == 0:
        numbersum = numbers[0]
    if len(numbers) > 1:
        return numbersum + recursive_sum(numbers[1:])
    return numbersum


def loop_sum(numbers: list) -> int:
    """
    Find out the sum of all the even numbers using loops.

    :param numbers: list of randomly ordered numbers
    :return: sum of even numbers
    """
    numbersum = 0
    for number in numbers:
        if number % 2 == 0:
            numbersum += number
    return numbersum


def loop_reverse(s: str) -> str:
    """Reverse a string using a loop.

    :param s: string
    :return: reverse of s
    """
    news = ""
    for letter in s:
        news = letter + news
    return news


def recursive_reverse(s: str) -> str:
    """Reverse a string using recursion.

    :param s: string
    :return: reverse of s
    """
    if len(s) > 1:
        return s[-1] + recursive_reverse(s[:-1])
    return s


if __name__ == '__main__':
    print(recursive_sum([1, 3, 5, 7, 9]))
    print(recursive_sum([2, 4, 5, 8]))
    print(loop_sum([1, 3, 5, 7, 9]))
    print(loop_sum([2, 4, 5, 8]))
    print(recursive_reverse("abcdef"))
    print(loop_reverse("abcdef"))