import re


def read_passports():
    kw = {}
    for line in open('4.txt'):
        # print(line.strip())
        if line.strip() == '':
            yield kw
            kw = {}
        else:
            kw.update(dict(kv.split(':') for kv in line.strip().split()))
    if kw:
        yield kw

exp_fields = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'])  #, 'cid'])
n_valid = 0
n_valid_2 = 0
for pp in read_passports():
    n_valid += int(set(pp.keys()).intersection(exp_fields) == exp_fields)
    matches = lambda pattern, haystack: bool(re.fullmatch(pattern, haystack))
    valid_fields = {
        'byr': 'byr' in pp and matches(r'\d\d\d\d', pp['byr']) and 1920 <= int(pp['byr']) <= 2002,
        'iyr': 'iyr' in pp and matches(r'\d\d\d\d', pp['iyr']) and 2010 <= int(pp['iyr']) <= 2020,
        'eyr': 'eyr' in pp and matches(r'\d\d\d\d', pp['eyr']) and 2020 <= int(pp['eyr']) <= 2030,
        'hgt': 'hgt' in pp and ((matches(r'\d+cm', pp['hgt']) and 150 <= int(pp['hgt'].replace('cm', '')) <= 193) or
                                (matches(r'\d+in', pp['hgt']) and 59 <= int(pp['hgt'].replace('in', '')) <= 76)),
        'hcl': 'hcl' in pp and matches(r'#[0-9a-f]{6}', pp['hcl']),
        'ecl': 'ecl' in pp and matches(r'(amb|blu|brn|gry|grn|hzl|oth)', pp['ecl']),
        'pid': 'pid' in pp and matches(r'\d{9}', pp['pid']),
    }
    print([(key, pp.get(key), valid_fields.get(key)) for key in valid_fields])
    n_valid_2 += int(all(valid_fields.values()))

print(n_valid)
print(n_valid_2)
