"""Bank."""
import datetime
import random


class PersonError(Exception):
    """Person error."""

    pass


class TransactionError(Exception):
    """Transaction error."""

    pass


class Person:
    """Person class."""

    def __init__(self, first_name: str, last_name: str, age: int):
        """
        Person constructor.

        :param first_name: first name
        :param last_name: last name
        :param age: age, must be greater than 0
        """
        self.first_name = first_name
        self.last_name = last_name
        if age <= 0:
            raise PersonError
        self._age = age
        self.bank_account = None

    @property
    def full_name(self) -> str:
        """Get person's full name. Combination of first and last name."""
        return f'{self.first_name} {self.last_name}'

    @property
    def age(self) -> int:
        """Get person's age."""
        return self._age

    @age.setter
    def age(self, value: int):
        """Set person's age. Must be greater than 0."""
        if value > 0:
            self._age = value
        else:
            raise PersonError

    def __repr__(self) -> str:
        """
        Person representation.

        :return: person's full name
        """
        return self.full_name


class Bank:
    """Bank class."""

    def __init__(self, name: str):
        """
        Bank constructor.

        :param name: name of the bank
        """
        self.name = name
        self.customers = []
        self.transactions = []

    def add_customer(self, person: Person) -> bool:
        """
        Add customer to bank.

        :param person: person object
        :return: was customer successfully added
        """
        if person not in self.customers:
            person.bank_account = Account(0.0, person, self)
            self.customers.append(person)
            return True
        else:
            return False

    def remove_customer(self, person: Person) -> bool:
        """
        Remove customer from bank.

        :param person: person object
        :return: was customer successfully removed
        """
        if person in self.customers:
            self.customers.remove(person)
            person.bank_account = None
            return True
        else:
            return False

    def __repr__(self) -> str:
        """
        Bank representation.

        :return: name of the bank
        """
        return self.name


class Transaction:
    """Transaction class."""

    def __init__(self, amount: float, date: datetime.date, sender_account: 'Account', receiver_account: 'Account',
                 is_from_atm: bool):
        """
        Transaction constructor.

        :param amount: value
        :param date: date of the transaction
        :param sender_account: sender's object
        :param receiver_account: receiver's object
        :param is_from_atm: is transaction from atm
        """
        self.amount = float(amount)
        self.date = date
        self.sender_account = sender_account
        self.receiver_account = receiver_account
        self.is_from_atm = is_from_atm

    def __repr__(self) -> str:
        """
        Transaction representation.

        :rtype: object's values displayed in a nice format
        """
        if self.is_from_atm:
            return f'({self.amount} €) ATM'
        else:
            return f'({self.amount} €) {self.sender_account.person} -> {self.receiver_account.person}'


def create_number():
    """Create random number for account."""
    ee = 'EE'
    for i in range(18):
        ee += str(random.randint(0, 9))
    return ee


class Account:
    """Account class."""

    def __init__(self, balance: float, person: Person, bank: 'Bank'):
        """
        Account constructor.

        :param balance: initial account balance
        :param person: person object
        :param bank: bank object
        """
        self._balance = balance
        self.person = person
        self.bank = bank
        self.number = create_number()
        self.transactions = []

    @property
    def balance(self) -> float:
        """Get account's balance."""
        return self._balance

    def deposit(self, amount: float, is_from_atm: bool = True):
        """Deposit money to account."""
        if amount <= 0:
            raise TransactionError
        elif is_from_atm:
            transaction = Transaction(amount, datetime.date.today(), self, self, is_from_atm)
            self.transactions.append(transaction)
            self.bank.transactions.append(transaction)
        self._balance += amount

    def withdraw(self, amount: float, is_from_atm: bool = True):
        """Withdraw money from account."""
        if amount <= 0 or amount > self._balance:
            raise TransactionError
        elif is_from_atm:
            transaction = Transaction(-amount, datetime.date.today(), self, self, is_from_atm)
            self.transactions.append(transaction)
            self.bank.transactions.append(transaction)
        self._balance -= amount

    def transfer(self, amount: float, receiver_account: 'Account'):
        """Transfer money from one account to another."""
        if self == receiver_account:
            raise TransactionError
        if self.bank == receiver_account.bank:
            if amount > self._balance:
                raise TransactionError
            self.withdraw(amount, is_from_atm=False)
            receiver_account.deposit(amount, is_from_atm=False)
            transaction = Transaction(amount, datetime.date.today(), self, receiver_account, False)
        else:
            if amount + 5 > self._balance:
                raise TransactionError
            self.withdraw(amount + 5, is_from_atm=False)
            receiver_account.deposit(amount, is_from_atm=False)
            transaction = Transaction(amount, datetime.date.today(), self, receiver_account, False)
            receiver_account.bank.transactions.append(transaction)
        self.bank.transactions.append(transaction)
        self.transactions.append(transaction)
        receiver_account.transactions.append(transaction)

    def account_statement(self, from_date: datetime.date, to_date: datetime.date) -> list:
        """All transactions in given period."""
        trans = []
        for transaction in self.transactions:
            if from_date <= transaction.date <= to_date:
                trans.append(transaction)
        return trans

    def get_debit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get total income in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: debit turnover number
        """
        turnover = 0
        for trans in self.account_statement(from_date, to_date):
            if trans.amount > 0 and trans.is_from_atm or trans.is_from_atm == False and self == trans.receiver_account:
                turnover += trans.amount
        return turnover

    def get_credit_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get total expenditure in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: credit turnover number
        """
        turnover = 0
        for trans in self.account_statement(from_date, to_date):
            if trans.amount < 0 or not trans.is_from_atm and self == trans.sender_account:
                turnover -= abs(trans.amount)
            if trans.sender_account.bank != trans.receiver_account.bank and self == trans.sender_account:
                turnover -= 5
        return turnover

    def get_net_turnover(self, from_date: datetime.date, to_date: datetime.date) -> float:
        """
        Get net turnover (income - costs) in given period.

        :param from_date: from date object (included)
        :param to_date: to date object (included)
        :return: net turnover number
        """
        a = self.get_debit_turnover(from_date, to_date)
        b = self.get_credit_turnover(from_date, to_date)
        return a + b

    def __repr__(self) -> str:
        """
        Account representation.

        :return: account number
        """
        return str(self.number)
