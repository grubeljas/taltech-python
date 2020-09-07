
def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    time = 0
    limit = 1000
    if (pos1 or jump_distance1 or sleep1 or pos2 or jump_distance2 or sleep2) > 1000:
        limit = 999999999
    while time < limit:
        a = time // sleep1 + 1
        b = time // sleep2 + 1
        distance1 = pos1 + a * jump_distance1
        distance2 = pos2 + b * jump_distance2
        if distance1 == distance2:
            return distance1
        time += 1
    else:
        return -1
    

if __name__ == "__main__":
    print(str(meet_me(1, 2, 1, 2, 1, 1)) + " expected:  3")
    print(str(meet_me(1, 2, 1, 1, 2, 1)) + " expected:  3")
    print(str(meet_me(1, 2, 3, 4, 5, 5)) + " expected: -1")
    print(str(meet_me(10, 7, 7, 5, 8, 6)) + " expected: 45")
    print(str(meet_me(0, 2, 1, 2, 1, 1)) + " expected:  4")
    print(str(meet_me(1, 6, 1, 14, 5, 1)) + " expected: 79")
    print(str(meet_me(100, 7, 4, 300, 8, 6)) + " expected:940")
    print(str(meet_me(1, 7, 1, 15, 5, 1)) + " expected: 50")
    print(str(meet_me(0, 1, 1, 1, 1, 1)) + " expected: -1")
    print(str(meet_me(3, 5, 10, 4, 1, 2)) + " expected: 8")
    print(str(meet_me(1, 3, 2, 1, 2, 1)) + " expected: 7")
    print(str(meet_me(0, 15, 6, 5, 5, 3)) + " expected: 15")
    print(str(meet_me(100000, 21, 2, 0, 11, 1)) + " expected: 2200000")

