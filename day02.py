def result(input_):
    input_ = [i.split(' ') for i in input_]

    part_one, part_two = 0, 0

    for combination in input_:
        min_, max_ = (int(i) for i in combination[0].split('-'))
        letter = combination[1][0]
        password = combination[2]
        occurrences = list(password).count(letter)

        # Part 1
        if occurrences >= min_ and occurrences <= max_:
            part_one += 1

        # Part 2
        if [password[min_-1], password[max_-1]].count(letter) == 1:
            part_two += 1

    return part_one, part_two
