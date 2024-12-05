from collections import defaultdict, deque

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

def topological_sort(update, rules):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    update_set = set(update)
    
    for x, y in rules:
        if x in update_set and y in update_set:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree.setdefault(x, 0)
    
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_order = []
    
    while queue:
        node = queue.popleft()
        sorted_order.append(node)
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_order

def find_middle(update):
    n = len(update)
    return update[n // 2]

def sum_middle_numbers_for_invalid_updates(input_data):
    rules, updates = parse_input(input_data)
    invalid_middle_sum = 0

    for update in updates:
        if not is_update_valid(update, rules):
            sorted_update = topological_sort(update, rules)
            invalid_middle_sum += find_middle(sorted_update)
    
    return invalid_middle_sum

with open("input.txt") as file:
    input_data = file.read()

print(sum_middle_numbers_for_invalid_updates(input_data))
