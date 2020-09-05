"""Primes identifier."""


def is_prime_number(number):
    if (number == 0) or (number == 1):
        return False
    elif number == 2:
        return True
    else:
        i = 2
        while number % i != 0:
            i += 1
            if i == number:
                return True
        else:
            return False


if __name__ == '__main__':
    print(is_prime_number(2))  # -> True
    print(is_prime_number(89))  # -> True
    print(is_prime_number(23))  # -> True
    print(is_prime_number(4))  # -> False
    print(is_prime_number(7))  # -> True
    print(is_prime_number(88))  # -> False
