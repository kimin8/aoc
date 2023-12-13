with open('day_04/04_input.txt') as d:
    lines = d.readlines()
from collections import defaultdict

N = defaultdict(int)

for i, line in enumerate(lines):
    N[i] += 1
    first, rest = line.split("|")
    id_, card = first.split(":")
    card_nums = [int(x) for x in card.split()]
    rest_nums = [int(x) for x in rest.split()]
    val = len(set(card_nums) & set(rest_nums))
    for j in range(val):
        N[i+1+j] += N[i]

print(sum(N.values()))