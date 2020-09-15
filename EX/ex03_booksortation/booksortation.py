"""Booksortation."""


def booksortation(books: list) -> dict:
    """
    Given a list of books (strings). Your task is to categorize and sort them.

    There are five books categories: spell books, history books, relics books, potion books and other books.

    If a book doesn't belong to any named categories, it goes to 'other books' category.

    However, if one book belongs to multiple categories, they should appear in only one
    (starting from up, whichever occurs first).

    :param books: given books as a list, list contains of strings
    :return: categorised and sorted books as a dict, where keys are categories and values are
    list of books that match this category. Lists should be sorted alphabetically.
    """
    pass


def add_book_to_category(book: str, category: str, categorised_books: dict) -> dict:
    """

    :param book:
    :param category:
    :param categorised_books:
    :return:
    """
    pass


def is_spell_book(book: str) -> bool:
    """
    Book is a spell book if its title starts with '*' (a star, without quotes) and ends with '*' (a star, no quotes).

    However, if the starting and ending star is the same star, it is not a spell book.

    For example: '*The Horrible Spells*' is a spell book.

    :param book: given book as a string
    :return: True if given book is a spell book, False otherwise
    """
    if book[0] == "*" and book[-1] == "*":
        return True
    else:
        return False


def is_history_book(book: str) -> bool:
    """
    Book is a history book if its title matches the pattern where each new word starts with a capital letter.

    Word is considered anything after a whitespace.

    For example: 'The Mighty King' and 'The Age Of The Wonderbolts' are both history books.
    Then again, 'the Ugly Duckling' isn't a history books because the word 'the' doesn't start with a capital letter.

    :param book: given book as a string
    :return: True if given book is a history book, False otherwise
    """
    list = book.split()
    for word in list:
        if word[0].isupper():
            pass
        else:
            return False
    return True


def is_relics_book(book: str) -> bool:
    """
    Book is a relics book if its title matches the uppercase-lowercase-uppercase-lowercase... pattern.

    It can start from both upper- and lowercase letters.
    PS! Pay attention to whitespaces.

    For example: 'ThE StAfF' and 'rAiNiNg dUmPlInGs' are both relics books.
    However 'ThE sTaFf' and 'rAiNiNg DuMpLiNgS' are not relics books.

    :param book: given book as a string
    :return: True if given book is a relics book, False otherwise
    """
    if book[0].islower():
        book = book[1:]
    for i in book[::2]:
        if i.isalpha():
            if i.isupper():
                pass
            else:
                return False
        else:
            pass
    for i in book[1::2]:
        if i.isalpha():
            if i.islower():
                pass
            else:
                return False
        else:
            pass
    return True


def is_potion_book(book: str) -> bool:
    """
    Book is a potion book if its title contains the same amount of vowels and consonants or the amount differs by one.

    However, it may contain as many symbols as it likes.

    The vowels are a, e, i, o, u.
    The consonants are b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, x, z, w, y.

    For example: 'The Banana Juice' is a potion book (7 vowels, 7 consonants)
    and so is 'The tomato potion' (7 vowels, 8 consonants -> differ by 1).
    However, 'The Green Liquid' isn't a potion book (6 vowels, 8 consonants -> differ by 2).

    :param book: given book as a string
    :return: True if given book is a potion book, False otherwise
    """
    book = book.lower()
    vowels = ["a", "e", "i", "o", "u"]
    consonants =['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'w', 'y']
    v = 0
    c = 0
    for i in book:
        if i in vowels:
            v += 1
        elif i in consonants:
            c += 1
        else:
            pass
    if c == v or c+1 == v or c-1 == v:
        return True
    else:
        return False






if __name__ == '__main__':
    # All True.
    print(is_spell_book('*kana*'))
    print(is_history_book('This Is A History Book'))
    print(is_relics_book('ThE StAfF'))
    print(is_potion_book('The Banana Juice'))
