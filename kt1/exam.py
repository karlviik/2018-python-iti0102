"""KT tasks."""


def capitalize_string(s: str) -> str:
    """
    Return capitalized string. The first char is capitalized, the rest remain as they are.

    capitalize_string("abc") => "Abc"
    capitalize_string("ABc") => "ABc"
    capitalize_string("") => ""
    """
    if len(s) == 1:
        return s[0].upper()
    if len(s) > 1:
        return s[0].upper() + s[1:]
    return ""


def sum_half_evens(nums: list) -> int:
    """
    Return the sum of first half of even ints in the given array.

    If there are odd number of even numbers, then include the middle number.

    sum_half_evens([2, 1, 2, 3, 4]) => 4
    sum_half_evens([2, 2, 0, 4]) => 4
    sum_half_evens([1, 3, 5, 8]) => 8
    sum_half_evens([2, 3, 5, 7, 8, 9, 10, 11]) => 10
    """
    evennums = []
    for num in nums:
        if not num % 2:
            evennums.append(num)
    amount = int((len(evennums) + 1) / 2)
    return sum(evennums[:amount])


def max_block(s: str) -> int:
    """
    Given a string, return the length of the largest "block" in the string.

    A block is a run of adjacent chars that are the same.

    max_block("hoopla") => 2
    max_block("abbCCCddBBBxx") => 3
    max_block("") => 0
    """
    largestblock = 0
    thisblock = 0
    blockchar = ""
    for letter in s:
        if letter == blockchar:
            thisblock += 1
        else:
            if thisblock > largestblock:
                largestblock = thisblock
            thisblock = 1
            blockchar = letter
    return largestblock


"""
print(max_block("hoooooopppppppla"))  # = > 2
print(max_block("abbCcCCddBBBxx"))  # = > 3
print(max_block(""))  # = > 0
"""
