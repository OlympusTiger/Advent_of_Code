
def main(inp):
    keys_and_locks = inp.split('\n\n')

    keys = []
    locks = []
    for x in keys_and_locks:
        grid = [list(i) for i in x.splitlines()]
        flip = list(zip(*grid))
        lens = [i.count('#') for i in flip]
        if ['#'] * 5 == grid[0]:
            locks.append(lens)
        else:
            keys.append(lens)

    keys.sort()
    locks.sort()

    valid = 0
    for k in keys:
        for l in locks:
            if k[0] + l[0] > 7:
                break
            if all(k[i] + l[i] <= 7 for i in range(1, 5)):
                valid += 1

    return valid, None



