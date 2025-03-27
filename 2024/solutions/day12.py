from itertools import product
from collections import defaultdict

DIRECTIONS = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def in_bounds(grid, position):
    i, j = position
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

def move(position, direction):
    i, j = position
    x, y = direction
    return i + x, j + y

def neighbors(grid, position):
    for direction in DIRECTIONS:
        next_pos = move(position, direction)
        if in_bounds(grid, next_pos):
            yield next_pos

def count_around(grid, position, target, return_bool=False, return_positions=False, return_around_count=False):
    around_count = 0
    positions = []
    for neighbor in neighbors(grid, position):
        if grid[neighbor[0]][neighbor[1]] == target:
            around_count += 1
            positions.append(neighbor)
    if return_positions and return_around_count:
        return positions, around_count
    elif return_positions:
        return positions
    elif return_bool:
        return around_count != 4
    else:
        return around_count

def diagonal_neighbors(grid, position):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    for direction in directions:
        i, j = move(position, direction)
        if in_bounds(grid, (i, j)):
            yield grid[i][j]

def calculate_corners(grid, position):
    current_value = grid[position[0]][position[1]]
    corner_count = 0

    for directions_pair in [((0, 1), (1, 0)), ((1, 0), (0, -1)), ((0, -1), (-1, 0)), ((-1, 0), (0, 1))]:
        side1 = side2 = 0
        for direction in directions_pair:
            i, j = move(position, direction)
            if not in_bounds(grid, (i, j)) or grid[i][j] != current_value:
                side1 += 1
            else:
                side2 += 1
        if side1 == 2:
            corner_count += 1
        if side2 == 2:
            i, j = move(directions_pair[0], directions_pair[1])
            i, j = move(position, (i, j))
            if grid[i][j] != current_value:
                corner_count += 1
    return corner_count

def main(input_string):
    grid = [list(line) for line in input_string.splitlines()]
    
    groups_by_value = defaultdict(list)
    for i, j in product(range(len(grid)), range(len(grid[0]))):
        groups_by_value[grid[i][j]].append((i, j))
  
    start_position = (0, 0)
    
    visited_global = set()
    queue_global = [start_position]
    groups = []

    while queue_global:
        queue = [queue_global.pop()]
        if queue[-1] in visited_global:
            continue
        visited_global.add(queue[-1])
        visited_local = set()
        current_group = set()

        while queue:
            i, j = queue.pop()
            if (i, j) in visited_local:
                continue
            land_value = grid[i][j]
            current_group.add((i, j))
            visited_local.add((i, j))
            visited_global.add((i, j))
            for neighbor in neighbors(grid, (i, j)):
                if grid[neighbor[0]][neighbor[1]] == land_value:
                    current_group.add(neighbor)
                    queue.append(neighbor)
                else:
                    queue_global.append(neighbor)
        groups.append(sorted(current_group))

    perimeter_total = 0
    sides_total = 0
    for group in groups:
        perimeter = 0
        sides = 0
        if len(group) == 1:
            perimeter += 4
        land_value = grid[group[0][0]][group[0][1]]
            
        for position in group:
            sides += calculate_corners(grid, position)
            around_count = count_around(grid, position, land_value)

            if around_count == 1:
                perimeter += 3
            elif around_count == 2:
                perimeter += 2
            elif around_count == 3:
                perimeter += 1
            elif around_count == 4:
                perimeter += 0
        perimeter_total += len(group) * perimeter
        sides_total += len(group) * sides


    return perimeter_total, sides_total
