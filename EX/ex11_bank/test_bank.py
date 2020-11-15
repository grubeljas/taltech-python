import pytest
from bank import PersonError, TransactionError, Person, Bank, Transaction, Account


p1 = Person('Pavel', 'Grub', 10)

print(p1)
a = 'Pavel Grub'


def test_person():
    assert p1.__repr__() == 'Pavel Grub'
