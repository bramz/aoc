def tree_encounters(lines, right, down):
    count, x, y = 0, 0, 0

    while (y + 1) <= len(lines):
        if lines[y][x % len(lines[0])] == '#':
            count += 1
        x += right
        y += down

    return count
        



if __name__ == "__main__":
    with open('inputs1.txt') as input:
        lines = [line for line in input.read().splitlines()]

    print(tree_encounters(lines, 3, 1))