
def policy_check(lines):
    count = 0
    for line in lines:
        amounts, letter, password = line.split(' ')
        min, max = map(int, amounts.split('-'))

        if max >= password.count(letter[0]) >= min:
            count += 1

    return count



if __name__ == "__main__":

    with open('input.txt') as input:
        lines = [line for line in input.read().splitlines()]
        


    print(policy_check(lines))
        