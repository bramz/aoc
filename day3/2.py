import math

def tree_encounters(lines, right, down):
    count, x, y = 0, 0, 0

    while (y + 1) <= len(lines):
        if lines[y][x % len(lines[0])] == '#':
            count += 1
        x += right
        y += down

    return count
        
def parse_slopes(lines):
    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    return math.prod(
        [tree_encounters(lines, slope[0], slope[1]) for slope in slopes]
    )


if __name__ == "__main__":
    with open('inputs1.txt') as input:
        lines = [line for line in input.read().splitlines()]

    print(parse_slopes(lines))