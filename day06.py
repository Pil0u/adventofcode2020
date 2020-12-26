def result(input_):
    groups_p1 = []
    current_p1 = set()

    groups_p2 = []
    current_p2 = set('azertyuiopqsdfghjklmwxcvbn')

    for passenger in input_:
        if passenger == '':
            groups_p1.append(current_p1)
            current_p1 = set()

            groups_p2.append(current_p2)
            current_p2 = set('azertyuiopqsdfghjklmwxcvbn')

            continue

        current_p1 = current_p1.union(set(passenger))
        current_p2 = current_p2.intersection(set(passenger))

    groups_p1.append(current_p1)
    groups_p2.append(current_p2)

    part_one = sum([len(g) for g in groups_p1])
    part_two = sum([len(g) for g in groups_p2])

    return part_one, part_two
