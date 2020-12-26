def prod(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p


def result(input_):
    input_ = sorted([0] + [int(i) for i in input_])

    # Part 1
    one_diff = 0
    three_diff = 0

    for idx, value in enumerate(input_):
        if idx == len(input_) - 1:
            next_ = max(input_) + 3
        else:
            next_ = input_[idx + 1]

        diff = next_ - value

        if diff == 1:
            one_diff += 1
        if diff == 3:
            three_diff += 1

    part_one = one_diff * three_diff

    # Part 2
    # The general idea for is to count the number of neighbors each adapter has, a neighbor being
    # an adapter that can be connected to the current value.
    # Ex: [1, 4, 5, 6, 7, 10, 11, 12, 15, 16, 19]
    #     1 has one neighbor (i.e. only one path is possible through it)
    #     4 has three neighbors (i.e. a crossroad of three paths through it)
    #     19 has one neighbor (the last adapter)
    #
    # We transform the list into a list of neighbors: [1, 3, 2, 1, 1, 2, 1, 1, 1, 1, 1]
    # then to a string '13211211111'.
    # From this string, because 1s represent unique paths, we keep the patterns between them:
    # '32' and '2' in our example.
    #
    # Each pattern represents N different paths, that we store in a dictionary.
    # Funny note, we can actually compute N if there was more different patterns.
    #     n=0  '2' -> 2 paths
    #     n=1  '32' -> 4 paths
    #     n=2  '332' -> 7 paths
    #     n=3  '3332' -> 13 paths = 2 + 4 + 7
    #     n=k  '33...332' -> u(n) = u(n-1) + u(n-2) + u(n-3)
    #
    # Multiplying them together gives the result.

    neighbors = []

    for idx, value in enumerate(input_):
        nb = 1
        for elem in input_[idx+2:idx+4]:
            if elem - value <= 3:
                nb += 1

        neighbors.append(nb)

    mapping = {
        '2': 2,
        '32': 4,
        '332': 7,
    }

    str_neighbors = ''.join([str(n) for n in neighbors])
    part_two = prod([mapping[i] for i in str_neighbors.split('1') if i != ''])

    return part_one, part_two
