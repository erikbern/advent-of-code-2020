import sys

n, b = [line.strip() for line in open(sys.argv[1])]
n = int(n)
buses = [int(z) for z in b.split(',') if z != 'x']
offsets = [i for i, z in enumerate(b.split(',')) if z != 'x']

wait_times = [bus - (n % bus) - bus*int(n % bus == 0)
              for bus in buses]
wait_time, bus = min(zip(wait_times, buses))
print(wait_time, bus, wait_time*bus)

def sgd(a, b):
    return b if a % b == 0 else sgd(b, a % b)

m, k = 1, 0  # solution is of the form i*m + k for some i

for b, o in zip(buses, offsets):
    while (k+o) % b > 0:
        k += m
    m = m * b // sgd(m, b)
    print(m, k)

