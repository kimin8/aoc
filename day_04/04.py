with open('day_04/04_input.txt') as d:
    lines = d.readlines()

total_value = 0

def get_value(line: str) -> int:
    line_value = 0
    card_info = line.split(": ")
    _, card_id = card_info[0].split()
    my_numbers = card_info[1].split(" | ")[0].split()
    winning_numbers = card_info[1].split(" | ")[1].split()

    my_numbers = [int(x) for x in my_numbers]
    winning_numbers = [int(x) for x in winning_numbers]

    for number in my_numbers:
        if number in winning_numbers:
            if line_value == 0:
                line_value = 1
            else: 
                line_value *= 2
    
    return line_value

for i in range(0, len(lines)):
    total_value += get_value(lines[i])

print(total_value)