import sys

def read():
    lines = []
    for line in open(sys.argv[1]):
        if line.strip() == '':
            yield lines
            lines = []
        else:
            lines.append(line.strip())
    if lines:
        yield lines


n_1, n_2 = 0, 0
for groups in read():
    answers_1 = set.union(*[set(group) for group in groups])
    answers_2 = set.intersection(*[set(group) for group in groups])
    print(groups, answers_1, answers_2)
    n_1 += len(answers_1)
    n_2 += len(answers_2)

print(n_1, n_2)
