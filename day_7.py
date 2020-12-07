import sys

data = {}
for line in open(sys.argv[1]):
    outer, inner = line.strip().rstrip('.').split(' bags contain ')
    inner_parsed = []
    if inner != 'no other bags':
        for d in inner.split(', '):
            count, bag_type = d.replace(' bags', '').replace(' bag', '').split(' ', 1)
            inner_parsed.append((int(count), bag_type))
    outer_parsed = outer.replace(' bags', '')
    assert outer not in data
    data[outer_parsed] = inner_parsed


can_hold_gold = {'shiny gold': True}
def can_hold_gold_f(bag_type):
    if bag_type not in can_hold_gold:
        can_hold_gold[bag_type] = any(can_hold_gold_f(bag_type) for count, bag_type in data[bag_type])
    return can_hold_gold[bag_type]

n_can_hold_gold = sum(1 for bag_type in data.keys()
                      if bag_type != 'shiny gold'
                      and can_hold_gold_f(bag_type))

print(n_can_hold_gold)

total_bags = {}
def total_bags_f(bag_type):
    if bag_type not in total_bags:
        total_bags[bag_type] = 1 + sum(count*total_bags_f(bag_type) for count, bag_type in data[bag_type])
    return total_bags[bag_type]

print(total_bags_f('shiny gold') - 1)
