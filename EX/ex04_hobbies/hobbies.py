"""Hobbies."""
import csv


def create_list_from_file(file):
    """
    Collect lines from given file into list.

    :param file: original file path
    :return: list of lines
    """
    with open("hobbies_database.txt", encoding='utf-8') as file:
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
        return "Empty dictionary."
    for name, value in name_dictionary.items():
        if len(value) > a:
            a = len(value)
            active_person = name
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
        return "Empty dictionary."
    for name, value in name_dictionary.items():
        if len(value) < a:
            a = len(value)
            passive_person = name
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
        if value == a:
            hobby.append(name)
    hobby = sorted(list(set(hobby)))
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
        if value == a:
            hobby.append(name)
    hobby = list(set(hobby))
    return hobby


def write_corrected_database(file, file_to_write):
    """
    Write .csv file in a proper way. Use collected and structured data.

    :param file: original file path
    :param file_to_write: file to write result
    """
    name_dictionary = sorted(create_dictionary(file).items())
    print(name_dictionary)
    with open(file_to_write, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        name = "Name"
        hobbies = "Hobbies"
        writer.writerow([name, hobbies])
        for element in name_dictionary:
            writer.writerow([element[0], '-'.join(element[1])])

# These examples are based on a given text file from the exercise.


if __name__ == '__main__':
    dic = create_dictionary("hobbies_database.txt")
    print(len(create_list_from_file("hobbies_database.txt")))  # -> 100
    print("Check presence of hobbies for chosen person:")
    print("shopping" in dic["Wendy"])  # -> True
    print("fitness" in dic["Sophie"])  # -> False
    print("gaming" in dic["Peter"])  # -> True
    print("Check if hobbies - person relation is correct:")
    print("Check if a person(people) with the biggest amount of hobbies is(are) correct:")
    print(find_person_with_most_hobbies("hobbies_database.txt"))  # -> ['Jack']
    print(len(dic["Jack"]))  # ->  12
    print(len(dic["Carmen"]))  # -> 10
    print("Check if a person(people) with the smallest amount of hobbies is(are) correct:")
    print(find_person_with_least_hobbies("hobbies_database.txt"))  # -> ['Molly']
    print(len(dic["Molly"]))  # -> 5
    print(len(dic["Sophie"]))  # -> 7
    print("Check if the most popular hobby(ies) is(are) correct")
    print(find_most_popular_hobby("hobbies_database.txt"))  # -> ['gaming', 'sport', 'football']
    print("Check if the least popular hobby(ies) is(are) correct")
    print(find_least_popular_hobby("hobbies_database.txt"))  # -> ['tennis', 'dance', 'puzzles', 'flowers']
    write_corrected_database("hobbies_database.txt", 'correct_hobbies_database.csv')
