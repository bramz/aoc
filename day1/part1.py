total = 2020

with open('input.txt', 'r') as input:
    numbers = [int(x) for x in input.read().split()]

for i, number in enumerate(numbers[:-1]):
    comp = total - number
    if comp in numbers[i+1:]:
        final = number * comp
        print("Result: {}".format(final))
        break
else:
    print("none")
