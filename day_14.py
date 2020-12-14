import sys

memory = {}
patterns = []
for line in open(sys.argv[1]):
    if line.startswith('mask'):
        mask = line.strip().split(' ')[-1]
        i0s = [35-i for i, bit in enumerate(mask) if mask[i] == '0']
        i1s = [35-i for i, bit in enumerate(mask) if mask[i] == '1']
    else:
        value = int(line.strip().split(' ')[-1])
        register = int(line[line.find('[')+1:line.find(']')])
        masked_value = 0
        for i in i0s:
            masked_value ^= value & (1 << i)
        for i in i1s:
            masked_value |= 1 << i
        memory[register] = masked_value

        merged_mask = []
        for i in range(36):
            merged_mask.append(mask[i] if mask[i] in '1X' else str((register >> (35-i))&1))
        patterns.append((''.join(merged_mask), value))

print(sum(memory.values()))

def recurse(patterns, mask):
    if not patterns:
        return 0

    # Find any bit that (a) mask[i] == 'X' (b) at least one pattern has bit[i] set to '0' or '1'
    for i in range(36):
        if mask[i] != 'X': continue
        if not any(pattern[i] in '01' for pattern, value in patterns): continue
        break
    else:
        # No bit found, so just use the last pattern's value for all remaining positions
        pattern, value = patterns[-1]
        return 2**sum(1 for bit in mask if bit == 'X') * value

    # Bit found. Split patterns into two subpatterns and recurse
    mask_0 = ['0' if j == i else bit for j, bit in enumerate(mask)]
    mask_1 = ['1' if j == i else bit for j, bit in enumerate(mask)]
    patterns_0 = [(pattern, value) for pattern, value in patterns if pattern[i] in '0X']
    patterns_1 = [(pattern, value) for pattern, value in patterns if pattern[i] in '1X']
    return recurse(patterns_0, mask_0) + recurse(patterns_1, mask_1)


print(recurse(patterns, ['X'] * 36))
