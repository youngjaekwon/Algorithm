from collections import deque
class Node:
    def __init__(self):
        self.connected = list()

def solution(n, wires):
    tree = dict()
    def extend_tree(x, y):
        if x not in tree:
            tree[x] = Node()
        tree[x].connected.append(y)
    for x, y in wires:
        extend_tree(x, y)
        extend_tree(y, x)
        
    def count_nodes(x, y):
        visited = set([x, y])
        queue = deque([x])
        count = 0
        while queue:
            v = queue.popleft()
            visited.add(v)
            count += 1
            queue.extend([n for n in tree[v].connected if n not in visited])
        return count
    
    answers = []
    for x, y in wires:
        answers.append((count_nodes(x, y), count_nodes(y, x)))
        
    answers.sort(key=lambda x: abs(x[0] - x[1]))
    return abs(answers[0][0] - answers[0][1])