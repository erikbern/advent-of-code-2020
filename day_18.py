import sys

def run(left_operand, operator, right_operand):
    if operator == '+':
        return int(left_operand) + int(right_operand)
    else:
        return int(left_operand) * int(right_operand)

def evaluate_simple(tokens, add_prio):
    while len(tokens) > 1:
        index = 1
        if add_prio:
            try:
                index = tokens.index('+')
            except ValueError:
                index = 1
        left_operand, operator, right_operand = tokens[index-1:index+2]
        tokens = tokens[:index-1] + [run(left_operand, operator, right_operand)] + tokens[index+2:]
    return tokens[0]

def evaluate(tokens, add_prio):
    while True:
        # Find paranthesis and simplify them
        left, right = None, None
        for i, token in enumerate(tokens):
            if token == '(':
                left = i
            elif token == ')':
                right = i
                break
        else: 
            break
        tokens = tokens[:left] + [evaluate_simple(tokens[left+1:right], add_prio)] + tokens[right+1:]
    return evaluate_simple(tokens, add_prio)

total_sum_1 = 0
total_sum_2 = 0
for line in open(sys.argv[1]):
    tokens = line.strip()
    # First, tokenize by injecting spaces around operators then splitting
    for op in '()+*':
        tokens = tokens.replace(op, ' ' + op + ' ')
    tokens = [token for token in tokens.split(' ') if token != '']
    res_1 = evaluate(tokens, False)
    res_2 = evaluate(tokens, True)    
    print(line.strip(), '->', res_1, res_2)
    total_sum_1 += res_1
    total_sum_2 += res_2

print(total_sum_1)
print(total_sum_2)
