"""Test for bank."""
import datetime
from bank import PersonError, TransactionError, Person, Bank, Transaction, Account


p1 = Person('Pavel', 'Bruh', 18)
p2 = Person('Ago', 'Loh', 40)
p3 = Person('Lolol', 'Kek', 69)
sw = Bank('Swedbank')
seb = Bank('SEB')


def test_person():
    """Test person."""
    assert p1.first_name == 'Pavel'
    assert p1.last_name == 'Bruh'
    assert p1.age == 18
    try:
        p3.age = 0
    except PersonError:
        pass
    p3.age = 40
    assert p3.age == 40
    assert p3.full_name == 'Lolol Kek'


def test_bank():
    """Test bank."""
    assert sw.name == 'Swedbank'
    sw.add_customer(p1)
    sw.add_customer(p2)
    sw.add_customer(p3)
    assert sw.add_customer(p1) is False
    assert sw.customers == [p1, p2, p3]
    sw.remove_customer(p2)
    assert sw.remove_customer(p2) is False
    assert sw.customers == [p1, p3]
    assert str(sw) == 'Swedbank'


def test_bank_account():
    """Test bank account."""
    ba1 = p1.bank_account
    seb.add_customer(p2)
    ba2 = p2.bank_account
    ba3 = p3.bank_account
    assert ba1.balance == 0.0
    assert ba1.person == p1
    assert ba1.bank == sw
    ba1.deposit(100.0)
    ba1.transfer(50.0, ba2)
    assert ba1.balance == 45.0
    assert ba2.balance == 50.0
    ba2.withdraw(10.0)
    assert len(ba2.transactions) == 2
    assert len(ba1.transactions) == 2
    assert str(ba1.transactions[0]) == '(100.0 €) ATM'
    ba1.transfer(10.0, ba3)
    assert str(ba3.transactions[0]) == '(10.0 €) Pavel Bruh -> Lolol Kek'
    assert len(ba1.account_statement(datetime.date.today(), datetime.date.today())) == 3
    assert ba1.get_net_turnover(datetime.date.today(), datetime.date.today()) == 35.0
