from itertools import cycle
from math import lcm

def main(input_data):
    directions_data, raw_guide_data = input_data.split('\n\n')
    directions = directions_data.replace('R', '1').replace('L', '0').strip()
    
    guide_map = {}
    for line in raw_guide_data.splitlines():
        key = line[:3]
        value1 = line[7:10]
        value2 = line[12:15]
        guide_map[key] = (value1, value2)

    current_position = 'AAA'
    total_steps = 0
    for direction in cycle(directions):
        current_position = guide_map[current_position][int(direction)]
        total_steps += 1
        if current_position == 'ZZZ':
            break

    starting_positions = [key for key in guide_map.keys() if key.endswith('A')]
    loop_lengths = []
    for start_pos in starting_positions:
        steps_to_reach_z = 0
        for direction in cycle(directions):
            steps_to_reach_z += 1
            start_pos = guide_map[start_pos][int(direction)]
            if start_pos.endswith('Z'):
                loop_lengths.append(steps_to_reach_z)
                break

    return total_steps, lcm(*loop_lengths)
