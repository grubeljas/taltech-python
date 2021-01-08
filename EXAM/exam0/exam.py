"""Exam0."""
from typing import Optional


def close_far(a: int, b: int, c: int) -> bool:
    """
    Return if one value is "close" and other is "far".

    #1

    Given three ints, a b c, return true if one of b or c is "close" (differing from a by at most 1),
    while the other is "far", differing from both other values by 2 or more.

    close_far(1, 2, 10) => True
    close_far(1, 2, 3) => False
    close_far(4, 1, 3) => True
    """
    if abs(b - c) > 1:
        if abs(a - b) < 2 and abs(a - c) > 1:
            return True
        if abs(a - c) < 2 and abs(a - b) > 1:
            return True
    return False


def get_names_from_results(results_string: str, min_result: int) -> list:
    """
    Given a string of names and scores, return a list of names where the score is higher than or equal to min_result.

    #2

    Results are separated by comma (,). Result contains a score and optionally a name.
    Score is integer, name can have several names separated by single space.
    Name part can also contain numbers and other symbols (except for comma).
    Return only the names which have the score higher or equal than min_result.
    The order of the result should be the same as in input string.

    get_names_from_results("ago 123,peeter 11", 0) => ["ago", "peeter"]
    get_names_from_results("ago 123,peeter 11,33", 10) => ["ago", "peeter"]  # 33 does not have the name
    get_names_from_results("ago 123,peeter 11", 100) => ["ago"]
    get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11) => ["ago", "peeter",  "kitty11!!"]
    get_names_from_results("ago 123,peeter 11,kusti riin 14", 12) => ["ago", "kusti riin"]
    """
    names = results_string.split(',')
    choosens = []
    name_scores = {}
    for name in names:
        score = name.split(' ')[-1]
        name = name.split(' ')[:-1]
        if name:
            name_scores[name[0]] = score
    for i in name_scores.items():
        if int(i[1]) >= min_result:
            choosens.append(i[0])
    return choosens


def tic_tac_toe(game: list) -> int:
    """
    Find game winner.

    #3

    The 3x3 table is represented as a list of 3 rows, each row has 3 element (ints).
    The value can be 1 (player 1), 2 (player 2) or 0 (empty).
    The winner is the player who gets 3 of her pieces in a row, column or diagonal.

    There is only one winner or draw. You don't have to validate whether the game is in correct (possible) state.
    I.e the game could have four 1s and one 0 etc.

    tic_tac_toe([[1, 2, 1], [2, 1, 2], [2, 2, 1]]) => 1
    tic_tac_toe([[1, 0, 1], [2, 1, 2], [2, 2, 0]]) => 0
    tic_tac_toe([[2, 2, 2], [0, 2, 0], [0, 1, 0]]) => 2

    :param game
    :return: winning player id
    """
    for row in game:
        if row[0] == row[1] == row[2] and row[0] != 0:
            return int(row[0])
    for i in range(3):
        if game[0][i] == game[1][i] == game[2][i] and game[0][i] != 0:
            return int(game[0][i])
    if game[0][0] == game[1][1] == game[2][2] or game[0][2] == game[1][1] == game[2][1]:
        if game[1][1] != 0:
            return int(game[1][1])
    return 0


def rainbows(field: str, lower=False) -> int:
    """
    Count rainbows.

    #4

    Function has to be recursive.

    assert rainbows("rainbowThisIsJustSomeNoise") == 1
    assert rainbows("WoBniar") == 1
    assert rainbows("rainbowobniar") == 1

    :param field: string to search rainbows from
    :return: number of rainbows in the string
    """
    field = list(field.lower())
    if set('rainbow') - set(field) == set():
        for i in list('rainbow'):
            field.remove(i)
        return 1 + rainbows(str(field))
    else:
        return 0


def longest_substring(text: str) -> str:
    """
    Find the longest substring.

    #5

    Substring may not contain any character twice.
    CAPS and lower case chars are the same (a == A)
    In output, the case (whether lower- or uppercase) should remain.
    If multiple substrings have same length, choose first one.

    aaa -> a
    abc -> abc
    abccba -> abc
    babcdEFghij -> abcdEFghij
    abBcd => Bcd
    '' -> ''
    """
    subs = []
    holder = ''
    for char in text:
        if char.lower() in holder.lower() or text.index(char) == len(text) - 1:
            if char.lower() not in holder.lower():
                holder += char
            subs.append(holder)
            holder = ''
        holder += char
    return max(subs, key=lambda x: len(x))


class Student:
    """Student class."""

    def __init__(self, name: str, average_grade: float, credit_points: int):
        """Constructor."""
        self.credit_points = credit_points
        self.average_grade = average_grade
        self.name = name


def create_student(name: str, grades: list, credit_points: int) -> Student:
    """
    Create a new student where average grade is the average of the grades in the list.

    Round the average grade up to three decimal places.
    If the list of grades is empty, the average grade will be 0.
    """
    try:
        average = sum(grades) / len(grades)
    except ZeroDivisionError:
        average = 0
    return Student(name, average, credit_points)


def get_top_student_with_credit_points(students: list, min_credit_points: int):
    """
    Return the student with the highest average grade who has enough credit points.

    If there are no students with enough credit points, return None.
    If several students have the same average score, return the first.
    """
    top = max(students, key=lambda x: x.average_grade)
    if top.average_grade > min_credit_points:
        return top
    return None


def add_result_to_student(student: Student, grades_count: int, new_grade: int, credit_points) -> Student:
    """
    Update student average grade and credit points by adding a new grade (result).

    As the student object does not have grades count information, it is provided in this function.
    average grade = sum of grades / count of grades

    With the formula above, we can deduct:
    sum of grades = average grade * count of grades

    The student has the average grade, function parameters give the count of grades.
    If the sum of grades is known, a new grade can be added and a new average can be calculated.
    The new average grade must be rounded to three decimal places.
    Given credits points should be added to old credit points.

    Example1:
        current average (from student object) = 4
        grades_count (from parameter) = 2
        so, the sum is 2 * 4 = 8
        new grade (from parameter) = 5
        new average = (8 + 5) / 3 = 4.333
        The student object has to be updated with the new average

    Example2:
        current average = 0
        grades_count = 0
        calculated sum = 0 * 0 = 0
        new grade = 4
        new average = 4 / 1 = 4

    Return the modified student object.
    """
    sum = grades_count * student.average_grade
    average = (sum + new_grade) / (grades_count + 1)
    student.average_grade = average
    student.credit_points += credit_points
    return student


def get_ordered_students(students: list) -> list:
    """
    Return a new sorted list of students by (down).

    credit points (higher first), average_grade (higher first), name (a to z).
    """
    students = sorted(students, key=lambda x: x.name)
    students = sorted(students, key=lambda x: x.average_grade, reverse=True)
    students = sorted(students, key=lambda x: x.credit_points, reverse=True)
    return students


class Room:
    """Room."""

    def __init__(self, number: int, price: int):
        """Constructor."""
        self.number = number
        self.price = price
        self.features = []
        self.booked = False

    def add_feature(self, feature: str) -> bool:
        """
        Add a feature to the room.

        Do not add the feature and return False if:
        - the room already has that feature
        - the room is booked.
        Otherwise, add the feature to the room and return True
        """
        if feature in self.features or self.booked:
            return False
        self.features.append(feature)

    def get_features(self) -> list:
        """Return all the features of the room."""
        pass

    def get_price(self) -> int:
        """Return the price."""
        return self.price

    def get_number(self) -> int:
        """Return the room number."""
        return self.number


class Hotel:
    """Hotel."""

    def __init__(self):
        """Constructor."""
        self.rooms = []

    def add_room(self, room: Room) -> bool:
        """
        Add room to hotel.

        If a room with the given number already exists, do not add a room and return False.
        Otherwise add the room to hotel and return True.
        """
        for i in self.rooms:
            if i.number == room.number:
                return False
        self.rooms.append(room)
        return True

    def book_room(self, required_features: list) -> Optional[Room]:
        """
        Book an available room which has the most matching features.

        Find a room which has most of the required features.
        If there are several with the same amount of matching features, return the one with the smallest room number.
        If there is no available rooms, return None
        """
        holder = Room(100000, 0)
        number = - 1
        for room in self.get_available_rooms():
            n_of_features = len(set(room.features) & set(required_features))
            if n_of_features >= number:
                number = n_of_features
                if holder.number > room.number:
                    holder = room
        if holder.price:
            holder.booked = True
            return holder
        return None

    def get_available_rooms(self) -> list:
        """Return a list of available (not booked) rooms."""
        available = []
        for room in self.rooms:
            if not room.booked:
                available.append(room)
        return available

    def get_rooms(self) -> list:
        """Return all the rooms (both booked and available)."""
        return self.rooms

    def get_booked_rooms(self) -> list:
        """Return all the booked rooms."""
        booked = []
        for room in self.rooms:
            if room.booked:
                booked.append(room)
        return booked

    def get_feature_profits(self) -> dict:
        """
        Return a dict where key is a feature and value is the total price for the booked rooms which have the feature.

        Example:
            room1, price=100, features=a, b, c
            room2, price=200, features=b, c, d
            room3, price=400, features=a, c

        all the rooms are booked
        result:
        {
        'a': 500,
        'b': 300,
        'c': 700,
        'd': 200
        }
        """
        price_list = {}
        for room in self.rooms:
            for feature in room.features:
                if feature in price_list:
                    price_list[feature] += room.price
                else:
                    price_list[feature] = room.price
        return price_list

    def get_most_profitable_feature(self) -> Optional[str]:
        """
        Return the feature which profits the most.

        Use get_feature_profits() method to get the total price for every feature.
        Return the feature which has the highest value (profit).
        If there are several with the same max value, return the feature which is alphabetically lower (a < z)
        If there are no features booked, return None.
        """
        if self.get_feature_profits():
            price = max(self.get_feature_profits().items(), key=lambda x: x[1])[0]
            return price
        return None


if __name__ == '__main__':
    print(get_names_from_results("ago 123,peeter 11", 0))
    print(get_names_from_results("ago 123,peeter 11,33", 10))
    print(get_names_from_results("ago 123,peeter 11", 100))
    print(get_names_from_results("ago 123,peeter 11,kitty11!! 33", 11))
    print(get_names_from_results("ago 123,peeter 11,kusti riin 14", 12))
    print(tic_tac_toe([[1, 0, 0], [1, 1, 2], [0, 2, 2]]))
    print(longest_substring('babcdEFghij'))
    hotel = Hotel()
    room1 = Room(1, 100)
    room1.add_feature("tv")
    room1.add_feature("bed")
    room2 = Room(2, 200)
    room2.add_feature("tv")
    room2.add_feature("sauna")
    hotel.add_room(room1)
    hotel.add_room(room2)
    hotel.add_room(Room(1, 150))
    room2.add_feature('tv')
    assert hotel.get_rooms() == [room1, room2]
    assert hotel.get_booked_rooms() == []

    assert hotel.book_room(["tv", "president"]) == room1
    assert hotel.get_available_rooms() == [room2]
    assert hotel.get_booked_rooms() == [room1]
    assert hotel.book_room([]) == room2
    assert hotel.get_available_rooms() == []
    room3 = Room(3, 100)
    hotel.add_room(room3)
    room3.add_feature('sauna')
    assert hotel.get_feature_profits() == {
        'tv': 300,
        'bed': 100,
        'sauna': 300
    }
    assert hotel.get_most_profitable_feature() == 'tv'
