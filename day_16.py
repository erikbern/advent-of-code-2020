import sys

lines = [line.strip() for line in open(sys.argv[1])]
i = lines.index('')
j = lines.index('', i+1)

constraints = {}
for line in lines[:i]:
    key, c = line.split(': ')
    constraints[key] = [tuple(map(int, r.split('-'))) for r in c.split(' or ')]

your_ticket = [int(z) for z in lines[i+2].split(',')]
    
def is_valid_n_c(n, c):
    return any(lo <= n <= hi for lo, hi in c)

def is_valid_n(n):
    return any(is_valid_n_c(n, c) for c in constraints.values())

invalid_sum = 0
still_valid = []
for ticket in lines[j+2:]:
    numbers = [int(z) for z in ticket.split(',')]
    invalid_numbers = [n for n in numbers if not is_valid_n(n)]
    invalid_sum += sum(invalid_numbers)
    if not invalid_numbers:
        still_valid.append(numbers)

print(invalid_sum)

def guess_order(keys):
    if not any(k is None for k in keys):
        return keys

    possible_keys = {}
    for i, key in enumerate(keys):
        if key is not None: continue
        possible_keys[i] = []
        for key in constraints.keys():  # guess the next field
            if key in keys: continue
            if all(is_valid_n_c(ticket[i], constraints[key]) for ticket in still_valid):
                possible_keys[i].append(key)

    next_i = min((i for i in possible_keys.keys()), key=lambda i: len(possible_keys[i]))
    print('next i:', next_i, possible_keys[next_i])
    next_keys = list(keys)
    for key in possible_keys[next_i]:
        next_keys[next_i] = key
        ret = guess_order(next_keys)
        if ret:
            return ret

keys = guess_order([None] * len(constraints))
print(keys)
mult = 1
for key, n in zip(keys, your_ticket):
    if key.startswith('departure'):
        mult *= n

print(mult)
