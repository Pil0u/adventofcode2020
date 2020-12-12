with open('input.txt') as f:
    input_ = f.read().splitlines()

# Functions for Part 2
def check_byr(string):
    try:
        value = int(string)
    except:
        return False
    
    return 1920 <= value <= 2002

def check_iyr(string):
    try:
        value = int(string)
    except:
        return False
    
    return 2010 <= value <= 2020

def check_eyr(string):
    try:
        value = int(string)
    except:
        return False
    
    return 2020 <= value <= 2030

def check_hgt(string):
    unit = string[-2:]
    try:
        number = int(string[:-2])
    except:
        return False
    
    if (unit == 'cm' and 150 <= number <= 193) or (unit == 'in' and 59 <= number <= 76):
        return True
    
    return False

def check_hcl(string):
    try:
        int(string[1:], 16)
    except:
        return False
    
    return string[0] == '#' and len(string[1:]) == 6

def check_ecl(string):
    return string in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

def check_pid(string):
    try:
        int(string)
    except:
        return False
    
    return len(string) == 9


passports = []
current_passport = []

for idx, elem in enumerate(input_):
    if elem == '':
        passports.append(current_passport)
        current_passport = []
        continue        
    
    current_passport.extend(elem.split(' '))

# Append last passport, still unstored
passports.append(current_passport)

required_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
field_valid, full_valid = 0, 0

for passport in passports:
    fields = {elem[:3]: elem[4:] for elem in passport}
    missing_fields = set(required_fields) - set(fields.keys())
    
    # Part 1
    if not any(missing_fields):
        field_valid += 1
        
        # Part 2
        current_valid = True
        
        for field in required_fields:
            if (field == 'byr' and not check_byr(fields['byr'])) \
            or (field == 'iyr' and not check_iyr(fields['iyr'])) \
            or (field == 'eyr' and not check_eyr(fields['eyr'])) \
            or (field == 'hgt' and not check_hgt(fields['hgt'])) \
            or (field == 'hcl' and not check_hcl(fields['hcl'])) \
            or (field == 'ecl' and not check_ecl(fields['ecl'])) \
            or (field == 'pid' and not check_pid(fields['pid'])):
                current_valid = False
                break
        
        if current_valid:
            full_valid += 1

print(field_valid)
print(full_valid)
