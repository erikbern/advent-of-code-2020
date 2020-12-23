import sys

cups = sys.argv[1]
steps = int(sys.argv[2])
n = int(sys.argv[3])

def print_cups(current_cup, next_cup, n):
    cups = []
    for i in range(n):
        cups.append(str(current_cup))
        current_cup = next_cup[current_cup]
    print(''.join(cups))

# Initialize what's essentially a linked list
next_cup = [None] * (n+1) # after cup i, what's the one to the right of it
cups = sys.argv[1]
current_cup = int(cups[0])
for i in range(len(cups)-1):
    next_cup[int(cups[i])] = int(cups[i+1])
if n > len(cups):
    next_cup[int(cups[-1])] = len(cups) + 1
    for i in range(len(cups)+1, n):
        next_cup[i] = i+1
    next_cup[n] = current_cup
else:
    next_cup[int(cups[-1])] = current_cup

# Simulate
for step in range(steps):
    if step % 100000 == 0:
        print(step, '...')

    if n < 10 and steps <= 100:
        print_cups(current_cup, next_cup, n)

    # Pick up three cups
    pick_up = []
    cup = next_cup[current_cup]
    for j in range(3):
        pick_up.append(cup)
        cup = next_cup[cup]

    # Remove those three cups
    next_cup[current_cup] = cup

    # Find the destination cup
    dest = current_cup
    while dest == current_cup or dest in pick_up:
        dest = (dest + n - 2) % n + 1

    # Place three cups after the destination cup
    after_dest_cup = next_cup[dest]
    next_cup[dest] = pick_up[0]
    next_cup[pick_up[-1]] = after_dest_cup

    # Pick the next one as the current cup
    current_cup = next_cup[current_cup]

if n < 10:
    print_cups(current_cup, next_cup, n)
    print_cups(1, next_cup, n)

next_two = [next_cup[1], next_cup[next_cup[1]]]
print(next_two, next_two[0] * next_two[1])

