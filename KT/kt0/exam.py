"""KT0."""


def nr_of_common_characters(string1: str, string2: str) -> int:
    """
    Return a number of common characters of string1 and string2.

    Do not take into account repeated characters.

    common_characters("iva", "avis") -> 3 # 'a', 'i', 'v' are common
    common_characters("saali", "pall") -> 2  # 'a', 'l' are common
    common_characters("memm", "taat") -> 0
    common_characters("memm", "") -> 0

    """
    count = 0
    word1 = []
    word2 = []
    for i in string1:
        word1.append(i)
    for j in string2:
        word2.append(j)
    for _ in set(word1):
        if _ in set(word2):
            count += 1
    return count


def nr_into_num_list(nr: int, num_list: list) -> list:
    """
    Return a list of numbers where the "nr" is added into the "num_list" so that the list keep going to be sorted.

    Built-in sort methods are not allowed.

    nr_into_num_list(5, []) -> [5]
    nr_into_num_list(5, [1,2,3,4]) -> [1,2,3,4,5]
    nr_into_num_list(5, [1,2,3,4,5,6]) -> [1,2,3,4,5,5,6]
    nr_into_num_list(0, [1,2,3,4,5]) -> [0,1,2,3,4,5,]

    """
    num_list.append(nr)
    if len(num_list) == 1:
        return num_list
    i = -1
    while num_list[i] != num_list[0]:
        if num_list[i] < num_list[i - 1]:
            num_list[i], num_list[i - 1] = num_list[i - 1], num_list[i]
            i -= 1
        else:
            return num_list
    return num_list
