def parse_bags(input_):
    main = {}

    for line in input_:
        current_dict = {}

        sentence = line.split(' bags contain ')
        key = sentence[0]

        if sentence[1] == 'no other bags.':
            main[key] = current_dict
            continue

        for elem in sentence[1].split(', '):
            splitted = elem.split()
            bag_type = f"{splitted[1]} {splitted[2]}"
            current_dict[bag_type] = int(splitted[0])

        main[key] = current_dict

    return main

def get_containers(bag, all_bags):
    containers = set()

    for key, val in all_bags.items():
        if bag in val.keys():
            containers.add(key)

    return containers

def get_containees(bag_type, all_bags):
    entry = all_bags[bag_type]
    n_bags = sum(entry.values())

    for key, val in all_bags[bag_type].items():
        n_bags += get_containees(key, all_bags) * val

    return n_bags


def result(input_):
    bags = parse_bags(input_)

    gold_containers = set()
    tested_containers = {'shiny gold'}

    while tested_containers:
        new_containers = set()
        for container in tested_containers:
            new_containers = new_containers.union(get_containers(container, bags))

        gold_containers = gold_containers.union(new_containers)
        tested_containers = new_containers

    part_one = len(gold_containers)
    part_two = get_containees('shiny gold', bags)

    return part_one, part_two
