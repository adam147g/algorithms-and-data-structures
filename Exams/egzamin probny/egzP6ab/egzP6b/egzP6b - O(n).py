from egzP6btesty import runtests


def jump(M):
    x, y = 0, 0
    field_set = {(x, y): 1}
    # field_set.update({(f"({x}, {y})"): (x, y)})
    # field_set.update({(x, y): 1})
    for el in M:
        if el == 'UL':
            x, y = x - 1, y + 2
        elif el == 'UR':
            x, y = x + 1, y + 2
        elif el == 'RU':
            x, y = x + 2, y + 1
        elif el == 'RD':
            x, y = x + 2, y - 1
        elif el == 'DR':
            x, y = x + 1, y - 2
        elif el == 'DL':
            x, y = x - 1, y - 2
        elif el == 'LD':
            x, y = x - 2, y - 1
        elif el == 'LU':
            x, y = x - 2, y + 1
        '''
        # temp = field_set.get(f"({x}, {y})")
        temp = field_set.get((x, y))
        if temp:
            # field_set.pop(f"({x}, {y})")
            field_set.pop((x, y))
        else:
            # field_set.update({f"({x}, {y})": (x, y)})
            # field_set.update({(x, y): 1})
            field_set[(x, y)] = 1
        '''

        if (x, y) in field_set.keys():
            field_set.pop((x, y))
        else:
            field_set[(x, y)] = 1

    return len(field_set)
'''
    Poniżej trochę wolniejsze, ale nadal działające
    
        if (x, y) in field_set.keys():
            field_set[(x, y)] = (field_set[(x, y)] + 1) % 2
        else:
            field_set[(x, y)] = 1
    return sum(field_set.values())
'''

runtests(jump, all_tests=True)
