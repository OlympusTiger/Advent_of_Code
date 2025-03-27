from functools import cache


@cache
def count_matches(towel):
    if not towel:
        return 1
    count = 0
    for pattern in patterns:
        if towel.startswith(pattern):
            count += count_matches(towel[len(pattern):])
    return count


def main(input_data):
    global patterns
    patterns, towels = input_data.split('\n\n')
    patterns = patterns.split(', ')
    towels = towels.splitlines()
    part1_count = 0
    part2_count = 0
    for towel in towels:
        if count_matches(towel):
            part1_count += 1
            part2_count += count_matches(towel)

    return part1_count, part2_count
