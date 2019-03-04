def is_valid_walk(walk):
    # walk = []
    x, y = 0, 0

    for i in walk:
        if i is 'n':
            y += 1
        if i is 's':
            y -= 1
        if i is 'w':
            x += 1
        if i is 'e':
            x -= 1

    if x is not 0:
        return False

    if y is not 0:
        return False

    if len(walk) is not 10:
        return False

    return True

def is_valid_walk_short(walk):
    return len(walk) == 10 and walk.count('n') == walk.count('s') and walk.count('e') == walk.count('w')
    
