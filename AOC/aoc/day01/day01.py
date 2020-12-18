
def sum2020of2(n):
    while True:
        a = n.pop(0)
        for i in n:
            if a + i == 2020:
                return a * i


def sum2020of3(n):
    for c in range(len(n)):
        a = n.pop(0)
        for b in n:
            for j in n:
                if a + b + j == 2020:
                    return a * b * j


def readfile(ss):
    names = []
    with open(ss, encoding='utf-8') as file:
        for line in file:
            names.append(int(line.strip()))
    return names


print(sum2020of3([2018, 3, 2019, 5, 2000, 23, 16, 1994]))
print(readfile('ff.csv'))
print(sum2020of3(readfile('lol.txt')))
