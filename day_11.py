import sys

dirs = [(dx, dy) for dx in range(-1, 2) for dy in range(-1, 2) if dx !=0 or dy != 0]

def step(matrix, max_steps, change_threshold):
    new_matrix = [[c for c in line] for line in matrix]
    h, w = len(matrix), len(matrix[0])
    for y in range(h):
        for x in range(w):
            count = 0
            for dx, dy in dirs:
                next_seat = '?'
                for i in range(1, max_steps+1):
                    if not (0 <= x + i*dx < w and 0 <= y + i*dy < h):
                        break
                    next_seat = matrix[y + i*dy][x + i*dx]
                    if next_seat in '#L':
                        break
                count += int(next_seat == '#')
            if matrix[y][x] == 'L' and count == 0:
                new_matrix[y][x] = '#'
            elif matrix[y][x] == '#' and count >= change_threshold:
                new_matrix[y][x] = 'L'
    return new_matrix

def print_matrix(matrix):
    return '\n'.join(''.join(line) for line in matrix)

def simulate(matrix, max_steps=1, change_threshold=4):
    matrix_str = print_matrix(matrix)

    while True:
        print(print_matrix(matrix) + '\n\n')
        new_matrix = step(matrix, max_steps, change_threshold)
        new_matrix_str = print_matrix(new_matrix)
        if new_matrix_str == matrix_str:
            break
        matrix, matrix_str = new_matrix, new_matrix_str

    print(sum(1 for c in matrix_str if c == '#'))

matrix = [[c for c in line.strip()] for line in open(sys.argv[1])]
simulate(matrix)
simulate(matrix, max_steps=999999, change_threshold=5)
