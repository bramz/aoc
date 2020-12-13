
def policy_check(lines):
    count = 0
    for line in lines:
        amount, letter, password = line.split(' ')
        amount1, amount2 = map(int, amount.split('-'))

        if bool(password[amount1-1] == letter[0]) != bool(password[amount2-1] == letter[0]):
            count += 1

    return count



if __name__ == "__main__":

    with open('input2.txt') as input:
        lines = [line for line in input.read().splitlines()]
        


    print(policy_check(lines))
        