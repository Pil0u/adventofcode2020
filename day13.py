def prod(iterable):
    p = 1
    for n in iterable:
        p *= n
    return p


def result(input_):

    # Part 1
    my_timestamp = int(input_[0])
    bus_ids = [int(value) for value in input_[1].split(',') if value != 'x']
    waiting_times = {}

    for bus_id in bus_ids:
        waiting_times[bus_id] = bus_id - (my_timestamp % bus_id)

    part_one = min(waiting_times, key=waiting_times.get) * min(waiting_times.values())

    # Part 2
    bus_ids = input_[1].split(',')

    step = 1
    timestamp = 1

    # Store busses with respective index in initial list, ignoring 'x'.
    indexed_busses = [[idx, int(bus_id)] for idx, bus_id in enumerate(bus_ids) if bus_id != 'x']

    # Visual explanation of how this works: https://streamable.com/tojflp
    for index, indexed_bus in enumerate(indexed_busses):
        busses_to_check = indexed_busses[:index+1]

        valid = [(timestamp + bus_to_check[0]) % int(bus_to_check[1]) == 0 for bus_to_check in busses_to_check]

        while not all(valid):
            timestamp += step
            valid = [(timestamp + bus_to_check[0]) % int(bus_to_check[1]) == 0 for bus_to_check in busses_to_check]
            # Uncomment this to visualize iterations
            # print(f"{timestamp} / {valid}")

        step = prod([bus[1] for bus in busses_to_check])

    part_two = timestamp

    return part_one, part_two
