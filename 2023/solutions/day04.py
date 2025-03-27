def main(inp):
    card_lines = inp.splitlines()
    cards = list(map(lambda x: x.split(':')[1], card_lines))
    points = 0
    winning_counts = []
    
    for card in cards:
        winning_numbers, my_numbers = card.split('|')
        winning_numbers = list(map(int, winning_numbers.split()))
        my_numbers = list(map(int, my_numbers.split()))
        score = 0
        temp_score = 0
        
        for num in my_numbers:
            if num in winning_numbers:
                score += 1
                if temp_score == 0:
                    temp_score += 1
                else:
                    temp_score *= 2
        
        winning_counts.append(score)
        points += temp_score
    
    total_scores = [1 for _ in range(len(cards))]
    
    for i, score in enumerate(total_scores):
        win_count = winning_counts[i]
        for j in range(i + 1, i + 1 + win_count):
            if j >= len(total_scores):
                break
            total_scores[j] += score
    
    return points, sum(total_scores)
                    