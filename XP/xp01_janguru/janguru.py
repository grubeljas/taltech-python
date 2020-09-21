"""This program is insane."""


def meet_me(pos1, jump_distance1, sleep1, pos2, jump_distance2, sleep2) -> int:
    """Do hard explain but it doesnt really matter."""
    if (pos1 > pos2) and (jump_distance1/sleep1 > jump_distance1/sleep1):
        return -1
    elif (pos2 > pos1) and (jump_distance2/sleep2 > jump_distance1/sleep1):
        return -1
    elif sleep1 == sleep2 and pos1 != pos2 and jump_distance1 == jump_distance2:
        return -1
    if pos1 < 1000 and pos2 < 1000 and jump_distance1 < 100 and jump_distance2 < 100 and sleep1 < 100 and sleep2 < 100:
        time = 0
        while time < 1000000:
            a = time // sleep1 + 1
            b = time // sleep2 + 1
            distance1 = pos1 + a * jump_distance1
            distance2 = pos2 + b * jump_distance2
            if distance1 == distance2:
                return distance1
            time += 1
    else:
        if sleep1 > sleep2:
            sleep1, sleep2 = sleep2, sleep1
            jump_distance1, jump_distance2 = jump_distance2, jump_distance1
            pos1, pos2 = pos2, pos1
        time = 0
        kord = sleep2 // sleep1
        jaak = sleep2 % sleep1
        a = jump_distance1 / sleep1
        b = jump_distance2 / sleep2
        distance1 = int(a * time + pos1 + jump_distance1 - (time % sleep1 * a))
        distance2 = int(b * time + pos2 + jump_distance2 - (time % sleep2 * b))
        if distance1 == distance2:
            return distance1
        while time < 1000000000000:
            for i in range(kord):
                time += sleep1
                a = jump_distance1 / sleep1
                b = jump_distance2 / sleep2
                distance1 = int(a * time + pos1 + jump_distance1 - (time % sleep1 * a))
                distance2 = int(b * time + pos2 + jump_distance2 - (time % sleep2 * b))
                if distance1 == distance2:
                    return distance1
            time += jaak
            a = jump_distance1 / sleep1
            b = jump_distance2 / sleep2
            distance1 = int(a * time + pos1 + jump_distance1 - (time % sleep1 * a))
            distance2 = int(b * time + pos2 + jump_distance2 - (time % sleep2 * b))
            if distance1 == distance2:
                return distance1
        else:
            return -1
    
