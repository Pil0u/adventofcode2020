from copy import deepcopy

def boot(seq):
    index = 0
    played_indices = set()

    acc = 0

    while True:
        if index == len(seq):
            return True, acc

        if index in played_indices:
            return False, acc

        played_indices.add(index)

        line = seq[index].split()
        op = line[0]
        value = int(line[1])

        if op == 'nop':
            index += 1

        if op == 'acc':
            acc += value
            index += 1

        if op == 'jmp':
            index += value

def generate_sequences(list_):
    all_seqs = []

    for idx, value in enumerate(list_):

        if value[:3] == 'nop':
            seq = deepcopy(list_)
            seq[idx] = 'jmp' + value[3:]
            all_seqs.append(seq)

        if value[:3] == 'jmp':
            seq = deepcopy(list_)
            seq[idx] = 'nop' + value[3:]
            all_seqs.append(seq)

    return all_seqs


def result(input_):
    # Part 1
    part_one = boot(input_)[1]

    # Part 2
    all_sequences = generate_sequences(input_)
    for sequence in all_sequences:
        result = boot(sequence)
        
        if result[0] is not False:
            part_two = result[1]
            break

    return part_one, part_two
