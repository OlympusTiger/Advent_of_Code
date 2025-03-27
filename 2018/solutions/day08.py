from collections import defaultdict


def value(n, nodes, v=0):
    if nodes[n]['n_childs'] == 0:
        print(sum(nodes[n]['metadata']))
        return v + sum(nodes[n]['metadata'])

    for i in nodes[n]['metadata']:
        if 0 < i <= nodes[n]['n_childs']:
            nn = nodes[n]['childs'][i-1]
            v = value(nn, nodes, v)

    return v


def recursive(n, data, nodes, i):
    for _ in range(nodes[n]['n_childs']):
        nn = max(nodes) + 1

        nodes[nn]['n_childs'] = data[i]
        n_metadata = data[i + 1]
        nodes[n]['childs'].append(nn)

        if nodes[nn]['n_childs'] == 0:
            nodes[nn]['metadata'] = data[i + 2:i + 2 + n_metadata]
            i += 2 + n_metadata

        else:
            i += 2

            nodes, i = recursive(nn, data, nodes, i)
            nodes[nn]['metadata'] = data[i:i + n_metadata]
            i += n_metadata

    return nodes, i


def main(inp):
    data = list(map(int, inp.split()))
    nodes = defaultdict(lambda: {'n_childs': 0, 'childs': [], 'metadata': []})

    nodes[0]['n_childs'] = data[0]

    nodes, i = recursive(0, data, nodes, 2)
    nodes[0]['metadata'] = data[i:]

    s = sum(map(lambda x: sum(nodes[x]['metadata']), nodes))

    return s, value(0, nodes)

