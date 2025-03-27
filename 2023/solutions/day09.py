from itertools import pairwise
from operator import sub

def calculate_next_value(numbers):
    differences = [sub(*pair[::-1]) for pair in pairwise(numbers)]
    if set(differences) == {0}:
        return numbers[-1]
    return numbers[-1] + calculate_next_value(differences)

def calculate_total(sequence):
    total = 0
    for numbers in sequence:
        total += calculate_next_value(numbers)
    return total

def main(input_data):
    sequences = [list(map(int, line.split())) for line in input_data.splitlines()]
    reversed_sequences = [numbers[::-1] for numbers in sequences]
    return calculate_total(sequences), calculate_total(reversed_sequences)
                    