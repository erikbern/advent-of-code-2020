import sys

foods = []
all_ingredients = set()
all_allergens = set()
for line in open(sys.argv[1]):
    ingredients, allergens = line.strip().rstrip(')').split(' (contains ')
    ingredients = ingredients.split(' ')
    allergens = allergens.split(', ')
    foods.append((set(ingredients), set(allergens)))
    all_ingredients.update(set(ingredients))
    all_allergens.update(set(allergens))

def check_foods(allergen, ingredient):
    return all(allergen not in food_allergens or ingredient in food_ingredients
               for food_ingredients, food_allergens in foods)

def recurse(assignments, taken_ingredients):
    if len(assignments) == len(all_allergens):
        print('    ', assignments)
        return assignments
    options = {allergen: [] for allergen in all_allergens if allergen not in assignments}  # allergen -> ingredients
    for allergen in options.keys():
        for ingredient in all_ingredients:
            if ingredient in taken_ingredients:
                continue
            if not check_foods(allergen, ingredient):
                continue
            options[allergen].append(ingredient)

    allergen = min(options.keys(), key=lambda allergen: len(options[allergen]))
    for ingredient in options[allergen]:
        new_assignments, new_taken_ingredients = assignments.copy(), taken_ingredients.copy()
        new_assignments[allergen] = ingredient
        new_taken_ingredients.add(ingredient)
        # print('    trying', allergen, '->', ingredient, new_assignments, new_taken_ingredients)
        res = recurse(new_assignments, new_taken_ingredients)
        if res:
            return res

can_be = {a: set() for a in all_allergens}  # allergen -> set of ingredients
can_be_inv = {}  # ingredient -> set of possible allergens
for allergen in all_allergens:
    for ingredient in all_ingredients:
        if ingredient in can_be[allergen]:  # optimization
            continue
        if not check_foods(allergen, ingredient):
            continue
        print('trying', allergen, '->', ingredient)
        res = recurse({allergen: ingredient}, {ingredient})
        if res:
            for a, i in res.items():
                can_be[a].add(i)
                can_be_inv.setdefault(i, set()).add(a)

print('can be:', can_be)
print('can be inv:', can_be_inv)

count = 0
for ingredients, allergens in foods:
    count += sum(1 for i in ingredients if i not in can_be_inv)

print(count)
print(','.join(sorted(can_be_inv.keys(), key=lambda i: min(can_be_inv[i]))))
