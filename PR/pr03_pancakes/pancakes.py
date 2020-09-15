"""Pancakes."""


def make_n_pancakes(n: int, ingredients: list) -> int:
    """
    Make n pancakes.

    If you can not make n pancakes, make as many as you can.
    If you can make more than n pancakes, do not make more. In that case make exactly n pancakes.

    Use the following functions here.
    Tip: the first step would be making dough.

    :param n: how many pancakes you have to make
    :param ingredients: given ingredients
    :return: amount of pancakes made
    """
    dough = make_dough(ingredients)
    dough = round(dough, 2)
    pancakes = 0
    if n > 30:
        needed_dough = n * 0.8
        if dough < needed_dough:
            pancakes = dough // 0.8
        else:
            pancakes = n
        return pancakes
    while can_make_pancake(dough) and pancakes < n:
        make_a_pancake(dough)
        pancakes += 1
        dough -= 0.8
    return pancakes


def make_dough(ingredients: list) -> int:
    """must always make as much dough as possible regardless of how many pancakes you are going to make.

    To make 7dl dough, it takes:
    One part egg, 5 parts milk, 4 parts flour, 1 part butter, 2 parts sugar.
    PS! It's a random recipe I made up, do not try to pancake according to this.

    :param ingredients: given ingredients as a list
    :return: dough made in dl
    """
    dough = 0
    empty = []
    ingreds_for_one_pancake = ["egg"] + ["milk"] * 5 + ["flour"] * 4 + ["butter"] + ["sugar"] * 2
    while ingredients != empty or ValueError:
        try:
            for i in ingreds_for_one_pancake:
                ingredients.remove(i)
            dough += 7
        except ValueError:
            break
    return dough


def can_make_pancake(dough: float) -> bool:
    """
    Make one pancake takes 0.8 dl pancake dough.

    Return True if you have enough dough to make a pancake, False otherwise.

    :param dough: pancake dough given in dl
    :return: boolean whether you have enough dough to make a pancake or not
    """
    if dough >= 0.8:
        return True
    else:
        return False


def make_a_pancake(dough: float) -> float:
    """
    Make a pancake. Making one pancake takes 0.8 dl dough.

    Round the remaining dough up to two decimal places.

    You do not have to implement the actual pancake making,
    you just have to return the amount of dough left after (hypothetically) making a pancake.

    :param dough: pancake dough given in dl
    :return: dough in dl after making a pancake
    """
    dough -= 0.8
    dough = round(dough, 2)
    return dough
