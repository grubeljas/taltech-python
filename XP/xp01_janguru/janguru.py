"""This program is insane."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    """It is hard explain but it doesnt really matter."""
    if (pos1 > pos2) and (jump_distance1/sleep1 > jump_distance1/sleep1):
        return -1
    elif (pos2 > pos1) and (jump_distance2/sleep2 > jump_distance1/sleep1):
        return -1
    elif sleep1 == sleep2 and pos1 != pos2 and jump_distance1 == jump_distance2:
        return -1
    time = 0
    while True:
        a = time // sleep1 + 1
        b = time // sleep2 + 1
        distance1 = pos1 + a * jump_distance1
        distance2 = pos2 + b * jump_distance2
        if distance1 == distance2:
            return distance1
        time += 1
    

"""
time = (pos2-pos1)/((jump_distance1 / sleep1)-(jump_distance2 / sleep2))
        a = time // sleep1 + 1
        b = time // sleep2 + 1
        distance1 = pos1 + a * jump_distance1
        distance2 = pos2 + b * jump_distance2
        print("soooo" + str(time//sleep1))
        print(time//sleep2)
        print(distance1)
        print(distance2)
        if distance1 == distance2 :
            return int(distance1)
        else:
            if sleep1 >= sleep2:
                sleep = sleep1
            else:
                sleep = sleep2
            time = time - 5*sleep
            while time < time + 5*sleep:
                a = time // sleep1 + 1
                b = time // sleep2 + 1
                distance1 = pos1 + a * jump_distance1
                distance2 = pos2 + b * jump_distance2
                if distance1 == distance2:
                    return distance1
                time += sleep1
                a = time // sleep1 + 1
                b = time // sleep2 + 1
                distance1 = pos1 + a * jump_distance1
                distance2 = pos2 + b * jump_distance2
                if distance1 == distance2:
                    return distance1
                time += sleep2-sleep1
            else:
                return -1
"""
