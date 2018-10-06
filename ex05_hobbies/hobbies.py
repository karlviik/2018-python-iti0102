"""Hobbies."""
import csv


def create_list_from_file(file):
    """
    Collect lines from given file into list.

    :param file: original file path
    :return: list of lines
    """
    with open(file) as txt:
        return txt.readlines()


def create_dictionary(file):
    """
    Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2].

    :param file: original file path
    :return: dict
    """
    element = create_list_from_file(file)
    dic = {}
    for row in element:
        if row.find("\n"):
            nlcheck = -1
        else:
            nlcheck = len(row)
        colon = row.find(":")
        try:
            dic[row[:colon]]
        except KeyError:
            dic[row[:colon]] = set()
        dic[row[:colon]].add(row[colon + 1: nlcheck])
    for key, hobset in dic.items():
        hoblist = []
        for hobby in hobset:
            hoblist.append(hobby)
        dic[key] = hoblist
    return dic


def find_least_or_most_hobbies_person(file, l_or_m):
    """
    Get person list with least or most hobbies.

    :param file: original file path
    :param l_or_m: 0 for least, 1 for most hobbies
    :return: list of people with least or most hobbies
    """
    dic = create_dictionary(file)
    if l_or_m:
        hoblen = 0
    else:
        hoblen = float("inf")
    hobpeople = []
    for key, hoblist in dic.items():
        if len(hoblist) == hoblen:
            hobpeople.append(key)
        elif len(hoblist) < hoblen and not l_or_m or len(hoblist) > hoblen and l_or_m:
            hoblen = len(hoblist)
            hobpeople = [key]
    return hobpeople


def find_person_with_most_hobbies(file):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :return: list
    """
    return find_least_or_most_hobbies_person(file, 1)


def find_person_with_least_hobbies(file):
    """
    Find the person (or people) who have less hobbies than others.

    :param file: original file path
    :return: list
    """
    return find_least_or_most_hobbies_person(file, 0)


def find_least_or_most_popular_hobby(file, l_or_m):
    """
    Find least or most popular hobby.

    :param file: original file path
    :param l_or_m: 0 for least, 1 for most popular hobby
    :return: list of hobbies
    """
    dic = create_dictionary(file)
    hobdic = {}
    for _, hoblist in dic.items():
        for hobby in hoblist:
            try:
                hobdic[hobby] += 1
            except KeyError:
                hobdic[hobby] = 1
    if l_or_m:
        hobpop = 0
    else:
        hobpop = float("inf")
    pophoblist = []
    for hobby, hobbypop in hobdic.items():
        if hobbypop == hobpop:
            pophoblist.append(hobby)
        elif hobbypop < hobpop and not l_or_m or hobbypop > hobpop and l_or_m:
            hobpop = hobbypop
            pophoblist = [hobby]
    return pophoblist


def find_most_popular_hobby(file):
    """
    Find the most popular hobby.

    :param file: original file path
    :return: list
    """
    return find_least_or_most_popular_hobby(file, 1)


def find_least_popular_hobby(file):
    """
    Find the least popular hobby.

    :param file: original file path
    :return: list
    """
    return find_least_or_most_popular_hobby(file, 0)


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    dic = create_dictionary(file)
    allnames = []
    for name, hobbies in dic.items():
        allnames.append(name)
        hobbies.sort()
    allnames.sort()
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        for name in allnames:
            hoblist = ""
            maxhobbycount = len(dic[name])
            hobbycount = 1
            for hobby in dic[name]:
                hoblist += hobby
                if maxhobbycount != hobbycount:
                    hoblist += "-"
                hobbycount += 1
            writer.writerow([name, hoblist])
