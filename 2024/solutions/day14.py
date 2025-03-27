import re
from itertools import groupby, pairwise

def tree(robots):
    time_step = 0
    while True:
        time_step += 1
        final_positions = []
        for robot in robots:
            y, x, dy, dx = map(int, re.findall('-?\d+', robot))
            x = (x + time_step * dx) % height
            y = (y + time_step * dy) % width
            final_positions.append((x, y))
        
        final_positions.sort()
        grouped_positions = groupby(final_positions, key=lambda pos: pos[0])
        
        for _, group in grouped_positions:
            group_list = list(group)
            consecutive_pairs = set()
            for first, second in pairwise(group_list):
                if second[1] - first[1] == 1:
                    consecutive_pairs.update((first, second))
            sorted_consecutive = sorted(consecutive_pairs)
            if not any(second[1] - first[1] != 1 for first, second in pairwise(sorted_consecutive)):
                if len(consecutive_pairs) > 10:
                    return time_step

width = 101
height = 103

def main(input_data):
    robots = input_data.splitlines()
    tree_time = tree(robots)
    final_positions = []

    for robot in robots:
        y, x, dy, dx = map(int, re.findall('-?\d+', robot))
        x = (x + 100 * dx) % height
        y = (y + 100 * dy) % width
        final_positions.append((x, y))
    
    quadrants = [0, 0, 0, 0]
    for x, y in final_positions:
        if x < height // 2 and y < width // 2:
            quadrants[0] += 1
        elif x < height // 2 and y > width // 2:
            quadrants[1] += 1
        elif x > height // 2 and y < width // 2:
            quadrants[2] += 1
        elif x > height // 2 and y > width // 2:
            quadrants[3] += 1

    

    return quadrants[0]*quadrants[1]*quadrants[2]*quadrants[3], tree_time
