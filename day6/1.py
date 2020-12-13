def count_answers(answers):
    count = 0
    for answer in answers:
        count += len(set(answer))
        
    return count


if __name__ == "__main__":
    with open('inputs.txt') as input:
        lines = [i.replace(' ', '').replace('\n', '') for i in input.read().split('\n\n')] 

    print(count_answers(lines))