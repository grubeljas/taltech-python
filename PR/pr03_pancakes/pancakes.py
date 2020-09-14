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
    pancakes = 0
    dough = make_dough(ingredients)
    while can_make_pancake(dough) and pancakes < n:
        make_a_pancake(dough)
        pancakes += 1
    return pancakes


def make_dough(ingredients: list) -> int:
    """
    You must always make as much dough as possible regardless of how many pancakes you are going to make.

    To make 7dl dough, it takes:
    One part egg, 5 parts milk, 4 parts flour, 1 part butter, 2 parts sugar.
    PS! It's a random recipe I made up, do not try to pancake according to this.

    :param ingredients: given ingredients as a list
    :return: dough made in dl
    """
    dough = 0
    while ingredients is not None:
        try:
            ingredients.remove("egg")
            for milk in range(5):
                ingredients.remove("milk")
            for flour in range(4):
                ingredients.remove("flour")
            ingredients.remove("butter")
            ingredients.remove("sugar")
            ingredients.remove("sugar")
            dough += 7
        except ValueError:
            break
        finally:
            pass
    return dough


def can_make_pancake(dough: float) -> bool:
    """
    Making one pancake takes 0.8 dl pancake dough.

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
    return dough


if __name__ == '__main__':
    ingredients = ["egg"] + ["milk"] * 5 + ["flour"] * 4 \
                  + ["butter"] + ["sugar"]
    print(make_dough(ingredients))  # 0 -> not enough sugar.
    ingredients2 = ["egg"] * 4 + ["milk"] * 9 + ["flour"] * 14 \
                   + ["butter"] * 3 + ["sugar"] * 7
    print(make_dough(ingredients2))  # 7 -> can make 7dl dough not 7.x dl.
    ingredients3 = ["egg" for _ in range(3)] + ["milk" for _ in range(15)] + ["flour" for _ in range(7)] \
                   + ["butter" for _ in range(3)] + ["sugar" for _ in range(2)]
    print(make_n_pancakes(8, ingredients3))  # 8
    ingredients4 = ["egg" for _ in range(21)] + ["milk" for _ in range(45)] + ["flour" for _ in range(4)] \
                   + ["butter" for _ in range(14)] + ["sugar" for _ in range(12)]
    print(make_n_pancakes(4, ingredients4))  # 4 -> 7dl dough, 0.8dl per pancake -> could make 8 pancakes, we want 4
