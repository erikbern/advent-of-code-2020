import sys

lines = [line.strip() for line in open(sys.argv[1])]
i = lines.index('')
unparsed_rules, messages = lines[:i], lines[i+1:]

rules = {}
for unparsed_rule in unparsed_rules:
    i, parts = unparsed_rule.split(': ')
    i = int(i)
    if parts.startswith('"'):
        rules[i] = ('str', parts.strip('"'))
    else:
        parts = [[int(z) for z in p.split(' ')] for p in parts.split(' | ')]
        rules[i] = ('sub', parts)

memoized = {}  # (pattern, rule) -> bool

def matches_memoized(pattern, rule):
    if (pattern, rule) not in memoized:
        memoized[(pattern, rule)] = matches(pattern, rule)
    # print(pattern, rule, '->', memoized[(pattern, rule)])
    return memoized[(pattern, rule)]


def matches(pattern, rule):
    tag, parts = rules[rule]
    if tag == 'str':
        return (pattern == parts)

    # Use dynamic programming to match
    for groups in parts:
        prefix_match = set([0])
        for rule in groups:
            new_prefix_match = set()
            for end_point in range(1, len(pattern)+1):
                for start_point in range(0, end_point):
                    if start_point in prefix_match and matches_memoized(pattern[start_point:end_point], rule):
                        new_prefix_match.add(end_point)
            prefix_match = new_prefix_match

        if len(pattern) in prefix_match:
            return True
    return False

count_valid = 0
for message in messages:
    res = matches_memoized(message, 0)
    print(message, '->', res)
    if res:
        count_valid += 1
print(count_valid)
