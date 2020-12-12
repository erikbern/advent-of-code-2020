import sys

steps = [(line[0], int(line[1:].strip())) for line in open(sys.argv[1])]
dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
cardinals = 'ENWS'

x, y, d = 0, 0, 0
for instruction, size in steps:
    if instruction in cardinals:
        dx, dy = dirs[cardinals.find(instruction)]
        x, y = x + dx*size, y+dy*size
    elif instruction in 'LR':
        assert size % 90 == 0
        dd = (size // 90) * {'R': -1, 'L': 1}[instruction]
        d = (d + dd + 4) % 4
    elif instruction == 'F':
        dx, dy = dirs[d]
        x, y = x + dx*size, y+dy*size
    print(instruction, size, (x, y), d)
print(x, y, abs(x) + abs(y))
print()

x, y, wx, wy = 0, 0, 10, 1
for instruction, size in steps:
    if instruction in cardinals:
        dx, dy = dirs[cardinals.find(instruction)]
        wx, wy = wx + dx*size, wy+dy*size
    elif instruction in 'LR':
        assert size % 90 == 0
        ccw_rots = ((size // 90) * {'R': -1, 'L': 1}[instruction] + 4) % 4
        for j in range(ccw_rots):
            wx, wy = -wy, wx
    elif instruction == 'F':
        x, y = x + wx*size, y + wy*size
    print(instruction, size, (x, y), (wx, wy))
print(x, y, abs(x) + abs(y))
