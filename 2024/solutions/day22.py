from more_itertools import sliding_window
from collections import defaultdict


def calculate_next(number):
    number = ((number * 64) ^ number) % 16777216
    number = ((number // 32) ^ number) % 16777216
    number = ((number * 2048) ^ number) % 16777216
    return number

def main(input_data):
    numbers = list(map(int, input_data.splitlines()))
    price_changes = defaultdict(int)
    result = 0
    for number in numbers:
        prices = [number % 10]
        changes = []
        temp = {}
        for _ in range(2000):
            number = calculate_next(number)
            price = number % 10
            changes.append(price - prices[-1])
            prices.append(price)
        for i, window in enumerate(sliding_window(changes[::-1], 4)):
            temp[window] = prices[-i - 1]
        for window in temp:
            price_changes[window] += temp[window]
        result += number
        
    return result, max(price_changes.values())


