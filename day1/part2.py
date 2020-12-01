sm = 2020

def triplets_sum(numbers, n):
    for i in range(0, n-2):
        for j in range(i+1, n-1):
            for k in range(j+1, n):
                if(numbers[i] + numbers[j] + numbers[k] == sm):
                    total = numbers[i] * numbers[j] * numbers[k]

                    return total


if __name__ == '__main__':
    with open('input.txt', 'r') as input:
        numbers = [int(x) for x in input.read().split()]

    n = len(numbers)
    print(triplets_sum(numbers, n))