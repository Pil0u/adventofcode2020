def result(input_):
    # Part 1
    position = [0, 0]
    direction = 90

    for todo in input_:
        action = todo[0]
        value = int(todo[1:])

        if action == 'F':
            if direction == 0:
                position[1] += value
            elif direction == 90:
                position[0] += value
            elif direction == 180:
                position[1] -= value
            elif direction == 270:
                position[0] -= value

        elif action == 'L':
            direction = (direction - value) % 360

        elif action == 'R':
            direction = (direction + value) % 360

        elif action == 'N':
            position[1] += value
        elif action == 'E':
            position[0] += value
        elif action == 'S':
            position[1] -= value
        elif action == 'W':
            position[0] -= value

    part_one = abs(position[0]) + abs(position[1])

    # Part 2
    position = [0, 0]
    waypoint = [10, 1]

    for todo in input_:
        action = todo[0]
        value = int(todo[1:])

        if action == 'F':
            position[0] += value * waypoint[0]
            position[1] += value * waypoint[1]

        elif action == 'N':
            waypoint[1] += value
        elif action == 'E':
            waypoint[0] += value
        elif action == 'S':
            waypoint[1] -= value
        elif action == 'W':
            waypoint[0] -= value

        else:
            if (action == 'R' and value == 90) or (action == 'L' and value == 270):
                waypoint = [waypoint[1], -waypoint[0]]
            elif (action == 'R' and value == 270) or (action == 'L' and value == 90):
                waypoint = [-waypoint[1], waypoint[0]]
            elif value == 180:
                waypoint = [-waypoint[0], -waypoint[1]]

    part_two = abs(position[0]) + abs(position[1])

    return part_one, part_two
