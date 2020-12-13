values = [
    'byr',
    'iyr',
    'eyr',
    'hgt',
    'hcl',
    'ecl',
    'pid',
    'cid'
]

def get_passports(lines: list[str]) -> list[dict]:
    passport = {}
    passports = []

    for line in lines:
        if passport and not line:
            passports.append(passport)
            passport = {}
        else:
            entries = line.split(' ')
            for entry in entries:
                key, value = entry.split(':')
                passport.update({key: value})

    if passport:
        passports.append(passport)

    return passports

def count_valid_passports(passports):
    count = 0
    
    for passport in passports:
        for value in values:
            if value in passport.keys():
                count += 1
                    
    return count
    

if __name__ == "__main__":
    with open('inputs.txt') as input:
        lines = [line for line in input.read().splitlines()]

    passports = get_passports(lines)

    print(count_valid_passports(passports))



