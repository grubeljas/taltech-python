"""Booksortation."""


def booksortation(books: list) -> dict:
    """
    Give a list of books (strings). Your task is to categorize and sort them.

    There are five books categories: spell books, history books, relics books, potion books and other books.

    If a book doesn't belong to any named categories, it goes to 'other books' category.

    However, if one book belongs to multiple categories, they should appear in only one
    (starting from up, whichever occurs first).

    :param books: given books as a list, list contains of strings
    :return: categorised and sorted books as a dict, where keys are categories and values are
    list of books that match this category. Lists should be sorted alphabetically.
    """
    categor_books = {}
    for book in books:
        if is_spell_book(book):
            add_book_to_category(book, "spell books", categor_books)
        elif is_history_book(book):
            add_book_to_category(book, "history books", categor_books)
        elif is_relics_book(book):
            add_book_to_category(book, "relics books", categor_books)
        elif is_potion_book(book):
            add_book_to_category(book, "potion books", categor_books)
        else:
            add_book_to_category(book, "other books", categor_books)
    for category in categor_books:
        categor_books[category].sort()
    return categor_books


def add_book_to_category(book: str, category: str, categorised_books: dict) -> dict:
    """
    Add book to category.

    :param book:
    :param category:
    :param categorised_books:
    :return:
    """
    if category in categorised_books:
        categorised_books[category].append(book)
    else:
        categorised_books[category] = [book]
    return categorised_books


def is_spell_book(book: str) -> bool:
    """
    Book is a spell book if its title starts with '*' (a star, without quotes) and ends with '*' (a star, no quotes).

    However, if the starting and ending star is the same star, it is not a spell book.

    For example: '*The Horrible Spells*' is a spell book.

    :param book: given book as a string
    :return: True if given book is a spell book, False otherwise
    """
    if book.startswith("*") and book.endswith("*") and len(book) > 1:
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
    if book.isnumeric() or not book.isalnum():
        return True
    books = book.split()
    for word in books:
        if word[0].isalpha():
            if word[0].isupper():
                pass
            else:
                return False
        elif word[0].isascii():
            try:
                if word[1].isupper():
                    pass
                else:
                    return False
            except IndexError:
                pass

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
    if book == "":
        return True
    if book[0].islower():
        book = book[1:]
    for i in book[::2]:
        if i.isalpha():
            if not i.isupper():
                return False
    for i in book[1::2]:
        if i.isalpha():
            if not i.islower():
                return True
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
    cons = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'x', 'z', 'w', 'y']
    v = 0
    c = 0
    for i in book:
        if i in vowels:
            v += 1
        elif i in cons:
            c += 1
        else:
            pass
    if c == v or c + 1 == v or c - 1 == v:
        return True
    else:
        return False

print("======must return True:========")
print(is_spell_book('*kana*'))
print(is_history_book('This Is A History Book'))
print(is_history_book("6419(!/)/(!#="))
print(is_history_book("*A History Book"))
print(is_history_book("*"))
print(is_history_book("1234"))
print(is_history_book(""))  # => True
print(is_relics_book('ThE StAfF'))
print(is_relics_book("rAiNiNg dUmPlInGs"))
print(is_relics_book("6419(!/)/(!#="))
print(is_relics_book("A"))
print(is_relics_book(""))
print(is_relics_book(""))  # => True
print(is_potion_book('The Banana Juice'))
print(is_potion_book('The tomato potion'))
print(is_potion_book(""))  # => True
print("======must return False:========")
print(is_spell_book(""))  # => False
print(is_potion_book('The Green Liquid'))  # False
print(is_relics_book("ThAt  s*tAfF")) # False
print(is_relics_book("ThAt  sTaFf")) # False
print(is_relics_book("ThE sTaFf"))  # False
print(is_relics_book("rAiNiNg DuMpLiNgS"))  # False
