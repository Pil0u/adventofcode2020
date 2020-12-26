from itertools import combinations, accumulate


def build_pairs(list_):
    result = set()
    
    for i, j in combinations(list_, 2):
        result.add(i + j)
        
    return result


def result(input_):
    input_ = [int(i) for i in input_]
    
    # Part 1
    for idx, value in enumerate(input_):
        preamble = input_[idx:25+idx]
        part_one = input_[25+idx]

        eligible = build_pairs(preamble)

        if part_one not in eligible:
            break
    
    # Part 2
    for new_idx, value in enumerate(input_[:idx+25]):
        sums_ = [i for i in accumulate(input_[new_idx:idx+25])]
        
        if part_one in sums_:
            end_range = new_idx + sums_.index(part_one) + 1
            contiguous_range = input_[new_idx:end_range]
            
            part_two = min(contiguous_range) + max(contiguous_range)
            break

    return part_one, part_two
