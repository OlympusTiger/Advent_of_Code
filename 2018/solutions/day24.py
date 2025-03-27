import re
from copy import deepcopy

class Group:
    def __init__(self, units, hp, dmg, dmg_type, initiative, immune, weak, team):
        self.units = units
        self.hp = hp
        self.dmg = dmg
        self.dmg_type = dmg_type
        self.initiative = initiative
        self.immune = immune
        self.weak = weak
        self.team = team

    @property
    def effective(self):
        return self.units * self.dmg

    def __repr__(self):
        return f'({self.units,self.hp,self.dmg,self.dmg_type,self.initiative,self.immune,self.weak,self.effective})'
        
    def total_damage(self, weaknesses, immunities):
        if self.dmg_type in immunities:
            return 0
        elif self.dmg_type in weaknesses:
            return 2 * self.effective
        else:
            return self.effective

    def defence(self, d):
        self.defend = d


def parse(i):
    immune, weak = [], []
    units, hp, dmg, initiative = map(int, re.findall('\d+', i))
    dmg_type = re.search('\w+(?= damage)', i).group(0)
    if (k := i.find('(')) != -1:
        l = i.find(')')
        st = i[k + 1 : l]
        s = st.split('; ')
        if len(s) == 1:
            if s[0].startswith('weak'):
                weak = s[0][8:].split(', ')
            elif s[0].startswith('immune'):
                immune = s[0][10:].split(', ')
        elif len(s) == 2:
            for j in s:
                if j.startswith('weak'):
                    weak = j[8:].split(', ')
                elif j.startswith('immune'):
                    immune = j[10:].split(', ')
    return units, hp, dmg, dmg_type, initiative, immune, weak


def attacking(pairs):
    pairs.sort(key=lambda x: -x[0].initiative)
    for g1, g2 in pairs:
        if g1.units > 0 and g2.units > 0:
            dead = g1.total_damage(g2.weak, g2.immune) // g2.hp
            dead = g2.units if g2.units < dead else dead
            g2.units -= dead


def target_selection(groups, team_im, team_in):
    pairs = []
    occupied = set()
    for g1 in groups:
        if g1.team == 0:
            if not team_in:
                continue
            for g2 in team_in:
                if g2 not in occupied:
                    g2.defence(g1.total_damage(g2.weak, g2.immune))
            m = max(team_in, key=lambda x: (x.defend, x.effective, x.initiative))
            if m.defend == 0:
                continue
            pairs.append((g1, m))
            occupied.add(m)
            team_in.remove(m)

        else:
            if not team_im:
                continue
            for g2 in team_im:
                if g2 not in occupied:
                    g2.defence(g1.total_damage(g2.weak, g2.immune))
            m = max(team_im, key=lambda x: (x.defend, x.effective, x.initiative))
            if m.defend == 0:
                continue
            pairs.append((g1, m))
            occupied.add(m)
            team_im.remove(m)

    return pairs


def main(inp):
    spl = inp.split('\n\n')
    team_immune = []
    team_infection = []
    for i in spl[0].splitlines()[1:]:
        team_immune.append(Group(*parse(i), 0))

    for i in spl[1].splitlines()[1:]:
        team_infection.append(Group(*parse(i), 1))
    
    _team_infection = 1
    _team_immune = 1
    part2=True
    boost = -1
    while _team_infection and bool(_team_immune)+part2:
        boost += 1
        _team_immune = deepcopy(team_immune)
        _team_infection = deepcopy(team_infection)
        for i in _team_immune:
            i.dmg += boost
        
        while len(_team_immune) > 0 and len(_team_infection) > 0:
            prev = sum([i.units for i in _team_immune + _team_infection])
            groups = _team_immune + _team_infection
            groups = sorted(groups, key=lambda x: (-x.effective, -x.initiative))
            attacking_pairs = target_selection(groups, _team_immune.copy(), _team_infection.copy())
            attacking(attacking_pairs)
            _team_immune = [i for i in _team_immune if i.units > 0]
            _team_infection = [i for i in _team_infection if i.units > 0]
            if prev == sum([i.units for i in _team_immune + _team_infection]):
                break

    winning_army = [i.units for i in _team_immune + _team_infection]

    return sum(winning_army),None
