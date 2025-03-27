def get_counts(hand, is_part2=False):
    counts = []
    for card in set(hand):
        card_count = hand.count(card)
        if card_count > 1 and (not is_part2 or card != 'J'):
            counts.append(card_count)
    if not is_part2:
        return set(counts), len(counts)
    
    counts.sort(reverse=True)
    if 'J' in hand:
        jack_count = hand.count('J')
        if counts:
            counts[0] += jack_count
        else:
            counts.append(jack_count + 1 if jack_count != 5 else 5)

    return set(counts), len(counts)

def custom_order1(hand, is_part2=False):
    combinations = [
        (set(), 0), ({2}, 1), ({2}, 2), 
        ({3}, 1), ({2, 3}, 2), ({4}, 1), 
        ({5}, 1)
    ]
    return combinations.index(get_counts(hand, is_part2))

def custom_order2(hand, is_part2=False):
    sequence = (
        ['J', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'Q', 'K', 'A']
        if is_part2 else
        ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    )
    return [sequence.index(card) for card in hand]

def main(input_data):
    lines = input_data.splitlines()
    hands = [[line.split()[0], line.split()[1]] for line in lines]
    
    sorted_hands_part1 = sorted(
        hands, 
        key=lambda hand: (custom_order1(hand[0]), custom_order2(hand[0]))
    )
    score_part1 = sum(int(hand[1]) * (i + 1) for i, hand in enumerate(sorted_hands_part1))
    
    sorted_hands_part2 = sorted(
        hands, 
        key=lambda hand: (custom_order1(hand[0], True), custom_order2(hand[0], True))
    )
    score_part2 = sum(int(hand[1]) * (i + 1) for i, hand in enumerate(sorted_hands_part2))
    
    return score_part1, score_part2
