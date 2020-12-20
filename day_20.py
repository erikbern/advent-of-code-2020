import sys

tiles = {}
for line in open(sys.argv[1]):
    if line == '\n': continue
    elif line.startswith('Tile'):
        tile_i = int(line.replace('Tile', '').replace(':\n', ''))
    else:
        tiles.setdefault(tile_i, []).append(line.strip())

k = int(len(tiles)**0.5)


def flip_horizontally(tile):
    return [''.join(reversed(row)) for row in tile]

def flip_diagonally(tile):
    return [''.join(col) for col in zip(*tile)]


rotations = {}  # (tile_i, j) -> tile
for tile_i, tile in tiles.items():
    for j in range(8):
        rotations[(tile_i, j)] = tile
        if j % 2 == 0:
            tile = flip_horizontally(tile)
        else:
            tile = flip_diagonally(tile)


monster_coords = [(0, 1), (1, 2), (4, 2), (5, 1), (6, 1), (7, 2), (10, 2), (11, 1), (12, 1), (13, 2), (16, 2), (17, 1), (18, 0), (18, 1), (19, 1)]
monster_w = max(x for x, y in monster_coords) + 1
monster_h = max(y for x, y in monster_coords) + 1

def recurse(placed):
    if len(placed) == k**2:
        print(placed[0][0] * placed[k-1][0] * placed[k*(k-1)][0] * placed[k**2-1][0])
        mega_grid = []
        for i in range(k):
            row_tiles = [rotations[p] for p in placed[i*k : (i+1)*k]]
            row_tiles = [[row[1:-1] for row in tile[1:-1]] for tile in row_tiles]
            for rows in zip(*row_tiles):
                mega_grid.append(''.join(rows))
        all_monster_coords = set()
        for row in range(len(mega_grid)-monster_h):
            for col in range(len(mega_grid[0])-monster_w):
                if all(mega_grid[row+y][col+x] == '#' for x, y in monster_coords):
                    all_monster_coords.update((col+x, row+y) for x, y in monster_coords)
        if all_monster_coords:
            total_waves = sum(int(c == '#') for c in ''.join(mega_grid))
            print('found sea monsters:', total_waves - len(all_monster_coords))

    row, col = len(placed)//k, len(placed)%k
    for tile_i in tiles.keys():
        if tile_i in [i for i, j in placed]:
            continue
        for j in range(8):
            if row > 0:  # check row above
                if rotations[placed[len(placed)-k]][-1] != rotations[(tile_i, j)][0]:
                    continue
            if col > 0:  # check col to the left
                if not all(p[-1] == q[0] for p, q in zip(rotations[placed[-1]], rotations[(tile_i, j)])):
                    continue
            placed_new = list(placed)
            placed_new.append((tile_i, j))
            recurse(placed_new)

recurse([])

