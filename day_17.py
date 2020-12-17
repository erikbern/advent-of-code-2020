import sys

active = set()
for i, line in enumerate(open(sys.argv[1])):
    for j, ch in enumerate(line.strip()):
        if ch == '#':
            active.add((0, 0, i, j))

def simulate(active, dirs):
    for step in range(6):
        nns_count = {}
        for i, j, k, l in active:
            for di, dj, dk, dl in dirs:
                coord2 = i+di, j+dj, k+dk, l+dl
                nns_count[coord2] = nns_count.get(coord2, 0) + 1

        new_active = set()
        for coord in active:
            if nns_count.get(coord, 0) in [2, 3]:
                new_active.add(coord)
        for coord, ct in nns_count.items():
            if coord not in active and ct == 3:
                new_active.add(coord)
        active = new_active
        print(len(active))

dirs_1 = [(0, di, dj, dk) for di in range(-1, 2) for dj in range(-1, 2) for dk in range(-1, 2)]
dirs_1 = [dijk for dijk in dirs_1 if dijk != (0, 0, 0, 0)]
simulate(active, dirs_1)

dirs_2 = [(di, dj, dk, dl) for di in range(-1, 2) for dj in range(-1, 2) for dk in range(-1, 2) for dl in range(-1, 2)]
dirs_2 = [dijk for dijk in dirs_2 if dijk != (0, 0, 0, 0)]
simulate(active, dirs_2)
