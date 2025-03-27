from general import Grid
from collections import deque

WIDTH = HEIGHT = 71

def shortest_path(grid):
    start = (0, 0)
    end = (WIDTH - 1, HEIGHT - 1)

    queue = deque([(0, start)])
    visited = set()
    while queue:
        steps, position = queue.popleft()
        if position == end:
            return steps
        if position in visited:
            continue
        visited.add(position)

        for neighbor, value in grid.neighbours(position, get_values=True):
            if value != '#':
                queue.append((steps + 1, neighbor))

    return None

def falling_bytes(grid, coordinates, time):
    while shortest_path(grid):
        grid[coordinates[time]] = '#'
        time += 1
    return coordinates[time - 1][::-1]

def main(input_data):
    coordinates = [list(map(int, line.split(',')))[::-1] for line in input_data.splitlines()]
    time = 1024
    grid = Grid.from_points(coordinates[:time], WIDTH, HEIGHT, '.', '#')
    
    return shortest_path(grid), falling_bytes(grid, coordinates, time)
