with open('input.txt') as f:
    input_ = f.read().splitlines()

input_ = [i.split(' ') for i in input_]

first_counter, second_counter = 0, 0

for combination in input_:
    min_, max_ = (int(i) for i in combination[0].split('-'))
    letter = combination[1][0]
    password = combination[2]
    occurrences = list(password).count(letter)
    
    # Part 1
    if occurrences >= min_ and occurrences <= max_:
        first_counter += 1
    
    # Part 2
    if [password[min_-1], password[max_-1]].count(letter) == 1:
        second_counter += 1

print(first_counter)
print(second_counter)
