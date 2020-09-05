"""Primes identifier."""


def is_prime_number(number: int):
    if (number == 0) or (number == 1):
        return False
    elif (number == 2) or (number == 3):
        return True
    else:
        for i in range(2, number - 1):
            if number % i == 0:
                break
                return False
            else:
                return True


if __name__ == '__main__':
    print(is_prime_number(2))  # -> True
    print(is_prime_number(3))  # -> True
    print(is_prime_number(1))  # -> True
    print(is_prime_number(4))  # -> False
    print(is_prime_number(7))
    print(is_prime_number(27))
