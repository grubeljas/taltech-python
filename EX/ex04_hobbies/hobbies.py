"""Hobbies."""
import csv


def create_list_from_file(file):
    """
    Collect lines from given file into list.

    :param file: original file path
    :return: list of lines
    """
    with open(file, encoding='utf-8') as file:
        collected_data = file.readlines()
    return collected_data


def create_dictionary(file):
    """
    Create dictionary about given peoples' hobbies as Name: [hobby_1, hobby_2].

    :param file: original file path
    :return: dict
    """
    data = create_list_from_file(file)
    name_dictionary = {}
    for i in data:
        i = i[:-1]
        name_1hobby = i.split(":")
        if name_1hobby[0] in name_dictionary:
            if name_1hobby[1] in name_dictionary[name_1hobby[0]]:
                pass
            else:
                name_dictionary[name_1hobby[0]].append(name_1hobby[1])
        else:
            name_dictionary[name_1hobby[0]] = [name_1hobby[1]]
    return name_dictionary


def find_person_with_most_hobbies(file):
    """
    Find the person (or people) who have more hobbies than others.

    :param file: original file path
    :return: list
    """
    name_dictionary = create_dictionary(file)
    a = 0
    if name_dictionary == {}:
        return []
    for nam, value in name_dictionary.items():
        if len(value) > a:
            a = len(value)
            active_person = [nam]
        elif value == a:
            active_person.append(nam)
    return active_person


def find_person_with_least_hobbies(file):
    """
    Find the person (or people) who have less hobbies than others.

    :param file: original file path
    :return: list
    """
    name_dictionary = create_dictionary(file)
    a = 100
    if name_dictionary == {}:
        return []
    for name, value in name_dictionary.items():
        if len(value) < a:
            a = len(value)
            passive_person = [name]
        elif value == a:
            passive_person.append(name)
    return passive_person


def find_most_popular_hobby(file):
    """
    Find the most popular hobby.

    :param file: original file path
    :return: list
    """
    name_dictionary = create_dictionary(file)
    hobbies_dict = {}
    for hobbies in name_dictionary.values():
        for element in hobbies:
            if element not in hobbies_dict.keys():
                hobbies_dict[element] = 1
            else:
                hobbies_dict[element] = hobbies_dict[element] + 1
    a = 0
    for name, value in hobbies_dict.items():
        if value > a:
            a = value
            hobby = [name]
        elif value == a:
            hobby.append(name)
    return hobby


def find_least_popular_hobby(file):
    """
    Find the least popular hobby.

    :param file: original file path
    :return: list
    """
    name_dictionary = create_dictionary(file)
    hobbies_dict = {}
    for hobbies in name_dictionary.values():
        for element in hobbies:
            if element not in hobbies_dict.keys():
                hobbies_dict[element] = 1
            else:
                hobbies_dict[element] = hobbies_dict[element] + 1
    a = 1000
    for name, value in hobbies_dict.items():
        if value < a:
            a = value
            hobby = [name]
        elif value == a:
            hobby.append(name)
    return hobby


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    name_dictionary = create_dictionary(file)
    for listt in name_dictionary.values():
        listt.sort()
    name_dictionary = sorted(name_dictionary.items())
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        for element in name_dictionary:
            writer.writerow([element[0], '-'.join(element[1])])
