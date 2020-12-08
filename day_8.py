import sys

instructions = []
for line in open(sys.argv[1]):
    ins, arg = line.strip().split()
    instructions.append((ins, int(arg)))

def execute(instructions):
    visited = set()
    acc, pointer = 0, 0
    while True:
        visited.add(pointer)
        ins, arg = instructions[pointer]
        if ins == 'nop':
            pointer += 1
        elif ins == 'acc':
            acc += arg
            pointer += 1
        else:
            pointer += arg
        if pointer in visited:
            return (False, acc)
        if pointer == len(instructions):
            return (True, acc)

print(execute(instructions))

possible_results = []
for i in range(len(instructions)):
    ins, arg = instructions[i]
    ins = {'nop': 'jmp', 'jmp': 'nop'}.get(ins)
    if ins is None:
        continue
    instructions_copy = list(instructions)
    instructions_copy[i] = (ins, arg)
    terminated, acc = execute(instructions_copy)
    if terminated:
        possible_results.append(acc)

print(possible_results)
