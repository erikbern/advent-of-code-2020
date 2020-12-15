import sys

numbers = [int(z) for z in sys.argv[1].split(',')]
index = int(sys.argv[2])
indices = {}
for i, n in enumerate(numbers):
    indices.setdefault(n, []).append(i)
while len(numbers) < index:
    if len(numbers) % 100000 == 0:
        print(len(numbers), '...')
    if numbers[-1] in indices and len(indices[numbers[-1]]) >= 2:
        number = indices[numbers[-1]][-1] - indices[numbers[-1]][-2]
    else:
        number = 0
    indices.setdefault(number, []).append(len(numbers))
    numbers.append(number)

print(numbers[-1])
