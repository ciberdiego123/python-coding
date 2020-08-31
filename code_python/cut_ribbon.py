class Node:
    def __init__(self, n, parent=None):
        self.n = n
        self.node_a = None
        self.node_b = None
        self.node_c = None
        self.parent = parent

    def calculate_h(self):
        h = 1
        while self.parent is not None:
            h += 1
        return h

class Tree:
    def __init__(self, root):
        self.root = root


n, a, b, c = [int(i) for i in input().split()]
cache = dict()
solutions = []


def get_node(num):
    if num in cache:
        return cache[num]
    else:
        node = Node(num)
        na, nb, nc = num - a, num - b, num - c
        node.node_a = Node(na, node)
        node.node_b = Node(nb, node)
        node.node_c = Node(nc, node)
        cache[num] = Node
        if num == 0:
            solutions.append(node.calculate_h())
        return node


tp = Tree(get_node(n))
list_n_to_search = [tp.root.node_a, tp.root.node_b, tp.root.node_c]
nodes_visited = set()
while list_n_to_search:
    curr_n = list_n_to_search.pop(0)
    if curr_n in nodes_visited:
        continue
    else:
        nodes_visited.add(curr_n)
    c_node = get_node(curr_n)
    if c_node.node_a.n > 0:
        list_n_to_search.append(c_node.node_a.n)
    if c_node.node_b.n > 0:
        list_n_to_search.append(c_node.node_b.n)
    if c_node.node_c.n > 0:
        list_n_to_search.append(c_node.node_c.n)
print(max(solutions))



