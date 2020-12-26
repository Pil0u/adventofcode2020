from itertools import product
import numpy

def star_neighbors(list_, i, j):
    n = len(list_)
    m = len(list_[0])

    neighbors = [n for n in product([-1, 0, 1], repeat=2) if n != (0, 0)]

    real_neighbors = []
    for neighbor in neighbors:
        new_i = i + neighbor[0]
        new_j = j + neighbor[1]

        if new_i % n == new_i and new_j % m == new_j:
            real_neighbors.append(list_[new_i][new_j])

    return real_neighbors

def line_star_neighbors(list_, i, j, stop_chars=['#', 'L']):
    n = len(list_)
    m = len(list_[0])

    neighbors = [n for n in product([-1, 0, 1], repeat=2) if n != (0, 0)]

    real_neighbors = []
    for neighbor in neighbors:
        new_i = i + neighbor[0]
        new_j = j + neighbor[1]

        while True:
            if new_i % n != new_i or new_j % m != new_j:
                break
            elif list_[new_i][new_j] in stop_chars:
                real_neighbors.append(list_[new_i][new_j])
                break

            new_i += neighbor[0]
            new_j += neighbor[1]

    return real_neighbors

def run(list_, func, requirement):
    old_mapping = None
    new_mapping = list_

    while new_mapping != old_mapping:

        old_mapping = new_mapping
        result = []

        for i in range(len(old_mapping)):
            for j in range(len(old_mapping[0])):
                myself = new_mapping[i][j]
                my_neighbors = func(old_mapping, i, j)

                if myself == 'L' and '#' not in my_neighbors:
                    result.append('#')
                elif myself == '#' and my_neighbors.count('#') >= requirement:
                    result.append('L')
                else:
                    result.append(myself)

        new_mapping = [''.join(row) for row in numpy.reshape(result, (len(old_mapping), len(old_mapping[0])))]

    return list(''.join(new_mapping)).count('#')


def result(input_):
    part_one = run(input_, star_neighbors, 4)
    part_two = run(input_, line_star_neighbors, 5)

    return part_one, part_two
