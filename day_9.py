import sys

data = [int(line.strip()) for line in open(sys.argv[1])]
window = int(sys.argv[2])

for i in range(window, len(data)):
    if not any(j != k and data[i] == data[j] + data[k]
               for j in range(i-window, i)
               for k in range(i-window, i)):
        print(i, data[i])
        invalid = data[i]

# The solution here is O(n^3) although it could be linear with some tricks
for i in range(0, len(data)-2):
    for j in range(i+2, len(data)):
        if sum(data[i:j]) == invalid:
            print(i, j, min(data[i:j]) + max(data[i:j]))
