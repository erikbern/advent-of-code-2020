import sys
f = open(sys.argv[1])
card_public_key = int(next(f).strip())
door_public_key = int(next(f).strip())

n = 20201227
group_order = n - 1  # it's a prime

print('generating discrete logs')
discrete_logs = [None] * n
powers = [None] * n
m = 1
for i in range(n):
    discrete_logs[m] = i
    powers[i] = m
    m = (7*m) % n

card_discrete_log = discrete_logs[card_public_key]
door_discrete_log = discrete_logs[door_public_key]

product = (card_discrete_log * door_discrete_log) % group_order
print(powers[product])

