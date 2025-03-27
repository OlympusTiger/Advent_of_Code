from itertools import product
import re


class Grid:
    def __init__(self, grid):
        self.grid = grid
        self.height = len(grid)
        self.width = len(grid[0])

    @classmethod
    def from_txt_file(cls, file, func=str):
        return cls([list(map(func, line)) for line in file.splitlines()])

    @classmethod
    def from_points(cls, points, height, width, empty_str, occupied_str):
        grid = [[empty_str for _ in range(width)] for _ in range(height)]
        for point in points:
            grid[point[0]][point[1]] = occupied_str
        return cls(grid)

    @classmethod
    def from_dict(cls, dictionary):
        min_x = min(map(lambda x: x[0], dictionary.keys()))
        max_x = max(map(lambda x: x[0], dictionary.keys()))
        min_y = min(map(lambda x: x[1], dictionary.keys()))
        max_y = max(map(lambda x: x[1], dictionary.keys()))
        return cls(
            [
                [dictionary[(i, j)] for j in range(min_y, max_y + 1)]
                for i in range(min_x, max_x + 1)
            ]
        )

    def __str__(self):
        return "\n".join("".join(str(i) for i in line) for line in self.grid)

    def __getitem__(self, position):
        i, j = position
        return self.grid[i][j]

    def __setitem__(self, position, value):
        i, j = position
        self.grid[i][j] = value

    def __iter__(self):
        for i in range(self.height):
            yield self.grid[i]

    def _find(self, *args):
        to_return = []
        for i, j in product(range(self.height), range(self.width)):
            if self.grid[i][j] in args:
                to_return.append((i, j))
        return to_return

    def popgrid(self, position):
        i, j = position
        return self.grid[i].pop(j)

    def insertgrid(self, position, value):
        i, j = position
        self.grid[i].insert(j, value)

    def row(self, r):
        return self.grid[r]

    def col(self, c):
        return [self.grid[i][c] for i in range(self.height)]

    def in_bounds(self, position):
        i, j = position
        return 0 <= i < self.height and 0 <= j < self.width

    def neighbours(
        self,
        position,
        diagonal=False,
        get_values=False,
        get_direction=False,
        exclude_value=[],
        exclude_dir=[],
    ):
        i, j = position
        for dx, dy in self.adjacency_map(diagonal):
            if (dx, dy) in exclude_dir:
                continue
            x, y = i + dx, j + dy
            if self.in_bounds((x, y)):
                if self.grid[x][y] not in exclude_value:
                    to_return = [(x, y)]
                    if get_values:
                        to_return.append(self.grid[x][y])
                    if get_direction:
                        to_return.append((dx, dy))
                    yield to_return

    @staticmethod
    def adjacency_map(diagonals):
        return (
            [(1, 0), (0, -1), (-1, 0), (0, 1)]
            if not diagonals
            else [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        )

    @staticmethod
    def move(x, d, multiplier=1):
        return (x[0] + d[0] * multiplier, x[1] + d[1] * multiplier)


def manhattan_distance(x, y=(0, 0)):
    zipped = zip(x, y)
    return sum(abs(a - b) for a, b in zipped)


def ints(string, delimiter=None):
    if delimiter is None:
        return [int(i) for i in string.split()]
    elif delimiter == "ure":
        return [int(i) for i in re.findall(r"\d+", string)]
    elif delimiter == "ire":
        return [int(i) for i in re.findall(r"-?\d+", string)]
    else:
        return [int(i) for i in string.split(delimiter)]
