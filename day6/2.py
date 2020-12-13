import string

def count_answers(answers):
    count = 0
    for answer in answers:
        count += len([x for x in string.ascii_lowercase if all([x in y for y in answer])])

    return count


if __name__ == "__main__":
    with open('inputs.txt') as input:
        lines = [i.replace(' ', '').split('\n') for i in input.read().split('\n\n')] 

    print(count_answers(lines))