"""Order names by popularity."""


def read_from_file() -> list:
    """
    Create the list of all the names.

    :return: list
    """
    names = []
    with open("popular_names.txt", encoding='utf-8') as file:
        for line in file:
            names.append(line.strip())
    return names


def to_dictionary(names: list) -> dict:
    """
    Make a dictionary from a list of names.

    :param names: list of all the names
    :return: dictionary {"name:sex": number}
    """
    name_counter = {}
    number = 1
    for name in names:
        if name not in name_counter:
            name_counter[name] = number
        else:
            name_counter[name] = name_counter[name] + 1
    return name_counter


def to_sex_dicts(names_dict: dict) -> tuple:
    """
    Divide the names by sex to 2 different dictionaries.

    :param names_dict: dictionary of names
    :return: two dictionaries {"name": number}, {"name": number}
    first one is male names, seconds is female names.
    """
    woman_dict = {}
    man_dict = {}
    for key, value in names_dict.items():
        if key.endswith("F"):
            woman_dict[key[0:-2]] = value
    for key, value in names_dict.items():
        if key.endswith("M"):
            man_dict[key[0:-2]] = value
    return man_dict, woman_dict


def most_popular(names_dict: dict) -> str:
    """
    Find the most popular name in the dictionary.

    If the dictionary is empty, return "Empty dictionary."
    :param names_dict: dictionary of names (key is name, value is count)
    :return: string
    """
    a = 0
    if names_dict == {}:
        return "Empty dictionary."
    for key, value in names_dict.items():
        if value > a:
            a = value
            b = key
    return b


def number_of_people(names_dict: dict) -> int:
    """
    Calculate the number of people in the dictionary.

    :param names_dict: dictionary of names (key is name, value is count)
    :return: int
    """
    summa = 0
    for value in names_dict.values():
        summa += value
    return summa


def names_by_popularity(names_dict: dict) -> str:
    r"""
    Create a string used to print the names by popularity.

    Format:
        1. name: number of people + "\n"
        ...

    Example:
        1. Kati: 100
        2. Mati: 90
        3. Nati: 80
        ...

    :param names_dict: dictionary of the names (key is name, value is count)
    :return: string
    """
    bruh = list(names_dict)
    string = ""
    if names_dict == {}:
        return ""
    if bruh[0].endswith(":F") or bruh[0].endswith(":M"):
        for key in bruh:
            names_dict[key[:-2]] = names_dict.pop(key)
    sorted(names_dict, )
    for i in range(len(names_dict)):
        name = most_popular(names_dict)
        amount = names_dict.get(name)
        string += f"{i + 1}. {name}: {amount}\n"
        names_dict.pop(name)
    return string
