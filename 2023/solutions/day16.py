from general import Grid



def lens(p,val,d):
    match val:
            case '.':
                yield (p,d)
            case '|':
                if d in [(1,0),(-1,0)]:
                    yield (p,d)
                else:
                    yield (p,(1,0))
                    yield (p,(-1,0))
            case '-':
                if d in [(0,1),(0,-1)]:
                    yield (p,d)
                else:
                    yield (p,(0,1))
                    yield (p,(0,-1))
            case '\\':
                if d==(0,1):
                    yield (p,(1,0))
                elif d==(0,-1):
                    yield (p,(-1,0))
                elif d==(1,0):
                    yield (p,(0,1))
                elif d==(-1,0):
                    yield (p,(0,-1))
            case '/':
                if d==(0,1):
                    yield (p,(-1,0))
                elif d==(0,-1):
                    yield (p,(1,0))
                elif d==(1,0):
                    yield (p,(0,-1))
                elif d==(-1,0):
                    yield (p,(0,1))


def beam_bounce(grid,start,d):
    q=[(grid.move(start,d,multiplier=-1),d)]
    seen=set()
    energized=set()
    while q:
        p,d=q.pop()
        if (p,d) in seen:
            continue
        seen.add((p,d))
        energized.add(p)
        nxt=grid.move(p,d)
        if not grid.in_bounds(nxt):
            continue
        for x in lens(nxt,grid[nxt],d):
            q.append(x)
    return len(energized)-1


def find_entrances(grid):
    top_row=[(0,i) for i in range(grid.width)]
    bottom_row=[(grid.height-1,i) for i in range(grid.width)]
    left_col=[(i,0) for i in range(grid.height)]
    right_col=[(i,grid.width-1) for i in range(grid.height)]
    all_energized=[]
    for e in top_row:
        all_energized.append(beam_bounce(grid,e,(1,0)))
    for e in bottom_row:
        all_energized.append(beam_bounce(grid,e,(-1,0)))
    for e in left_col:
        all_energized.append(beam_bounce(grid,e,(0,1)))
    for e in right_col:
        all_energized.append(beam_bounce(grid,e,(0,-1)))
    return max(all_energized)



def main(inp):
    grid=Grid.from_txt_file(inp)
    start = (0,0)
    d=(0,1)

    return beam_bounce(grid,start,d),find_entrances(grid)
                    