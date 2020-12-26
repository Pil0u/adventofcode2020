from itertools import combinations

def result(input_):
    input_ = [int(i) for i in input_]

    # Part 1
    for i, j in combinations(input_, 2):
        if i + j == 2020:
            part_one = i * j
            break

    # Part 2
    for i, j, k in combinations(input_, 3):
        if i + j + k == 2020:
            part_two = i * j * k
            break

    return (part_one, part_two)
