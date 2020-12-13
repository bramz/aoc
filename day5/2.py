
def find_seat_positions(seat, row1, row2, col1, col2):
    for i in range(7):
        if seat[i] == 'F':
            row2 = (row2 + row1)//2
        elif seat[i] == 'B':
            row1 = (row2 + row1)//2

    for i in range(6, 10):
        if seat[i] == 'L':
            col2 = (col2 + col1)//2
        elif seat[i] == 'R':
            col1 = (col2 + col1)//2

    return (col2, row2)

if __name__ == "__main__":
    with open('inputs.txt') as input:
        lines = [line for line in input.read().splitlines()]

    highs = []

    for i in range(len(lines)):
        seat_positions = find_seat_positions(lines[i], 0, 127, 0, 7)
        seat_id = seat_positions[1] * 8 + seat_positions[0]
        highs.append(seat_id)

    for i in range(min(highs), max(highs)):
        if i not in highs:
            print(i)
        
    