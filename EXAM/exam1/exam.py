"""Exam 1 (2021-01-04)."""


def sum_of_multiples(limit: int, multiplier: int):
    """
    Given a limit, find the sum of all the multiples of multiplier up to but not including that number.

    #1

    Limit and multiplier are both natural numbers.
    If limit is smaller or equal than multiplier it should return 0.

    sum_of_multiples(20, 5) -> 30
    sum_of_multiples(10, 1) -> 45
    sum_of_multiples(5, 5) -> 0
    """
    summa = 0
    if limit <= multiplier:
        return summa
    for i in range(multiplier, limit, multiplier):
        summa += i
    return summa


def mix_string(s1: str, s2: str) -> str:
    """
    Given two strings s1 and s2, create a mixed string by alternating between str1 and str2 chars.

    #2

    mix_string("AAA", "bbb") -> AbAbAb
    mix_string("AA", "") -> AA
    mix_string("mxdsrn", "ie tig") -> mixed string
    """
    result = ''
    for i in range(len(s2) + len(s1)):
        if i % 2 == 0:
            result += s1[i // 2]
        else:
            result += s2[i // 2]
    return result


def bingo(matrix: list, numbers: list) -> tuple:
    """
    Whether the matrix has winning combinations with the given numbers.

    #3

    Check if player got any winning combinations:
    1. Corners - all 4 corners contain winning numbers
    2. Diagonals - all diagonals contain winning numbers
    3. Full game - all numbers in the matrix/ticket are in the winning numbers
    Example matrix:
    [
        [ 5,  7, 11, 15, 21],
        [22, 25, 26, 27,  9],
        [34,  2, 48, 54, 58],
        [59, 61, 33, 81, 24],
        [90, 37,  3,  6, 32],
    ]

    :param matrix: 5 x 5 bingo ticket of numbers
    :param numbers: list of winning numbers (size always at least 4)
    :return: tuple of booleans (corners, diagonals, full_game)
    """
    corners = matrix[0][0] in numbers and matrix[0][4] in numbers and matrix[4][0] in numbers and matrix[4][4] in numbers
    diagonals = True
    for i in range(len(matrix)):
        if matrix[i][i] not in numbers or matrix[i][len(matrix[i]) - 1 - i] not in numbers:
            diagonals = False
    full = False
    if diagonals:
        full = True
        for row in matrix:
            for n in row:
                if n not in numbers:
                    full = False
    return (corners, diagonals, full)


def can_reach(arr: list, start: int) -> bool:
    """
    Given an array of non-negative integers arr, you are initially positioned at start index of the array.

    #4

    When you are at index i, you can jump to i + arr[i] or i - arr[i], check if you can reach to any index with value 0.

    Notice that you can not jump outside of the array at any time.

    Solution has to be recursive!

    Example 1:
    Input: arr = [4,2,3,0,3,1,2], start = 5
    Output: True
    Explanation:
    All possible ways to reach at index 3 with value 0 are:
    index 5 -> index 4 -> index 1 -> index 3
    index 5 -> index 6 -> index 4 -> index 1 -> index 3

    Example 2:
    Input: arr = [4,2,3,0,3,1,2], start = 0
    Output: True
    Explanation:
    One possible way to reach at index 3 with value 0 is:
    index 0 -> index 4 -> index 1 -> index 3

    Example 3:
    Input: arr = [1, 2, 0], start = 0
    Output: False
    From index 0, we can move to index 1, but then nowhere else.

    :return boolean whether a possible route exists or not
    """
    try:
        pos_value = start + arr[start]
        if arr[start] == 0:
            pos = True
        elif pos_value < 0:
            return False
        else:
            pos = can_reach(arr, pos_value)
    except IndexError:
        pos = False
    try:
        neg_value = start - arr[start]
        if arr[start] == 0:
            neg = True
        elif neg_value < 0:
            return False
        else:
            neg = can_reach(arr, neg_value)
    except IndexError:
        neg = False
    return pos or neg


def is_prime_number(number):
    """Check if the number is prime."""
    if (number == 0) or (number == 1):
        return False
    i = 2
    while number % i != 0:
        if i == number:
            return True
        i += 1
    return False


def prime_factorization(number: int) -> dict:
    """
    Given a natural number greater than 1, return it's prime factorization.

    #5

    Return the prime factorization of number.

    Return dict, where the key is a prime factor and the value is count of this factor.

    12 = 2 * 2 * 3 => {2: 2, 3: 1}
    1960 = 2 * 2 * 2 * 5 * 7 * 7 => {2: 3, 5: 1, 7: 2}
    79 = 79 * 1 => {79: 1}

    Prime number is a number which is divisible only by 1 and the number itself.
    For example 2, 3, 5, 7, 11, 13, 17, 19, 23 are prime numbers.

    Examples:
    2 => { 2: 1 }
    12 => { 2: 2, 3: 1 }
    1960 => { 2: 3, 5: 1, 7: 2 }
    1024 => { 2: 10 }
    79 => { 79: 1 }
    121 => { 11: 2 }

    :param number: a number greater than 1
    :return: dict of prime factors and their counts.
    """
    primes_count = {}
    while number > 1:
        for n in range(2, number + 1):
            if number % n == 0:
                if n in primes_count:
                    primes_count[n] += 1
                else:
                    primes_count[n] = 1
                number //= n
                break
    return primes_count


class Candy:
    """Candy #6."""

    def __init__(self, name: str, filling: str):
        """
        Candy class constructor.

        :param name: candy name
        :param filling: candy filling
        """
        self.name = name
        self.filling = filling

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name


class CandyShop:
    """Candy shop #6."""

    def __init__(self):
        """CandyShop class constructor."""
        self.cand = []

    def add_candies(self, list_candy: list):
        """
        Add list of fresh candies to already existing ones.

        :param list_candy: list of candies to add
        :return:
        """
        self.cand += list_candy

    def get_candies(self) -> list:
        """
        Return list of all candies existing in the shop.

        :return: list of all candies
        """
        return self.cand

    def get_candies_by_filling(self, filling: str) -> list:
        """
        Get list of candies that have the same filling as given in parameter value.

        :return: list
        """
        same = []
        for candy in self.get_candies():
            if candy.filling == filling:
                same.append(candy)
        return same

    def sort_candies_by_filling(self) -> list:
        """
        Method should return list of candies sorted by filling in alphabetical order.

        If filling is the same, then sort
        by name in alphabetical order.

        :return: sorted list of candies
        """
        cand = sorted(self.get_candies(), key=lambda x: x.name)
        cand = sorted(cand, key=lambda x: x.filling)
        return cand

    def get_candy_popularity(self):
        """
        Find how many candies of each filling and name.
        """
        stats = {}
        for candy in self.get_candies():
            if candy.name in stats:
                stats[candy.name] += 1
            else:
                stats[candy.name] = 1
        return stats

    def get_most_popular_candy_name_and_filling(self) -> dict:
        """
        Find the most popular candy name and filling.

        Method should return dict with name and filling of the most popular candy in the shop (type of candy which name
        and filling is present the most in the shop). NB! You should consider the most popular combination of name and filling.
        {name: most_pop_candy_name, filling: most_pop_candy_filling}

        If there are several suitable candidates, return any of those (doesn't matter which one).

        :return: dict with name and filling of most pop candy
        """
        candies = self.get_candy_popularity()
        candy = max(candies, key=lambda x: candies[x])
        for c in self.cand:
            if c.name == candy:
                candy = c
        return {'name': candy.name, 'filling': candy.filling}

    def get_least_popular_candy_name_and_filling(self) -> dict:
        """
        Find the least popular candy name and filling.

        Method should return dict with name and filling of the least popular candy in the shop (type of candy which name
        and filling is present the least in the shop). NB! You should consider the least popular combination of name and filling.
        {name: least_pop_candy_name, filling: least_pop_candy_filling}

        If there are several suitable candidates, return any of those (doesn't matter which one).

        :return: dict with name and filling of least pop candy
        """
        candies = self.get_candy_popularity()
        candy = min(candies, key=lambda x: candies[x])
        for c in self.cand:
            if c.name == candy:
                candy = c
        return {'name': candy.name, 'filling': candy.filling}

    def collect_candies_by_filling(self) -> dict:
        """
        Group candies by filling.

        Method should return dict with candies divided by filling, where dict key is filling and dict value is list
        of candies with this filling.
        {candy_filling: [candy1, candy2]}

        :return: dict of candies divided by filling
        """
        filling_groups = {}
        for candy in self.get_candies():
            if candy.filling in filling_groups:
                filling_groups[candy.filling].append(candy)
            else:
                filling_groups[candy.filling] = [candy]
        return filling_groups


class Grade:
    """Grade #7."""

    def __init__(self, grade, weight: int, assignment: str, date: str):
        """Constructor."""
        self.assignment = assignment
        self.value = grade
        self.weight = weight
        self.date = date
        self.previous_grades = {}

    def change_grade(self, new_grade: int, date: str):
        """
        Change a previous grade.

        This function should save the previous grade in a dictionary previous_grades, where key is the date and value
        is the value of the grade. Value and date should be updated.
        """
        self.previous_grades[self.date] = self.value
        self.value = new_grade
        self.date = date


class Student:
    """Student #7."""

    def __init__(self, name: str):
        """Constructor."""
        self.name = name
        self.grades = {}

    def grade(self, grade: Grade):
        """
        Add a grade for an assignment that a students has done.

        Grades are kept in a dictionary where assignment name is the key and Grade object is the value (All previous
        grades for the same assignment are kept in the Grade object previous grades dictionary).
        Note that this function is only used when a student does an assignment for the first time.
        """
        self.grades[grade.assignment] = grade

    def redo_assignment(self, new_grade: int, assignment: str, date: str):
        """
        Update the grade for given assignment.

        This function is only used when an assignment has been attempted at least once before. Keep in mind that you
        need to also keep the history of grades, not create a new grade!
        """
        self.grades[assignment].change_grade(new_grade, date)

    def calculate_weighted_average(self):
        """
        Calculate the weighted average of grades.

        You should take into account the weights. There are three weights: 1, 2 and 3, where 3 means that one grade of
        weight 3 is the same as three grades of weight 1.

        For example:
        if there are grades 4 with weight 3 and 3 with weight 1, then the resulting value will be
                (4 * 3 + 3 * 1) / (3 + 1) = 15 / 4 = 3.75
        which will be rounded to 4.

        Also make sure not to miss out when a grade is noted as "!". If there is no attempt to redo this, then "!"
        should be equivalent to grade "1".
        """
        value = 0
        number = 0
        for grade in self.grades.values():
            value = grade.value
            if grade.value == '!':
                value = 1
            value += grade.weight * value
            number += grade.weight
        average = value / number
        return round(average)


class Class:
    """Class #7."""

    def __init__(self, teacher: str, students: list):
        """Constructor."""
        self.teacher = teacher
        self.students = students

    def add_student(self, student: Student):
        """Add student to the class."""
        self.students.append(student)

    def add_students(self, students: list):
        """Add several students to the class."""
        self.students += students

    def remove_student(self, student: Student):
        """Remove student from the class."""
        self.students.remove(student)

    def get_grade_sheet(self):
        """
        Return grade sheet as a table.

        Grade sheet includes information of all the students in the class and their final grades.
        All edges should be either "|" or "-".
        First column is student's name and the second column is the final grade (weighted average).
        First, second and third row should look something like this (notice the capital letters):
        ----------------------
        | Name | Final grade |
        ----------------------

        Make sure that all the columns are correctly aligned after the longest element.
        For example, consider following rows:
        | Ago                   |  5  |
        | Some really long name |  3  |

        Rules are following:
        Each row (except for "-----" rows) starts with "|" and a space " " and ends with a space " " and "|".
        Text in "Name" column needs to be aligned to left
        Grades in "Final grade" column need to be centered

        Students in the table should follow the order which they were added to the class.

        The whole table would look something like this:
        ---------------------------------------
        | Name                  | Final grade |
        ---------------------------------------
        | Ago                   |      5      |
        | Johannes              |      4      |
        | Mari                  |      5      |
        | Some really long name |      3      |
        ---------------------------------------

        """
        pass


if __name__ == '__main__':
    assert sum_of_multiples(20, 5) == 30

    assert mix_string("AAA", "bbb") == "AbAbAb"
    assert bingo([
        [5, 7, 11, 15, 21],
        [22, 25, 26, 27, 9],
        [34, 2, 48, 54, 58],
        [59, 61, 33, 81, 24],
        [90, 37, 3, 6, 32],
    ], [5, 21, 90, 32]) == (True, False, False)
    assert bingo([
        [5, 7, 11, 15, 21],
        [22, 25, 26, 27, 9],
        [34, 2, 48, 54, 58],
        [59, 61, 33, 81, 24],
        [90, 37, 3, 6, 32],
    ], [5, 21, 90, 32, 25, 48, 81, 27, 61, 91]) == (True, True, False)
    print(mix_string('sk', 'ua'))

    assert can_reach([1, 0, 1], 2) is True

    assert prime_factorization(1960) == {2: 3, 5: 1, 7: 2}
    print(mix_string('sk', 'ua'))
    candy_shop = CandyShop()
    candy1 = Candy('candy1', 'chocolate')
    candy2 = Candy('candy2', 'caramel')
    candy3 = Candy('candy3', 'nut')
    candy4 = Candy('candy1', 'chocolate')
    candy5 = Candy('candy2', 'vanilla')
    candy6 = Candy('candy2', 'vanilla')
    candy7 = Candy('candy3', 'nut')
    candy8 = Candy('candy1', 'chocolate')

    candies = [candy1, candy2, candy3, candy4, candy5, candy6, candy7, candy8]
    candy_shop.add_candies(candies)
    # NB! there are candy variable names in comments, not instance name parameter values!!!
    print(candy_shop.get_candies_by_filling('chocolate'))  # [candy1, candy4, candy8]
    print(candy_shop.get_candy_popularity())
    print(candy_shop.get_least_popular_candy_name_and_filling())  # {name: candy2, filling: caramel}
    print(candy_shop.get_most_popular_candy_name_and_filling())  # {name: candy1, filling: chocolate}
    print(candy_shop.sort_candies_by_filling())  # [candy2, candy1, candy4, candy8, candy7, candy3, candy6, candy5]
    print(candy_shop.collect_candies_by_filling())  # {chocolate: [candy1, candy4, candy8],
    #                                                  caramel: [candy2],
    #                                                  nut: [candy3, candy7],
    #                                                  vanilla: [candy5, candy6]}
    print(mix_string('sk', 'ua'))

    # Teacher, grade, student
    mari = Student("Mari Maa")
    jyri = Student("Jyri Jogi")
    teele = Student("Teele Tee")
    cl = Class("Anna", [mari, jyri, teele])
    mari.grade(Grade(5, 3, "KT", "01/09/2020"))
    gr = Grade("!", 3, "KT", "01/09/2020")
    jyri.grade(gr)
    teele.grade(Grade(4, 3, "KT", "01/09/2020"))

    print(f"Jyri keskmine hinne on {jyri.calculate_weighted_average()}.")  # 1

    jyri.redo_assignment(3, "KT", "14/09/2020")
    print(len(gr.previous_grades))  # 1

    print(f"Jyri keskmine hinne on nyyd {jyri.calculate_weighted_average()}.")  # 3
    print()

    mari.grade(Grade(5, 1, "TK", "30/11/2020"))
    jyri.grade(Grade(4, 1, "TK", "30/11/2020"))
    teele.grade(Grade(3, 1, "TK", "30/11/2020"))

    print(f"Teele keskmine hinne on {teele.calculate_weighted_average()}.")  # 4
    print(cl.get_grade_sheet())

    tuuli = Student("Tuuli Karu")
    cl.add_student(tuuli)
    print(len(cl.students))  # 4
