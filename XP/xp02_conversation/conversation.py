"""Finding guessed number."""
import re
import math as m


class Student:
    def __init__(self, biggest_number: int):
        """
        Constructor.

        save biggest number into a variable that is attainable later on.
        Create a collection of all possible results [possible_answers] <- dont rename that (can be a list or a set)
        :param biggest_number: biggest possible number(inclusive) to guess
        NB: calculating using sets is much faster compared to lists
        """
        self.possible_answers = set([all_possible_answers for all_possible_answers in range(biggest_number + 1)])

    def decision_branch(self, sentence: str):
        """
        Regex can and should be used here.

        :param sentence: sentence to solve
        call one of the functions bellow (within this class) and return either one of the following strings:
        f"Possible answers are {sorted_list_of_possible_answers_in_growing_sequence)}." if there are multiple
        f"The number I needed to guess was {final_answer}." if the result is certain
        """
        pass

    def intersect_possible_answers(self, update: list):
        """
        Logical AND between two sets.

        :param update: new list to be put into conjunction with self.possible_answers
        conjunction between self.possible_answers and update
        https://en.wikipedia.org/wiki/Logical_conjunction
        """
        pass

    def exclude_possible_answers(self, update: list):
        """
        Logical SUBTRACTION between two sets.

        :param update: new list to be excluded from self.possible_answers
        update excluded from self.possible_answers
        """
        pass

    def deal_with_number_of_zeroes(self, amount_of_zeroes: int):
        """
        Filter possible_answers to match the amount of zeroes in its binary form.

        :param amount_of_zeroes: number of zeroes in the correct number's binary form
        """
        pass

    def deal_with_number_of_ones(self, amount_of_ones: int):
        """
        Filter possible answers to match the amount of ones in its binary form.

        :param amount_of_ones: number of zeroes in the correct number's binary form
        """
        pass

    def deal_with_primes(self, is_prime: bool):
        """
        Filter possible answers to either keep or remove all primes.

        Call find_primes_in_range to get all composite numbers in range.
        :param is_prime: boolean whether the number is prime or not
        """
        pass

    def deal_with_composites(self, is_composite: bool):
        """
        Filter possible answers to either keep or remove all composites.

        Call find_composites_in_range to get all composite numbers in range.
        :param is_composite: boolean whether the number is composite or not
        """
        pass

    def deal_with_dec_value(self, decimal_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param decimal_value: decimal value within the number like 9 in 192
        """
        pass

    def deal_with_hex_value(self, hex_value: str):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        :param hex_value: hex value within the number like e in fe2
        """
        pass

    def deal_with_quadratic_equation(self, equation: str, to_multiply: bool, multiplicative: float, is_bigger: bool):
        """
        Filter possible answers to remove all numbers that doesn't have the decimal_value in them.

        Regex can be used here.
        Call quadratic_equation_solver with variables a, b, c.
        deal_with_dec_value should be called.
        :param equation: the quadratic equation
        :param to_multiply: whether it is necessary to multiply or divide with a given multiplicative
        :param multiplicative: the multiplicative to multiply or divide with
        :param is_bigger: to use the bigger or smaller result of the quadratic equation(min or max from [x1, x2])
        """
        pass

    def deal_with_fibonacci_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all fibonacci numbers.

        Call find_fibonacci_numbers to get all fibonacci numbers in range.
        :param is_in: boolean whether the number is in fibonacci sequence or not
        """
        pass

    def deal_with_catalan_sequence(self, is_in: bool):
        """
        Filter possible answers to either keep or remove all catalan numbers.

        Call find_catalan_numbers to get all catalan numbers in range.
        :param is_in: boolean whether the number is in catalan sequence or not
        """
        pass

    def deal_with_number_order(self, increasing: bool, to_be: bool):
        """
        Filter possible answers to either keep or remove all numbers with wrong order.

        :param increasing: boolean whether to check is in increasing or decreasing order
        :param to_be: boolean whether the number is indeed in that order
        """
        pass


def normalize_quadratic_equation(equation: str):
    """
    Normalize the quadratic equation.

    normalize_quadratic_equation("x2 + 2x = 3") => "x2 + 2x - 3 = 0"
    normalize_quadratic_equation("0 = 3 + 1x2") => "x2 + 3 = 0"
    normalize_quadratic_equation("2x + 2 = 2x2") => "2x2 - 2x - 2 = 0"
    normalize_quadratic_equation("0x2 - 2x = 1") => "2x + 1 = 0"
    normalize_quadratic_equation("2x2 + 3x - 4 + 0x2 - x1 + 0x1 + 12 - 12x2 = 4x2 + x1 - 2") => "14x2 - x - 10 = 0"

    :param equation: quadratic equation to be normalized
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return: normalized equation
    """
    a = 0
    b = 0
    c = 0
    ax2 = r"([\+-]?)\s?(\d*)x2"
    bx1 = r"([\+-]?)\s?(\d*)x1*\b"
    cx0 = r"([\+-])\s?\b(\d+)\b"
    equation = equation.split("=")
    equation[1] = equation_swapper(equation[1])
    equation = equation[0] + equation[1]
    matcha = re.search(ax2, equation)
    matchb = re.search(bx1, equation)
    matchc = re.search(cx0, equation)
    if matcha:
        regex_a = re.findall(ax2, equation)
        for i in regex_a:
            if i[0] != "-":
                if i[1] == "":
                    a += 1
                else:
                    a += int(i[1])
            else:
                if i[1] == "":
                    a -= 1
                else:
                    a -= int(i[1])
    if matchb:
        regex_b = re.findall(bx1, equation)
        for i in regex_b:
            if i[0] != "-":
                if i[1] == "":
                    b += 1
                else:
                    b += int(i[1])
            else:
                if i[1] == "":
                    b -= 1
                else:
                    b -= int(i[1])
    if matchc:
        regex_c = re.findall(cx0, equation)
        for i in regex_c:
            if i[0] != "-":
                c += int(i[1])
            else:
                c -= int(i[1])
    if a < 0:
        a *= -1
        b *= -1
        c *= -1
    if a == 0:
        a = ""
    elif a == 1:
        a = "x2 "
    else:
        a = str(a) + "x2 "
    if b == 0:
        b = ""
    elif b == 1:
        b = "+ x "
    elif b == -1:
        b = "- x "
    else:
        b = str(b) + "x "
        if not b.startswith("-"):
            b = "+" + b
        b = str(b)[0] + " " + str(b)[1:]
    if c == 0:
        c = ""
    else:
        c = str(c)
        if not c.startswith("-"):
            c = "+" + c
        c = str(c)[0] + " " + str(c)[1:] + " "
    eq = f"{a}{b}{c}= 0"
    if eq.startswith("+"):
        eq = eq[2:]
    return eq


def equation_swapper(equation: str):
    """
    Swap symbols in equation.

    :param equation:
    :return:
    """
    equation = equation.replace("-", ".")
    equation = equation.replace("+", "-")
    equation = equation.replace(".", "+")
    if not equation.startswith("-"):
        equation = "-" + equation
    return equation


def quadratic_equation_solver(equation: str):
    """
    Solve the normalized quadratic equation.

    :param equation: quadratic equation
    https://en.wikipedia.org/wiki/Quadratic_formula
    :return:
    if there are no solutions, return None.
    if there is exactly 1 solution, return it.
    if there are 2 solutions, return them in a tuple, where smaller is first
    all numbers are returned as floats.
    """
    ax2 = r"(\d*)x2"
    bx1 = r"([\+-]?)\s?(\d*)x\b"
    cx0 = r"([\+-])\s(\d+)\b"
    matcha = re.search(ax2, equation)
    matchb = re.search(bx1, equation)
    matchc = re.search(cx0, equation)
    if matcha:
        a = matcha.group()[:-2]
        if a == "":
            a = 1
        a = int(a)
    else:
        a = 0
    if matchb:
        b = matchb.group()[:-1]
        if b == "- ":
            b = -1
        elif b == "+ ":
            b = +1
        else:
            b = int(b[0] + b[2:])
    else:
        b = 0
    if matchc:
        c = matchc.group()
        c = int(c[0] + c[2:])
    else:
        c = 0
    dicriminant = abs(b**2) - 4 * a * c
    if dicriminant < 0:
        return None
    elif dicriminant == 0:
        x = (- b) / (2 * a)
        return x
    elif dicriminant > 0:
        x1 = ((- b) - m.sqrt(dicriminant)) / (2 * a)
        x2 = ((- b) + m.sqrt(dicriminant)) / (2 * a)
        if x1 > x2:
            x1, x2 = x2, x1
        a = (x1, x2)
        return a


def find_primes_in_range(biggest_number: int):
    """
    Find all primes in range(end inclusive).

    :param biggest_number: all primes in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    :return: list of primes
    """
    primes = []
    for n in range(biggest_number):
        if n == 2:
            primes.append(n)
        elif n > 2:
            for p in primes:
                if n % p == 0:
                    continue
            primes.append(n)
    return primes


def find_composites_in_range(biggest_number: int):
    """
    Find all composites in range(end inclusive).

    Call find_primes_in_range from this method to get all composites
    :return: list of composites
    :param biggest_number: all composites in range of biggest_number(included)
    """
    primes = find_primes_in_range(biggest_number + 1)
    composites = []
    for n in range(2, biggest_number):
        if n not in primes:
            composites.append(n)
    return composites


def find_fibonacci_numbers(biggest_number: int):
    """
    Find all Fibonacci numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all fibonacci numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Fibonacci_number
    :return: list of fibonacci numbers
    """
    fibonacci = [0, 1]
    while True:
        n = fibonacci[-2] + fibonacci[-1]
        if n <= biggest_number:
            fibonacci.append(n)
        else:
            break
    return fibonacci


def find_catalan_numbers(biggest_number: int):
    """
    Find all Catalan numbers in range(end inclusive).

    Can be solved using recursion.
    :param biggest_number: all catalan numbers in range of biggest_number(included)
    https://en.wikipedia.org/wiki/Catalan_number
    :return: list of catalan numbers
    """
    catalan = []
    for n in range(1, biggest_number + 1):
        if n == 1:
            catalan.append(1)
        else:
            c = m.factorial(2 * n) / (m.factorial(n) * m.factorial(n + 1))
            catalan.append(int(c))
    return catalan
