with open('day_02/02_input.txt') as x:
    lines = x.readlines()

ans = 0

def get_total_value(given_line: str) -> int:
    game_info, reveals = given_line.split(": ")
    _, game_id = game_info.split(" ")
    game_id = int(game_id)

    highest = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    reveals_groups = reveals.split("; ")
    for reveal in reveals_groups:
        hands = reveal.split(", ")

        for hand in hands:
            amount, color = hand.split(" ")
            if int(amount) > highest[color]:
                highest[color] = int(amount)
    
    return highest["red"] * highest["blue"] * highest["green"]

for line in lines:
    ans += get_total_value(line.strip())

print(ans)