from general import Grid
from heapq import heappop, heappush
from itertools import product
import networkx as nx

def part1(grid, start, end):
    queue = [(0, start, (0, 1))]
    seen = set()
    while queue:
        steps, position, direction = heappop(queue)
        if position == end:
            return steps
        if (position, direction) in seen:
            continue
        seen.add((position, direction))
        for next_position, next_direction in grid.neighbours(position, get_direction=True):
            if grid[next_position] == '#':
                continue
            if next_direction == direction:
                heappush(queue, (steps + 1, next_position, next_direction))
            else:
                heappush(queue, (steps + 1001, next_position, next_direction))


def part2(grid, start, end):
    graph = nx.Graph()
    graph.add_edge((start, (0, 1)), (start, (-1, 0)), weight=1000)
    for position in product(range(grid.height), range(grid.width)):
        if grid[position] in 'S#':
            continue
        if position == end:
            graph.add_edge(((position[0] + 1, position[1]), (-1, 0)), end, weight=1)
            graph.add_edge(((position[0], position[1] - 1), (0, 1)), end, weight=1)
        for next_position, direction in grid.neighbours(position, get_direction=True):
            if grid[next_position] not in '#E':
                reverse_direction = (-direction[0], -direction[1])
                for direction in Grid.adjacency_map(False):
                    if direction == reverse_direction:
                        graph.add_edge((position, reverse_direction), (next_position, direction), weight=1)
                    else:
                        graph.add_edge((position, reverse_direction), (next_position, direction), weight=1001)
    shortest_paths = nx.all_shortest_paths(graph, (start, (0, 1)), end, weight='weight', method='dijkstra')
    seats = set()
    for path in shortest_paths:
        seats.update(map(lambda x: x[0], path))
    return len(seats)


def main(input_file):
    grid = Grid.from_txt_file(input_file)
    start = end = None
    for position in product(range(grid.height), range(grid.width)):
        if grid[position] == 'S':
            start = position
        if grid[position] == 'E':
            end = position
        if start and end:
            break

    return part1(grid, start, end), part2(grid, start, end)
