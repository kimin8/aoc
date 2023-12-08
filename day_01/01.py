with open('day_01/01_input.txt') as x:
    lines = x.readlines()

sum = 0
def get_line_value(line: str):
    digits = []
    for i, c in enumerate(line):
        if c.isdigit():
            digits.append(c)
        for d, val in enumerate(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']):
            if line[i:].startswith(val):
                digits.append(str(d+1))
    return int(digits[0] + digits[-1])

for line in lines:
    sum += get_line_value(line.strip())
print(sum)