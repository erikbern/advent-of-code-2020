dirs = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
m = [line.strip() for line in open('3.txt')]
product = 1
for dx, dy in dirs:
    x, y, n_trees = 0, 0, 0
    while y < len(m):
        n_trees += int(m[y][x] == '#')
        x = (x + dx) % len(m[y])
        y = y + dy
    print(dx, dy, n_trees)
    product *= n_trees
print(product)
