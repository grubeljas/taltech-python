"""EX15."""
import copy


class Statistics:
    """Class statistics."""

    def __init__(self, bad, nice, wish):
        self.bad = self.read_list(bad)
        self.nice = nice
        self.wish = wish

    def read_list(self, file):
        temp = []
        lines = open(file, 'r').read().split('\n')
        for element in lines:
            temp.append(Child(element))
        return temp


class Child:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name


if __name__ == '__main__':
    st = Statistics('ex15_naughty_list.csv', 'ex15_nice_list.csv', 'ex15_wish_list.csv')
    print(st.bad)
