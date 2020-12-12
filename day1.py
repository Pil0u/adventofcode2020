from itertools import combinations

with open('input.txt') as f:
    input_ = f.read().splitlines()

input_ = [int(i) for i in input_]

# Part 1
for i, j in combinations(input_, 2):
    if i + j == 2020:
        print(i * j)
        break

# Part 2
for i, j, k in combinations(input_, 3):
    if i + j + k == 2020:
        print(i * j * k)
        break
