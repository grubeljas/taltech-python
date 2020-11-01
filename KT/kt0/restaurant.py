"""Restaurant system."""


class Restaurant:
    """Restaurant."""

    def __init__(self, name: str):
        """Restaurant constructor."""
        self.name = name
        self.menus = []

    def add_dish(self, dish: 'Dish') -> bool:
        """Add a dish if not already in restaurant."""
        return self.menus[0].add_dish(dish)

    def get_dishes(self) -> list:
        """Return all the dishes in the restaurant."""
        dishes = []
        for menu in self.menus:
            for dish in menu.food:
                dishes.append(dish)
        return dishes

    def add_menu(self, menu: 'Menu') -> bool:
        """
        Add a menu to the restaurant if all the dishes are available.

        Menu cannot be added if:
        - it has no dishes
        - the menu with the same dishes (in any order) already exists
        """
        if not menu.food:
            return False
        for menuu in self.menus:
            if menuu.compare_to(menu):
                return False
        else:
            self.menus.append(menu)
            return True

    def get_menus(self) -> list:
        """Return all the menus in the restaurant."""
        return self.menus

    def get_dishes_available_in_menu(self) -> list:
        """Return unique dishes which are in one of the menues."""
        unique = list(set(self.get_dishes()))
        return unique

    def get_menus_ordered_by_price(self) -> list:
        """A new list of menus ordered by total price (highest first), then by dish count (lower first)."""
        menus = sorted(self.menus, key=lambda x: len(x.food))
        menus = sorted(menus, key=lambda x: x.count_price(), reverse=True)
        return menus


class Dish:
    """Dish (food)."""

    def __init__(self, name: str, price: int):
        """Dish constructor."""
        self._name = name
        self.price = price

    def get_name(self) -> str:
        """Return the name of the dish."""
        return self._name

    def get_price(self) -> int:
        """Return the price of the dish."""
        return self.price


class Menu:
    """Menu which holds different dishes."""

    def __init__(self):
        """Menu constructor."""
        self.food = []

    def add_dish(self, dish: Dish) -> bool:
        """Add dish to menu if it does not exist already."""
        if dish in self.food:
            return False
        else:
            self.food.append(dish)
            return True

    def get_dishes(self) -> list:
        """Return all the dishes in menu."""
        return self.food

    def count_price(self):
        """Count price of all dishes."""
        count = 0
        for dish in self.food:
            count += dish.price
        return count

    def compare_to(self, menu: 'Menu') -> bool:
        """
        Compare the current menu with the given menu.

        Menus are the same if:
        - they have the same dishes (instances)
        - they have the same dishes (name-price are the same)
        - the order is not important (menu A,B is the same as B,A)
        If the menus are the same, return True. Oterhwise False.
        """
        if set(self.food) == set(menu.food):
            return True
        else:
            return False
