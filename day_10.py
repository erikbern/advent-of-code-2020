import sys

adapters = [int(line.strip()) for line in open(sys.argv[1])]
adapters.sort()
last_adapter = 0
diff_counts = {3: 1}  # includes last one
for adapter in adapters:
    diff = adapter - last_adapter
    diff_counts[diff] = diff_counts.get(diff, 0) + 1
    last_adapter = adapter

print(diff_counts)
print(diff_counts[1] * diff_counts[3])

# Use dynamic programming for the second part
combinations = [1] + [0] * max(adapters)
for adapter in adapters:
    combinations[adapter] = sum(combinations[max(0, adapter-3) : adapter])
    print(adapter, combinations[adapter])
