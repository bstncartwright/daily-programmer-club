def num_jewels_and_stones(J: str, S: str) -> int:
    mirror = []
    for i in J:
        if i not in mirror:
            mirror.append(i)

    count = 0
    for letter in mirror:
        for other_letter in S:
            if letter == other_letter:
                count += 1
    return count

# Jonathan is learning about Git! :)