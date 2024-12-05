def parse_input(input_data):
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = [tuple(map(int, line.split("|"))) for line in rules_section.splitlines()]
    updates = [list(map(int, line.split(","))) for line in updates_section.splitlines()]
    return rules, updates

def is_update_valid(update, rules):
    positions = {page: idx for idx, page in enumerate(update)}
    for x, y in rules:
        if x in positions and y in positions:
            if positions[x] > positions[y]:
                return False
    return True

def find_middle(update):
    n = len(update)
    return update[n // 2]

def sum_middle_numbers(input_data):
    rules, updates = parse_input(input_data)
    valid_middle_sum = 0

    for update in updates:
        if is_update_valid(update, rules):
            valid_middle_sum += find_middle(update)
    
    return valid_middle_sum

with open("input.txt") as file:
    input_data = file.read()

print(sum_middle_numbers(input_data))
