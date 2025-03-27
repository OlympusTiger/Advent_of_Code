from collections import defaultdict
import networkx as nx
import matplotlib.pyplot as plt

def main(input_str):
    inputs, operations = input_str.split('\n\n')

    wires = defaultdict(lambda: None)

    graph = nx.Graph()
    node_positions = {}
    nodes_with_values = set()

    for line in inputs.splitlines():
        node, value = line.split(':')
        wires[node] = int(value)
        nodes_with_values.add(node)
        node_number = int(node[1:])
        if node[0] == 'x':
            node_positions[node] = (0, 2 * node_number)
        else:
            node_positions[node] = (0, 2 * node_number + 1)

    operations_lines = operations.splitlines()

    while operations_lines:
        line = operations_lines.pop(0)
        node_a, operator, node_b, _, node_c = line.split()
        if node_a not in nodes_with_values or node_b not in nodes_with_values:
            operations_lines.append(line)
            continue

        nodes_with_values.add(node_c)

        for node, position in node_positions.items():
            if node_a in node:
                node_a_y = position[1]
                node_a = node
            if node_b in node:
                node_b_y = position[1]
                node_b = node
        node_c_y = (node_a_y + node_b_y) / 2

        if operator == 'AND':
            graph.add_edge(node_a, operator + node_c)
            graph.add_edge(node_b, operator + node_c)
            if 'x' in node_a + node_b:
                node_c_x = 1.5
                if (node_c_x, node_c_y) in node_positions.values():
                    node_c_x = 3.2
                    node_c_y += 0.3
                node_positions[operator + node_c] = (node_c_x, node_c_y)
            else:
                node_c_x = 3
                if (node_c_x, node_c_y) in node_positions.values():
                    node_c_x = 3.2
                    node_c_y += 0.3
                node_positions[operator + node_c] = (node_c_x, node_c_y)
        elif operator == 'OR':
            graph.add_edge(node_a, operator + node_c)
            graph.add_edge(node_b, operator + node_c)
            node_c_x = 4
            if (node_c_x, node_c_y) in node_positions.values():
                node_c_x = 4.2
                node_c_y += 0.4
            node_positions[operator + node_c] = (node_c_x, node_c_y)
        else:
            graph.add_edge(node_a, operator + node_c)
            graph.add_edge(node_b, operator + node_c)
            if 'z' in node_c:
                node_c_x = 5
                if (node_c_x, node_c_y) in node_positions.values():
                    node_c_x = 5.2
                    node_c_y += 0.2
                node_positions[operator + node_c] = (node_c_x, node_c_y)
            elif 'x' in node_a + node_b:
                node_c_x = 2
                if (node_c_x, node_c_y) in node_positions.values():
                    node_c_x = 2.2
                    node_c_y += 0.2
                node_positions[operator + node_c] = (node_c_x, node_c_y)
            else:
                node_c_x = 3
                if (node_c_x, node_c_y) in node_positions.values():
                    node_c_x = 3.2
                    node_c_y += 0.2
                node_positions[operator + node_c] = (node_c_x, node_c_y)

    nx.draw(graph, node_positions, with_labels=True)
    plt.show()

    while True:
        for line in operations.splitlines():
            node_a, operator, node_b, _, node_c = line.split()
            if wires[node_a] is None or wires[node_b] is None:
                wires[node_c]
                continue
            if operator == 'AND':
                wires[node_c] = wires[node_a] & wires[node_b]
            elif operator == 'OR':
                wires[node_c] = wires[node_a] | wires[node_b]
            else:
                wires[node_c] = wires[node_a] ^ wires[node_b]
        if all(value is not None for value in wires.values()):
            break

    end_nodes = [node for node in wires if node.startswith('z')]
    end_nodes.sort(reverse=True)

    return int(''.join(str(wires[node]) for node in end_nodes), 2), None

