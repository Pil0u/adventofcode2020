def result(input_):
    i_max, j_max = len(input_), len(input_[0])

    slopes = [[1, 1], [1, 3], [1, 5], [1, 7], [2, 1]]
    part_two = 1

    for slope in slopes:
        i, j = 0, 0
        trees = 0

        while i < i_max:
            if input_[i][j] == '#':
                trees += 1

            i += slope[0]
            j = (j + slope[1]) % j_max

        # Part 1
        if slope == [1, 3]:
            part_one = trees

        # Part 2
        part_two *= trees

    return part_one, part_two
